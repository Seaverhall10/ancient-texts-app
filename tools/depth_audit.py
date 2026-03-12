"""
depth_audit.py - Analyze content depth across all era files
"""
import os
import sys
import ast
import traceback

def analyze_chapter(ch):
    """Analyze a single chapter dict for depth metrics."""
    result = {
        'id': ch.get('id', '?'),
        'title': ch.get('title', '?'),
        'ref': ch.get('ref', '?'),
        'type': ch.get('type', 'chapter'),
        'synopsis_len': len(ch.get('synopsis', '') or ''),
        'sections': [],
        'num_sections': 0,
        'total_section_chars': 0,
        'num_hebrew_terms': 0,
        'hebrew_terms': [],
        'num_cross_refs': 0,
        'ane_backdrop_len': 0,
        'ane_backdrop_preview': '',
        'second_temple_count': 0,
        'divine_council_len': 0,
        'key_verse': bool(ch.get('key_verse')),
    }

    # Sections - handle both heading/body and title/content patterns
    sections = ch.get('sections', []) or []
    result['num_sections'] = len(sections)
    for sec in sections:
        body = sec.get('body', '') or sec.get('content', '') or ''
        heading = sec.get('heading', '') or sec.get('title', '') or ''
        body_len = len(body)
        result['total_section_chars'] += body_len
        result['sections'].append({
            'heading': heading,
            'body_len': body_len
        })

    # Hebrew terms
    ht = ch.get('hebrew_terms', []) or []
    result['num_hebrew_terms'] = len(ht)
    result['hebrew_terms'] = ht

    # Cross refs
    cr = ch.get('cross_refs', []) or []
    result['num_cross_refs'] = len(cr)

    # ANE backdrop
    ane = ch.get('ane_backdrop', '') or ''
    if isinstance(ane, str):
        result['ane_backdrop_len'] = len(ane)
        result['ane_backdrop_preview'] = ane[:80] if ane else ''

    # Second temple
    st = ch.get('second_temple', []) or []
    result['second_temple_count'] = len(st)

    # Divine council note
    dc = ch.get('divine_council_note', '') or ''
    if isinstance(dc, str):
        result['divine_council_len'] = len(dc)

    return result


def load_era_file(filepath):
    """Load an era file and return the CHAPTERS list."""
    try:
        namespace = {}
        with open(filepath, 'r', encoding='utf-8') as f:
            exec(compile(f.read(), filepath, 'exec'), namespace)
        return namespace.get('CHAPTERS', [])
    except Exception as e:
        print(f"  ERROR loading {filepath}: {e}", file=sys.stderr)
        return []


def main():
    data_dir = 'data'

    # Find all era files grouped by book (exclude data/ root duplicates)
    books = {}
    for root, dirs, files in os.walk(data_dir):
        if os.path.basename(root) == 'data':
            continue  # Skip era files in the data/ root itself
        for f in files:
            if f.startswith('era_') and f.endswith('.py'):
                book = os.path.basename(root)
                fp = os.path.join(root, f)
                if book not in books:
                    books[book] = []
                books[book].append(fp)

    # Sort files within each book
    for book in books:
        books[book].sort()

    # Analyze each book
    book_stats = {}

    for book in sorted(books.keys()):
        era_files = books[book]
        stats = {
            'era_files': len(era_files),
            'chapters': 0,
            'study_chapters': 0,  # exclude inserts
            'total_sections': 0,
            'total_section_chars': 0,
            'total_hebrew_terms': 0,
            'total_cross_refs': 0,
            'total_second_temple': 0,
            'total_ane_chars': 0,
            'ane_chapters': 0,
            'total_dc_chars': 0,
            'dc_chapters': 0,
            'total_synopsis_chars': 0,
            'chapter_details': []
        }

        for fp in era_files:
            chapters = load_era_file(fp)
            for ch in chapters:
                analysis = analyze_chapter(ch)
                stats['chapters'] += 1
                if analysis['type'] in ('chapter', 'study'):
                    stats['study_chapters'] += 1
                stats['total_sections'] += analysis['num_sections']
                stats['total_section_chars'] += analysis['total_section_chars']
                stats['total_hebrew_terms'] += analysis['num_hebrew_terms']
                stats['total_cross_refs'] += analysis['num_cross_refs']
                stats['total_second_temple'] += analysis['second_temple_count']
                stats['total_synopsis_chars'] += analysis['synopsis_len']
                if analysis['ane_backdrop_len'] > 10:
                    stats['total_ane_chars'] += analysis['ane_backdrop_len']
                    stats['ane_chapters'] += 1
                if analysis['divine_council_len'] > 10:
                    stats['total_dc_chars'] += analysis['divine_council_len']
                    stats['dc_chapters'] += 1
                stats['chapter_details'].append(analysis)

        book_stats[book] = stats

    # Print table
    print()
    print("=" * 160)
    print(f"{'BOOK':<22} {'ERAS':>5} {'CHAPS':>6} {'STUDY':>6} {'SECTS':>6} {'SEC KB':>7} {'AVG/S':>6} "
          f"{'HEB T':>6} {'XREFS':>6} {'2NDTM':>6} {'ANE#':>5} {'ANE KB':>7} {'DC#':>4} {'DC KB':>6} {'SYN KB':>7}")
    print("=" * 160)

    for book in sorted(book_stats.keys()):
        s = book_stats[book]
        avg_sec = s['total_section_chars'] // s['total_sections'] if s['total_sections'] > 0 else 0
        sec_kb = s['total_section_chars'] / 1024
        ane_kb = s['total_ane_chars'] / 1024
        dc_kb = s['total_dc_chars'] / 1024
        syn_kb = s['total_synopsis_chars'] / 1024

        print(f"{book:<22} {s['era_files']:>5} {s['chapters']:>6} {s['study_chapters']:>6} "
              f"{s['total_sections']:>6} {sec_kb:>7.1f} {avg_sec:>6} "
              f"{s['total_hebrew_terms']:>6} {s['total_cross_refs']:>6} {s['total_second_temple']:>6} "
              f"{s['ane_chapters']:>5} {ane_kb:>7.1f} {s['dc_chapters']:>4} {dc_kb:>6.1f} {syn_kb:>7.1f}")

    print("=" * 160)

    # Genesis detailed analysis
    print("\n\n" + "=" * 80)
    print("GENESIS GOLD STANDARD - DETAILED CHAPTER BREAKDOWN")
    print("=" * 80)
    if 'genesis' in book_stats:
        for ch in book_stats['genesis']['chapter_details']:
            if ch['type'] != 'chapter':
                continue
            avg_body = ch['total_section_chars'] // ch['num_sections'] if ch['num_sections'] > 0 else 0
            print(f"\n  {ch['ref']}: \"{ch['title']}\"")
            print(f"    Sections: {ch['num_sections']}  |  Total body chars: {ch['total_section_chars']}  |  Avg body: {avg_body}")
            print(f"    Hebrew terms: {ch['num_hebrew_terms']} {ch['hebrew_terms']}")
            print(f"    Cross-refs: {ch['num_cross_refs']}  |  Second Temple: {ch['second_temple_count']}")
            print(f"    ANE backdrop: {ch['ane_backdrop_len']} chars  |  Divine Council: {ch['divine_council_len']} chars")
            print(f"    Synopsis: {ch['synopsis_len']} chars")
            if ch['sections']:
                for sec in ch['sections']:
                    print(f"      -> \"{sec['heading']}\": {sec['body_len']} chars")

    # Comparative summary - find thin books
    print("\n\n" + "=" * 80)
    print("COMPARATIVE DEPTH ANALYSIS")
    print("=" * 80)

    gen = book_stats.get('genesis', {})
    gen_avg_sec_chars = gen.get('total_section_chars', 0) / gen.get('total_sections', 1)
    gen_avg_ht = gen.get('total_hebrew_terms', 0) / gen.get('study_chapters', 1) if gen.get('study_chapters') else 0
    gen_avg_xref = gen.get('total_cross_refs', 0) / gen.get('study_chapters', 1) if gen.get('study_chapters') else 0
    gen_avg_secs = gen.get('total_sections', 0) / gen.get('study_chapters', 1) if gen.get('study_chapters') else 0

    print(f"\nGenesis baseline (per study chapter):")
    print(f"  Avg sections/chapter: {gen_avg_secs:.1f}")
    print(f"  Avg chars/section: {gen_avg_sec_chars:.0f}")
    print(f"  Avg hebrew terms/chapter: {gen_avg_ht:.1f}")
    print(f"  Avg cross-refs/chapter: {gen_avg_xref:.1f}")

    print(f"\n{'BOOK':<22} {'SECTS/CH':>9} {'%GEN':>6} {'CHR/SEC':>8} {'%GEN':>6} {'HT/CH':>7} {'%GEN':>6} {'XR/CH':>7} {'%GEN':>6} {'VERDICT':>10}")
    print("-" * 100)

    for book in sorted(book_stats.keys()):
        s = book_stats[book]
        if s['study_chapters'] == 0:
            continue

        avg_secs = s['total_sections'] / s['study_chapters']
        avg_chr_sec = s['total_section_chars'] / s['total_sections'] if s['total_sections'] > 0 else 0
        avg_ht = s['total_hebrew_terms'] / s['study_chapters']
        avg_xr = s['total_cross_refs'] / s['study_chapters']

        pct_secs = (avg_secs / gen_avg_secs * 100) if gen_avg_secs > 0 else 0
        pct_chr = (avg_chr_sec / gen_avg_sec_chars * 100) if gen_avg_sec_chars > 0 else 0
        pct_ht = (avg_ht / gen_avg_ht * 100) if gen_avg_ht > 0 else 0
        pct_xr = (avg_xr / gen_avg_xref * 100) if gen_avg_xref > 0 else 0

        avg_pct = (pct_secs + pct_chr + pct_ht + pct_xr) / 4

        if avg_pct >= 80:
            verdict = "STRONG"
        elif avg_pct >= 50:
            verdict = "MODERATE"
        elif avg_pct >= 25:
            verdict = "THIN"
        else:
            verdict = "VERY THIN"

        marker = ""
        if book == "genesis":
            verdict = "STANDARD"

        print(f"{book:<22} {avg_secs:>9.1f} {pct_secs:>5.0f}% {avg_chr_sec:>8.0f} {pct_chr:>5.0f}% "
              f"{avg_ht:>7.1f} {pct_ht:>5.0f}% {avg_xr:>7.1f} {pct_xr:>5.0f}% {verdict:>10}")


if __name__ == '__main__':
    main()

"""
build_content_map.py — Content Navigation & Analytics Generator

Builds CONTENT_MAP.json: the master index for the entire Ancient Texts Study App.
Any AI agent reads this ONCE and knows EVERYTHING about the app — what exists,
what's missing, where cross-references point, statistics, hot passages, gaps.

Run: python agents/build_content_map.py
Output: CONTENT_MAP.json (project root)

The CONTENT_MAP contains:
  - texts: all 50 texts with status (has_flow, has_interlinear, era_count, etc.)
  - eras: all 147 eras with chapter counts, themes, key verses
  - cross_ref_index: every cited passage → which chapters cite it
  - hot_passages: most frequently cross-referenced scriptures
  - glossary_index: term → chapters that use it
  - flow_stats: verse/note counts per book
  - gaps: what's missing (no flow, no interlinear, thin notes, etc.)
  - connection_map: topic clusters across books (divine council, Messiah, etc.)
"""

import os
import sys
import json
import re
import importlib.util
from collections import defaultdict
from datetime import datetime

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

DATA_DIR     = os.path.join(ROOT, 'data')
MANIFEST_PATH = os.path.join(ROOT, 'manifest.json')
FLOW_DIR     = os.path.join(DATA_DIR, 'flow')
OUTPUT_PATH  = os.path.join(ROOT, 'CONTENT_MAP.json')


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_era_file(text_id, data_file, data_dir=None):
    """Load era file, respecting data_dir override (e.g. 1enoch -> enoch1)."""
    actual_dir = data_dir if data_dir else text_id
    text_dir = os.path.join(DATA_DIR, actual_dir)
    for path in [os.path.join(text_dir, data_file + '.py'),
                 os.path.join(DATA_DIR, data_file + '.py')]:
        if os.path.exists(path):
            try:
                mod = load_module('era_' + data_file, path)
                return getattr(mod, 'CHAPTERS', [])
            except Exception:
                return []
    return []


def extract_crossrefs(chapter):
    """Extract all cross-reference strings from a chapter dict."""
    refs = []
    for r in chapter.get('cross_refs', []):
        ref_str = r.get('ref', '')
        if ref_str:
            refs.append({
                'ref': ref_str,
                'type': r.get('type', '?'),
                'note': r.get('note', '')[:120]
            })
    return refs


def extract_body_text(chapter):
    """Get plain text from sections."""
    parts = []
    for s in chapter.get('sections', []):
        body = re.sub(r'<[^>]+>', '', s.get('body', ''))
        parts.append(body)
    return ' '.join(parts)


def load_flow_stats(text_id):
    """Return {verses, notes, chapters} for a flow file."""
    flow_path = os.path.join(FLOW_DIR, f'flow_{text_id}.py')
    if not os.path.exists(flow_path):
        return None
    try:
        mod = load_module('flow_' + text_id, flow_path)
        flow_var  = next((v for v in dir(mod) if v.startswith('FLOW_')),  None)
        notes_var = next((v for v in dir(mod) if v.startswith('NOTES_')), None)
        flow  = getattr(mod, flow_var,  {}) if flow_var  else {}
        notes = getattr(mod, notes_var, {}) if notes_var else {}
        total_v = sum(len(ch) for ch in flow.values())
        total_n = sum(len(ch) for ch in notes.values())
        return {
            'chapters': len(flow),
            'verses': total_v,
            'notes': total_n,
            'coverage': 'complete' if total_v > 0 else 'empty'
        }
    except Exception as e:
        return {'error': str(e)}


def load_interlinear_stats(text_id):
    """Return chapter/word count for a text's interlinear data."""
    candidates = [
        os.path.join(DATA_DIR, f'interlinear_{text_id}.py'),
        os.path.join(DATA_DIR, f'interlinear_nt_{text_id}.py'),
    ]
    # Genesis stores its interlinear in its own subdirectory as interlinear.py
    if text_id == 'genesis':
        candidates.append(os.path.join(DATA_DIR, 'genesis', 'interlinear.py'))
    for path in candidates:
        if os.path.exists(path):
            try:
                mod = load_module('il_' + text_id, path)
                var = next((v for v in dir(mod)
                           if v.startswith('INTERLINEAR') and not v.startswith('INTERLINEAR_NT')
                           and text_id.upper().replace('1', '').replace('2', '') in v.upper()
                           or v == 'INTERLINEAR'), None)
                if not var:
                    # Try NT pattern
                    var = next((v for v in dir(mod) if v.startswith('INTERLINEAR_')), None)
                if not var:
                    continue
                data = getattr(mod, var, {})
                # Count words (handle both OT and NT structures)
                total_words = 0
                for ch in data.values():
                    if isinstance(ch, dict):
                        verses = ch.get('verses', [])
                        if verses:
                            for v in verses:
                                total_words += len(v.get('words', []))
                        else:
                            # OT flat: {verse_num: [words]}
                            for v_data in ch.values():
                                if isinstance(v_data, list):
                                    total_words += len(v_data)
                return {
                    'chapters': len(data),
                    'words': total_words,
                    'language': 'greek' if 'NT' in var else 'hebrew',
                    'file': os.path.basename(path)
                }
            except Exception as e:
                return {'error': str(e)}
    return None


# ── Key topic keywords for connection mapping ──────────────────────────────
TOPIC_KEYWORDS = {
    'divine_council':    ['divine council', 'heavenly court', 'sons of god', 'b\'nei elohim', 'elohim', 'psalm 82', 'watchers'],
    'messiah':           ['messiah', 'anointed', 'christ', 'servant', 'fulfillment', 'prophecy', 'seed of woman'],
    'creation':          ['creation', 'bereshit', 'genesis 1', 'ex nihilo', 'made', 'formed', 'bara'],
    'covenant':          ['covenant', 'berith', 'promise', 'oath', 'faithfulness', 'hesed'],
    'flood_judgment':    ['flood', 'nephilim', 'genesis 6', 'watchers', 'judgment', 'noah'],
    'resurrection':      ['resurrection', 'raised', 'empty tomb', 'anastasis', 'life from dead'],
    'exile_return':      ['exile', 'babylon', 'return', 'restoration', 'scattered', 'gathered'],
    'temple':            ['temple', 'tabernacle', 'sanctuary', 'shekinah', 'holy of holies', 'presence'],
    'law_grace':         ['law', 'torah', 'grace', 'works', 'faith', 'justification', 'righteousness'],
    'eschatology':       ['eschatology', 'last days', 'end times', 'apocalypse', 'new creation', 'consummation'],
}


def score_topic(text_blob, keywords):
    text_lower = text_blob.lower()
    return sum(1 for kw in keywords if kw in text_lower)


def build_content_map():
    print('Building CONTENT_MAP.json...')
    print('=' * 60)

    with open(MANIFEST_PATH, encoding='utf-8') as f:
        manifest = json.load(f)

    texts = manifest.get('texts', [])
    eras  = manifest.get('eras', [])

    content_map = {
        'generated': datetime.now().isoformat(),
        'version': '1.0',
        'summary': {},
        'texts': {},
        'eras': {},
        'cross_ref_index': defaultdict(list),  # ref_str → [{chapter_id, text_id, note}]
        'hot_passages': [],
        'flow_stats': {},
        'interlinear_stats': {},
        'gaps': {
            'no_flow': [],
            'no_interlinear': [],
            'thin_eras': [],       # texts with < 2 eras
            'empty_eras': [],      # eras with 0 chapters
            'missing_files': [],   # era data_files not found on disk
        },
        'topic_connections': defaultdict(list),  # topic → [{text_id, era_id, score}]
        'glossary_index': {},
        'schema_info': {
            'cross_ref_index': 'Maps "Book ch:v" → list of {chapter_id, era_id, text_id, note}',
            'hot_passages': 'Top 50 most cross-referenced passages across all era files',
            'topic_connections': 'Maps topic name → list of {text_id, era_id, score} sorted by relevance',
            'gaps.no_flow': 'text_ids with no flow translation file',
            'gaps.no_interlinear': 'text_ids with no interlinear data',
        }
    }

    # ── Process each text ──────────────────────────────────────────────
    print(f'Processing {len(texts)} texts...')
    for t in texts:
        tid   = t['id']
        tname = t.get('name', tid)
        cat   = t.get('category', '?')

        text_eras = [e for e in eras if e.get('text') == tid]

        # Flow stats
        flow = load_flow_stats(tid)
        if flow:
            content_map['flow_stats'][tid] = flow
        else:
            if cat in ('ot', 'nt'):
                content_map['gaps']['no_flow'].append(tid)

        # Interlinear stats
        il = load_interlinear_stats(tid)
        if il:
            content_map['interlinear_stats'][tid] = il
        else:
            if t.get('interlinear'):
                content_map['gaps']['no_interlinear'].append(tid)

        # Era count check
        if len(text_eras) < 2 and cat in ('ot', 'nt'):
            content_map['gaps']['thin_eras'].append({
                'text_id': tid,
                'era_count': len(text_eras)
            })

        content_map['texts'][tid] = {
            'name': tname,
            'category': cat,
            'chapters': t.get('chapters', 0),
            'era_count': len(text_eras),
            'has_flow': flow is not None,
            'has_interlinear': il is not None,
            'flow_verses': flow.get('verses', 0) if flow else 0,
            'il_words': il.get('words', 0) if il else 0,
            'il_language': il.get('language', '') if il else '',
            'era_ids': [e['id'] for e in text_eras],
        }

    # ── Build data_dir lookup (some texts have data_dir != text_id) ────
    text_data_dirs = {t['id']: t.get('data_dir', t['id']) for t in texts}

    # ── Process each era ──────────────────────────────────────────────
    print(f'Processing {len(eras)} eras...')
    for e in eras:
        eid      = e['id']
        text_id  = e.get('text', '')
        data_file = e.get('data_file', '')
        chapters = []

        if data_file:
            data_dir = text_data_dirs.get(text_id)
            chapters = load_era_file(text_id, data_file, data_dir=data_dir)
            if not chapters:
                content_map['gaps']['missing_files'].append({
                    'era_id': eid,
                    'text_id': text_id,
                    'data_file': data_file
                })
            elif len(chapters) == 0:
                content_map['gaps']['empty_eras'].append(eid)

        # Accumulate cross-refs and topic scores
        all_body_text = ''
        all_cross_refs = []
        chapter_index = []
        for ch in chapters:
            cid  = ch.get('id', '')
            cref = ch.get('ref', '')
            cross_refs = extract_crossrefs(ch)
            body_text  = extract_body_text(ch)
            all_body_text  += ' ' + body_text
            all_cross_refs += cross_refs

            chapter_index.append({
                'id': cid,
                'ref': cref,
                'title': ch.get('title', ''),
                'synopsis': ch.get('synopsis', '')[:200],
                'key_verse': (ch.get('key_verse') or {}).get('ref', ''),
                'cross_ref_count': len(cross_refs),
                'has_divine_council_note': bool(ch.get('divine_council_note')),
                'hebrew_terms': ch.get('hebrew_terms', []),
            })

            # Add to cross-ref index
            for r in cross_refs:
                ref_str = r['ref']
                content_map['cross_ref_index'][ref_str].append({
                    'chapter_id': cid,
                    'chapter_ref': cref,
                    'era_id': eid,
                    'text_id': text_id,
                    'note': r['note'][:80]
                })

        # Topic scoring
        for topic, keywords in TOPIC_KEYWORDS.items():
            score = score_topic(all_body_text, keywords)
            if score > 0:
                content_map['topic_connections'][topic].append({
                    'text_id': text_id,
                    'era_id': eid,
                    'era_name': e.get('name', eid),
                    'score': score
                })

        content_map['eras'][eid] = {
            'text_id': text_id,
            'name': e.get('name', eid),
            'chapters_ref': e.get('chapters', ''),
            'chapter_count': len(chapters),
            'themes': e.get('themes', []),
            'chapters': chapter_index,
            'cross_ref_count': len(all_cross_refs),
            'has_data_file': bool(data_file),
        }

    # ── Hot passages (most cited) ──────────────────────────────────────
    print('Computing hot passages...')
    ref_counts = {ref: len(cites) for ref, cites in content_map['cross_ref_index'].items()}
    hot = sorted(ref_counts.items(), key=lambda x: x[1], reverse=True)[:50]
    content_map['hot_passages'] = [
        {
            'ref': ref,
            'cited_count': count,
            'cited_in': [c['text_id'] for c in content_map['cross_ref_index'][ref]][:8]
        }
        for ref, count in hot
    ]

    # ── Sort topic connections by score ───────────────────────────────
    for topic in content_map['topic_connections']:
        content_map['topic_connections'][topic].sort(key=lambda x: x['score'], reverse=True)

    # ── Glossary index ────────────────────────────────────────────────
    print('Building glossary index...')
    glossary_path = os.path.join(DATA_DIR, 'glossary.py')
    if os.path.exists(glossary_path):
        try:
            gmod = load_module('glossary', glossary_path)
            glossary = getattr(gmod, 'GLOSSARY', {})
            for term_key, term_data in glossary.items():
                content_map['glossary_index'][term_key] = {
                    'gloss': term_data.get('gloss', ''),
                    'strongs': term_data.get('strongs', ''),
                    'chapters_used': term_data.get('chapters_used', []),
                    'language': term_data.get('language', 'hebrew'),
                }
            print(f'  {len(glossary)} glossary terms indexed')
        except Exception as e:
            print(f'  Glossary error: {e}')

    # ── Summary statistics ────────────────────────────────────────────
    total_flow_verses = sum(s.get('verses', 0) for s in content_map['flow_stats'].values())
    total_il_words    = sum(s.get('words', 0) for s in content_map['interlinear_stats'].values()
                           if isinstance(s, dict) and 'words' in s)
    total_chapters    = sum(e['chapter_count'] for e in content_map['eras'].values())
    total_crossrefs   = sum(len(v) for v in content_map['cross_ref_index'].values())

    content_map['summary'] = {
        'total_texts': len(texts),
        'total_eras': len(eras),
        'total_study_chapters': total_chapters,
        'total_flow_verses': total_flow_verses,
        'total_il_words': total_il_words,
        'total_cross_refs': total_crossrefs,
        'unique_passages_cited': len(content_map['cross_ref_index']),
        'glossary_terms': len(content_map['glossary_index']),
        'texts_with_flow': sum(1 for s in content_map['flow_stats'].values() if s and s.get('verses', 0) > 0),
        'texts_with_interlinear': len(content_map['interlinear_stats']),
        'gap_count': {
            'no_flow': len(content_map['gaps']['no_flow']),
            'no_interlinear': len(content_map['gaps']['no_interlinear']),
            'thin_eras': len(content_map['gaps']['thin_eras']),
            'missing_files': len(content_map['gaps']['missing_files']),
        }
    }

    # Convert defaultdicts to regular dicts for JSON serialization
    content_map['cross_ref_index']   = dict(content_map['cross_ref_index'])
    content_map['topic_connections']  = dict(content_map['topic_connections'])

    # Write output
    print(f'\nWriting {OUTPUT_PATH}...')
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(content_map, f, ensure_ascii=False, indent=2)

    file_size_mb = os.path.getsize(OUTPUT_PATH) / (1024 * 1024)
    print(f'DONE: {OUTPUT_PATH} ({file_size_mb:.1f} MB)')

    # Print summary
    s = content_map['summary']
    print(f"""
╔══════════════════════════════════════════╗
║         CONTENT MAP SUMMARY             ║
╠══════════════════════════════════════════╣
║ Texts:            {s['total_texts']:>6}                  ║
║ Eras:             {s['total_eras']:>6}                  ║
║ Study chapters:   {s['total_study_chapters']:>6}                  ║
║ Flow verses:      {s['total_flow_verses']:>6}                  ║
║ Interlinear words:{s['total_il_words']:>6,}               ║
║ Cross-references: {s['total_cross_refs']:>6}                  ║
║ Unique passages:  {s['unique_passages_cited']:>6}                  ║
║ Glossary terms:   {s['glossary_terms']:>6}                  ║
╠══════════════════════════════════════════╣
║ GAPS:                                    ║
║ No flow:          {s['gap_count']['no_flow']:>6}                  ║
║ No interlinear:   {s['gap_count']['no_interlinear']:>6}                  ║
║ Thin eras (<2):   {s['gap_count']['thin_eras']:>6}                  ║
║ Missing files:    {s['gap_count']['missing_files']:>6}                  ║
╚══════════════════════════════════════════╝
""")
    return content_map


if __name__ == '__main__':
    build_content_map()

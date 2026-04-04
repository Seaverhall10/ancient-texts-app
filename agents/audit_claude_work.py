"""
audit_claude_work.py — Audit all Claude Code output

Validates map journeys, waypoint data, era files, flow translations,
interlinear data, glossary entries, cross-references, code structure,
BOOK_TO_TEXT mapping, color assignments, geographic coordinates,
and theological accuracy.

Usage:
    python agents/audit_claude_work.py --map          # Audit MAP_JOURNEYS
    python agents/audit_claude_work.py --waypoints    # Audit all waypoint data
    python agents/audit_claude_work.py --colors       # Audit color uniqueness/visibility
    python agents/audit_claude_work.py --coords       # Validate geographic coordinates
    python agents/audit_claude_work.py --links        # Validate "Read in App" links
    python agents/audit_claude_work.py --eras         # Audit era file depth/structure
    python agents/audit_claude_work.py --flow         # Audit flow translation files
    python agents/audit_claude_work.py --interlinear  # Audit interlinear data
    python agents/audit_claude_work.py --glossary     # Audit glossary entries
    python agents/audit_claude_work.py --xrefs        # Audit cross-reference quality
    python agents/audit_claude_work.py --code         # Audit code structure (CSS/JS/build)
    python agents/audit_claude_work.py --all          # Map-related audits (default)
    python agents/audit_claude_work.py --full-app     # Full app audit (everything)
    python agents/audit_claude_work.py --ai-review    # AI theological review of descriptions
"""
import re
import sys
import os
import json
import math
import argparse
from datetime import datetime
import importlib.util

# Windows UTF-8 fix
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Import shared config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.config import (
    PROJECT_ROOT, DATA_DIR, MANIFEST_PATH, REPORTS_DIR,
    ARBITER_API_KEY, ARBITER_MODEL, ARBITER_TEMPERATURE,
    AUDIT_LEVELS, THEOLOGICAL_GUIDELINES
)


# ══════════════════════════════════════════════════════════
# CONSTANTS
# ══════════════════════════════════════════════════════════

APP_JS = os.path.join(PROJECT_ROOT, 'src', 'js', 'app.js')

# Valid coordinate bounds for biblical geography
COORD_BOUNDS = {
    'lat_min': 25.0,   # Southern Egypt
    'lat_max': 42.0,   # Northern Turkey
    'lng_min': 25.0,   # Libya
    'lng_max': 55.0,   # Persia
}

# Minimum color distance (in RGB space) to consider "distinct"
MIN_COLOR_DISTANCE = 60

# Known epoch order for validation
EPOCH_ORDER = [
    'watcher_descent', 'nimrod_expansion',                          # PRIMEVAL
    'abraham', 'abrahams_war', 'isaac', 'jacob', 'joseph',         # PATRIARCHS
    'moses_life', 'exodus', 'spies_route', 'balaam', 'wilderness', # EXODUS
    'conquest', 'philistine_migration', 'ark_journey',             # CONQUEST
    'giant_slayer', 'david_flight', 'elijah', 'phoenician_trade',  # KINGDOM
    'jesus_galilee', 'jesus_final_week',                           # JESUS
    'paul_journey1', 'paul_journey2', 'paul_journey3',             # APOSTOLIC
]


# ══════════════════════════════════════════════════════════
# 1. EXTRACT JOURNEYS — Parse MAP_JOURNEYS from app.js
# ══════════════════════════════════════════════════════════

def extract_journeys():
    """Extract all journey objects from MAP_JOURNEYS array in app.js."""
    if not os.path.exists(APP_JS):
        return None, f"app.js not found at {APP_JS}"

    with open(APP_JS, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find MAP_JOURNEYS array
    start = content.find('var MAP_JOURNEYS = [')
    if start == -1:
        return None, "MAP_JOURNEYS array not found in app.js"

    # Find matching ];
    bracket_depth = 0
    in_string = False
    escape_next = False
    end = start
    for i in range(start, len(content)):
        c = content[i]
        if escape_next:
            escape_next = False
            continue
        if c == '\\':
            escape_next = True
            continue
        if c == "'" and not in_string:
            in_string = True
            continue
        if c == "'" and in_string:
            in_string = False
            continue
        if not in_string:
            if c == '[':
                bracket_depth += 1
            elif c == ']':
                bracket_depth -= 1
                if bracket_depth == 0:
                    end = i + 1
                    break

    array_text = content[start:end]

    # Extract individual journey objects by splitting on journey id boundaries
    # Handles both formats: {id: 'xxx' (inline) and {\n            id: 'xxx' (newline)
    journeys = []
    journey_sections = re.split(r'(?=\{(?:\s*\n\s*)?id:\s)', array_text)

    for section in journey_sections:
        id_match = re.search(r"id:\s*'([^']+)'", section)
        if not id_match:
            continue

        jid = id_match.group(1)
        name_match = re.search(r"name:\s*'([^']*(?:\\.[^']*)*)'", section)
        color_match = re.search(r"color:\s*'(#[0-9a-fA-F]+)'", section)
        desc_match = re.search(r"desc:\s*'([^']*(?:\\.[^']*)*)'", section)
        refs_match = re.search(r"refs:\s*'([^']*(?:\\.[^']*)*)'", section)

        # Extract waypoints
        waypoints = []
        wp_pattern = (
            r"\{lat:([\d.-]+),\s*lng:([\d.-]+),\s*"
            r"label:'([^']*(?:\\.[^']*)*)'(?:,\s*ref:'([^']*(?:\\.[^']*)*)')?"
            r"(?:,\s*desc:'([^']*(?:\\.[^']*)*)')?"
        )
        for wp_match in re.finditer(wp_pattern, section):
            waypoints.append({
                'lat': float(wp_match.group(1)),
                'lng': float(wp_match.group(2)),
                'label': wp_match.group(3),
                'ref': wp_match.group(4) or '',
                'desc': wp_match.group(5) or '',
            })

        journeys.append({
            'id': jid,
            'name': name_match.group(1) if name_match else '',
            'color': color_match.group(1) if color_match else '',
            'desc': desc_match.group(1) if desc_match else '',
            'refs': refs_match.group(1) if refs_match else '',
            'waypoints': waypoints,
        })

    return journeys, None


# ══════════════════════════════════════════════════════════
# 2. AUDIT MAP JOURNEYS — Main structure audit
# ══════════════════════════════════════════════════════════

def audit_map_journeys():
    """Audit MAP_JOURNEYS array for completeness and structure."""
    findings = []
    journeys, err = extract_journeys()
    if err:
        findings.append(('CRITICAL', 'map_structure', err))
        return findings

    print(f"  Found {len(journeys)} journeys")

    # Check journey count
    if len(journeys) < 20:
        findings.append(('WARNING', 'journey_count',
            f'Only {len(journeys)} journeys found (expected 20+)'))

    # Check each journey has required fields
    for j in journeys:
        if not j['name']:
            findings.append(('CRITICAL', j['id'], 'Missing journey name'))
        if not j['color']:
            findings.append(('CRITICAL', j['id'], 'Missing journey color'))
        if not j['desc']:
            findings.append(('WARNING', j['id'], 'Missing journey description'))
        if not j['refs']:
            findings.append(('WARNING', j['id'], 'Missing scripture references'))
        if len(j['waypoints']) < 3:
            findings.append(('WARNING', j['id'],
                f"Only {len(j['waypoints'])} waypoints (minimum 3 expected)"))

        # Check waypoints have descriptions
        wp_without_desc = sum(1 for wp in j['waypoints'] if not wp['desc'])
        if wp_without_desc > 0:
            findings.append(('INFO', j['id'],
                f"{wp_without_desc}/{len(j['waypoints'])} waypoints missing descriptions"))

        # Check waypoints have refs
        wp_without_ref = sum(1 for wp in j['waypoints'] if not wp['ref'])
        if wp_without_ref > 0:
            findings.append(('WARNING', j['id'],
                f"{wp_without_ref}/{len(j['waypoints'])} waypoints missing scripture refs"))

    # Check chronological order
    found_ids = [j['id'] for j in journeys]
    expected_order = [eid for eid in EPOCH_ORDER if eid in found_ids]
    if found_ids != expected_order:
        findings.append(('WARNING', 'epoch_order',
            'Journeys not in expected chronological order'))
        # Show which are out of order
        for i, (found, expected) in enumerate(zip(found_ids, expected_order)):
            if found != expected:
                findings.append(('INFO', 'epoch_order',
                    f"  Position {i}: found '{found}', expected '{expected}'"))
                break

    return findings


# ══════════════════════════════════════════════════════════
# 3. AUDIT COLORS — Uniqueness and visibility
# ══════════════════════════════════════════════════════════

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def color_distance(c1, c2):
    """Calculate Euclidean distance between two RGB colors."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))


def audit_colors():
    """Audit journey colors for uniqueness and visibility."""
    findings = []
    journeys, err = extract_journeys()
    if err:
        findings.append(('CRITICAL', 'colors', err))
        return findings

    colors = {}
    for j in journeys:
        if j['color']:
            if j['color'] in colors:
                findings.append(('CRITICAL', 'duplicate_color',
                    f"'{j['id']}' and '{colors[j['color']]}' share color {j['color']}"))
            colors[j['color']] = j['id']

    # Check for similar colors
    color_list = [(jid, hex_to_rgb(color)) for color, jid in colors.items()]
    for i in range(len(color_list)):
        for k in range(i + 1, len(color_list)):
            dist = color_distance(color_list[i][1], color_list[k][1])
            if dist < MIN_COLOR_DISTANCE:
                findings.append(('WARNING', 'similar_colors',
                    f"'{color_list[i][0]}' and '{color_list[k][0]}' colors are very similar (distance: {dist:.0f})"))

    # Check for yellow/gold colors (bad on map terrain)
    YELLOW_RANGE = {'r_min': 180, 'g_min': 150, 'b_max': 100}
    for j in journeys:
        if j['color']:
            r, g, b = hex_to_rgb(j['color'])
            if r > YELLOW_RANGE['r_min'] and g > YELLOW_RANGE['g_min'] and b < YELLOW_RANGE['b_max']:
                findings.append(('WARNING', j['id'],
                    f"Color {j['color']} appears yellowish/gold -- poor visibility on map terrain"))

    print(f"  Checked {len(colors)} unique colors")
    return findings


# ══════════════════════════════════════════════════════════
# 4. AUDIT COORDINATES — Geographic validation
# ══════════════════════════════════════════════════════════

def audit_coordinates():
    """Validate geographic coordinates and check for zigzag paths."""
    findings = []
    journeys, err = extract_journeys()
    if err:
        findings.append(('CRITICAL', 'coords', err))
        return findings

    for j in journeys:
        wps = j['waypoints']
        if len(wps) < 2:
            continue

        # Check bounds
        for i, wp in enumerate(wps):
            if not (COORD_BOUNDS['lat_min'] <= wp['lat'] <= COORD_BOUNDS['lat_max']):
                findings.append(('WARNING', j['id'],
                    f"Waypoint {i+1} '{wp['label'][:30]}' lat {wp['lat']} outside expected range"))
            if not (COORD_BOUNDS['lng_min'] <= wp['lng'] <= COORD_BOUNDS['lng_max']):
                findings.append(('WARNING', j['id'],
                    f"Waypoint {i+1} '{wp['label'][:30]}' lng {wp['lng']} outside expected range"))

        # Check for duplicate coordinates
        seen_coords = {}
        for i, wp in enumerate(wps):
            coord_key = f"{wp['lat']:.2f},{wp['lng']:.2f}"
            if coord_key in seen_coords:
                findings.append(('WARNING', j['id'],
                    f"Waypoints {seen_coords[coord_key]+1} and {i+1} share coordinates ({coord_key})"))
            seen_coords[coord_key] = i

        # Check for geographic zigzags (simplified: large backtracking)
        if len(wps) >= 4:
            total_direct = math.sqrt(
                (wps[-1]['lat'] - wps[0]['lat'])**2 +
                (wps[-1]['lng'] - wps[0]['lng'])**2
            )
            total_path = sum(
                math.sqrt(
                    (wps[i+1]['lat'] - wps[i]['lat'])**2 +
                    (wps[i+1]['lng'] - wps[i]['lng'])**2
                ) for i in range(len(wps) - 1)
            )
            if total_direct > 0 and total_path / total_direct > 4.0:
                findings.append(('INFO', j['id'],
                    f"Path efficiency ratio {total_path/total_direct:.1f}x -- possible zigzag (review manually)"))

    print(f"  Validated coordinates for {len(journeys)} journeys")
    return findings


# ══════════════════════════════════════════════════════════
# 5. AUDIT READ LINKS — Validate "Read in App" resolution
# ══════════════════════════════════════════════════════════

def audit_read_links():
    """Validate that waypoint refs can resolve to valid text IDs via BOOK_TO_TEXT."""
    findings = []

    if not os.path.exists(APP_JS):
        findings.append(('CRITICAL', 'links', f"app.js not found at {APP_JS}"))
        return findings

    # Extract BOOK_TO_TEXT from app.js
    with open(APP_JS, 'r', encoding='utf-8') as f:
        content = f.read()

    book_map = {}
    btt_match = re.search(r'var BOOK_TO_TEXT\s*=\s*\{([^}]+)\}', content, re.DOTALL)
    if btt_match:
        for entry in re.finditer(r"'([^']+)'\s*:\s*'([^']+)'", btt_match.group(1)):
            book_map[entry.group(1).lower()] = entry.group(2)

    if not book_map:
        findings.append(('CRITICAL', 'book_map',
            'BOOK_TO_TEXT mapping not found or empty'))
        return findings

    print(f"  Found {len(book_map)} BOOK_TO_TEXT mappings")

    # Load manifest to check valid text IDs
    valid_texts = set()
    if os.path.exists(MANIFEST_PATH):
        with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
        for text in manifest.get('texts', []):
            valid_texts.add(text['id'])

    # Check each journey waypoint ref can resolve
    journeys, err = extract_journeys()
    if err:
        findings.append(('CRITICAL', 'links', err))
        return findings

    unresolvable = []
    for j in journeys:
        for i, wp in enumerate(j['waypoints']):
            if not wp['ref']:
                continue
            # Parse first book reference
            ref = wp['ref'].split(';')[0].strip()
            # Extract book name (everything before chapter:verse)
            book_match = re.match(r'^([\d\s]*[A-Za-z]+(?:\s+[A-Za-z]+)*)', ref)
            if book_match:
                book_name = book_match.group(1).strip().lower()
                # Check if it maps
                if book_name not in book_map:
                    # Try without space after number prefix
                    alt = book_name.replace('1 ', '1').replace('2 ', '2').replace('3 ', '3')
                    if alt not in book_map:
                        unresolvable.append((j['id'], i+1, wp['label'][:25], ref))

    if unresolvable:
        findings.append(('INFO', 'unresolvable_refs',
            f"{len(unresolvable)} waypoint refs cannot resolve to app text IDs"))
        for jid, wp_num, label, ref in unresolvable[:10]:  # Show first 10
            findings.append(('INFO', jid,
                f"  WP {wp_num} '{label}': ref '{ref}' not in BOOK_TO_TEXT"))

    # Check BOOK_TO_TEXT targets exist in manifest
    if valid_texts:
        for book, text_id in book_map.items():
            if text_id not in valid_texts:
                findings.append(('WARNING', 'book_map',
                    f"'{book}' -> '{text_id}' not found in manifest"))

    return findings


# ══════════════════════════════════════════════════════════
# 6. AUDIT WAYPOINT DESCRIPTIONS — Content quality check
# ══════════════════════════════════════════════════════════

def audit_waypoint_descriptions():
    """Check quality of waypoint descriptions."""
    findings = []
    journeys, err = extract_journeys()
    if err:
        findings.append(('CRITICAL', 'descriptions', err))
        return findings

    total_wps = 0
    with_desc = 0
    short_desc = 0

    for j in journeys:
        for i, wp in enumerate(j['waypoints']):
            total_wps += 1
            if wp['desc']:
                with_desc += 1
                if len(wp['desc']) < 30:
                    short_desc += 1
                    findings.append(('INFO', j['id'],
                        f"WP {i+1} '{wp['label'][:25]}' has very short description ({len(wp['desc'])} chars)"))

    coverage = (with_desc / total_wps * 100) if total_wps > 0 else 0
    findings.append(('INFO', 'description_coverage',
        f"{with_desc}/{total_wps} waypoints have descriptions ({coverage:.0f}%)"))

    if short_desc > 0:
        findings.append(('INFO', 'short_descriptions',
            f"{short_desc} waypoints have descriptions under 30 characters"))

    if coverage < 80:
        findings.append(('WARNING', 'description_coverage',
            f"Description coverage is {coverage:.0f}% (target: 80%+)"))

    return findings


# ══════════════════════════════════════════════════════════
# 7A. ERA FILE AUDIT — Depth, structure, theology
# ══════════════════════════════════════════════════════════

def load_module_safe(name, path):
    """Safely load a Python module from disk."""
    try:
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod, None
    except Exception as e:
        return None, str(e)


def audit_era_files():
    """Audit all era files for depth, structure, and theological quality."""
    findings = []

    # Load manifest
    if not os.path.exists(MANIFEST_PATH):
        findings.append(('CRITICAL', 'era_audit', 'manifest.json not found'))
        return findings

    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # Required chapter fields
    REQUIRED_FIELDS = ['id', 'ref', 'title', 'era', 'type']
    DEPTH_FIELDS = ['synopsis', 'sections', 'cross_refs', 'original_terms', 'key_verse']
    THEOLOGY_FIELDS = ['divine_council_note', 'ane_backdrop', 'second_temple']

    total_eras = 0
    total_chapters = 0
    thin_chapters = 0
    missing_divine_council = 0
    missing_ane = 0
    missing_second_temple = 0
    total_sections = 0
    total_xrefs = 0
    total_terms = 0
    empty_synopsis = 0
    missing_key_verse = 0

    for text_def in manifest.get('texts', []):
        text_id = text_def['id']
        data_dir = text_def.get('data_dir', text_id)
        text_path = os.path.join(DATA_DIR, data_dir)

        if not os.path.isdir(text_path):
            continue

        # Find era files
        era_files = [f for f in os.listdir(text_path) if f.startswith('era_') and f.endswith('.py')]
        total_eras += len(era_files)

        for era_file in era_files:
            era_path = os.path.join(text_path, era_file)
            mod_name = era_file[:-3]
            mod, err = load_module_safe(mod_name, era_path)

            if err:
                findings.append(('CRITICAL', f'{text_id}/{era_file}', f'Failed to load: {err}'))
                continue

            chapters = getattr(mod, 'CHAPTERS', None)
            if not chapters:
                findings.append(('WARNING', f'{text_id}/{era_file}', 'No CHAPTERS list found'))
                continue

            for ch in chapters:
                total_chapters += 1
                ch_id = ch.get('id', 'unknown')

                # Check required fields
                for field in REQUIRED_FIELDS:
                    if field not in ch or not ch[field]:
                        findings.append(('CRITICAL', ch_id, f"Missing required field: '{field}'"))

                # Check depth fields
                sections = ch.get('sections', [])
                xrefs = ch.get('cross_refs', [])
                terms = ch.get('original_terms', [])
                synopsis = ch.get('synopsis', '')
                key_verse = ch.get('key_verse', None)

                section_count = len(sections) if isinstance(sections, list) else 0
                xref_count = len(xrefs) if isinstance(xrefs, list) else 0
                term_count = len(terms) if isinstance(terms, list) else 0

                total_sections += section_count
                total_xrefs += xref_count
                total_terms += term_count

                # Thin chapter detection
                if section_count < 3 and xref_count < 3:
                    thin_chapters += 1
                    findings.append(('WARNING', ch_id,
                        f"Thin chapter: {section_count} sections, {xref_count} xrefs"))

                # Synopsis check
                if not synopsis or len(str(synopsis)) < 20:
                    empty_synopsis += 1

                # Key verse check
                if not key_verse:
                    missing_key_verse += 1

                # Theology field checks
                if not ch.get('divine_council_note'):
                    missing_divine_council += 1
                if not ch.get('ane_backdrop'):
                    missing_ane += 1
                if not ch.get('second_temple') or (isinstance(ch.get('second_temple'), list) and len(ch.get('second_temple')) == 0):
                    missing_second_temple += 1

                # Check section quality
                for si, sec in enumerate(sections if isinstance(sections, list) else []):
                    if isinstance(sec, dict):
                        if not sec.get('heading'):
                            findings.append(('INFO', ch_id, f"Section {si+1} missing heading"))
                        body = sec.get('body', '')
                        if isinstance(body, str) and len(body) < 50:
                            findings.append(('INFO', ch_id, f"Section '{sec.get('heading', si+1)}' has thin body ({len(body)} chars)"))

                # Check cross-ref quality
                for xref in (xrefs if isinstance(xrefs, list) else []):
                    if isinstance(xref, dict):
                        if not xref.get('ref'):
                            findings.append(('WARNING', ch_id, "Cross-ref missing 'ref' field"))
                        if not xref.get('note') or len(str(xref.get('note', ''))) < 10:
                            findings.append(('INFO', ch_id, f"Cross-ref '{xref.get('ref', '?')}' has thin/missing note"))
                        if not xref.get('type'):
                            findings.append(('INFO', ch_id, f"Cross-ref '{xref.get('ref', '?')}' missing type (ot/nt/ane/dss)"))

    # Summary stats
    dc_pct = ((total_chapters - missing_divine_council) / total_chapters * 100) if total_chapters else 0
    ane_pct = ((total_chapters - missing_ane) / total_chapters * 100) if total_chapters else 0
    st_pct = ((total_chapters - missing_second_temple) / total_chapters * 100) if total_chapters else 0

    findings.append(('INFO', 'era_summary',
        f"Scanned {total_eras} era files, {total_chapters} chapters"))
    findings.append(('INFO', 'era_depth',
        f"Totals: {total_sections} sections, {total_xrefs} xrefs, {total_terms} original_terms"))
    findings.append(('INFO', 'era_thin',
        f"{thin_chapters} thin chapters (< 3 sections AND < 3 xrefs)"))
    findings.append(('INFO', 'era_synopsis',
        f"{empty_synopsis} chapters missing/thin synopsis"))
    findings.append(('INFO', 'era_key_verse',
        f"{missing_key_verse} chapters missing key_verse"))
    findings.append(('INFO', 'era_theology',
        f"Divine council: {dc_pct:.0f}% | ANE backdrop: {ane_pct:.0f}% | Second Temple: {st_pct:.0f}%"))

    if thin_chapters > total_chapters * 0.3:
        findings.append(('WARNING', 'era_quality',
            f"{thin_chapters}/{total_chapters} chapters are thin ({thin_chapters/total_chapters*100:.0f}%) — target < 30%"))

    print(f"  Scanned {total_eras} era files, {total_chapters} chapters")
    print(f"  {total_sections} sections, {total_xrefs} xrefs, {total_terms} terms")
    print(f"  {thin_chapters} thin chapters, {missing_key_verse} missing key_verse")

    return findings


# ══════════════════════════════════════════════════════════
# 7B. FLOW FILE AUDIT — Coverage, gaps, format
# ══════════════════════════════════════════════════════════

def audit_flow_files():
    """Audit flow translation files for coverage and quality."""
    findings = []
    flow_dir = os.path.join(DATA_DIR, 'flow')

    if not os.path.isdir(flow_dir):
        findings.append(('CRITICAL', 'flow', 'data/flow/ directory not found'))
        return findings

    flow_files = [f for f in os.listdir(flow_dir) if f.startswith('flow_') and f.endswith('.py')]
    # Only count combined flow files (single underscore after 'flow')
    combined_flows = [f for f in flow_files if f.count('_') == 1]

    total_files = len(combined_flows)
    total_verses = 0
    total_notes = 0
    files_with_gaps = 0

    for flow_file in sorted(combined_flows):
        flow_path = os.path.join(flow_dir, flow_file)
        mod_name = flow_file[:-3]
        mod, err = load_module_safe(mod_name, flow_path)

        if err:
            findings.append(('CRITICAL', flow_file, f'Failed to load: {err}'))
            continue

        # Find the FLOW_* variable
        flow_var = None
        notes_var = None
        for attr_name in dir(mod):
            val = getattr(mod, attr_name)
            if attr_name.startswith('FLOW_') and isinstance(val, dict):
                flow_var = val
            if attr_name.startswith('NOTES_') and isinstance(val, dict):
                notes_var = val

        if not flow_var:
            findings.append(('WARNING', flow_file, 'No FLOW_* variable found'))
            continue

        # Count verses and check for gaps
        file_verses = 0
        file_gaps = 0
        for ch_num, verses in flow_var.items():
            if isinstance(verses, dict):
                verse_nums = sorted(verses.keys())
                file_verses += len(verse_nums)

                # Check for gaps in verse numbering
                if verse_nums:
                    expected = list(range(verse_nums[0], verse_nums[-1] + 1))
                    missing = set(expected) - set(verse_nums)
                    if missing:
                        file_gaps += len(missing)
                        if len(missing) <= 3:
                            findings.append(('WARNING', flow_file,
                                f"Ch {ch_num}: missing verses {sorted(missing)}"))
                        else:
                            findings.append(('WARNING', flow_file,
                                f"Ch {ch_num}: {len(missing)} missing verses"))

                # Check for empty verse text
                for v_num, text in verses.items():
                    if not text or len(str(text).strip()) < 5:
                        findings.append(('WARNING', flow_file,
                            f"Ch {ch_num}:{v_num} has empty/very short text"))

        total_verses += file_verses
        if file_gaps > 0:
            files_with_gaps += 1

        # Count notes
        if notes_var:
            for ch_num, notes in notes_var.items():
                if isinstance(notes, dict):
                    total_notes += len(notes)

    findings.append(('INFO', 'flow_summary',
        f"Scanned {total_files} combined flow files, {total_verses} total verses"))
    findings.append(('INFO', 'flow_notes',
        f"{total_notes} scholarly notes across all flow files"))

    if files_with_gaps > 0:
        findings.append(('WARNING', 'flow_gaps',
            f"{files_with_gaps} flow files have verse gaps"))

    print(f"  Scanned {total_files} flow files, {total_verses} verses, {total_notes} notes")

    return findings


# ══════════════════════════════════════════════════════════
# 7C. INTERLINEAR AUDIT — Hebrew/Greek word entries
# ══════════════════════════════════════════════════════════

def audit_interlinear():
    """Audit interlinear data files for completeness and format."""
    findings = []

    # Find all interlinear files
    il_files = []
    for f in os.listdir(DATA_DIR):
        if f.startswith('interlinear_') and f.endswith('.py'):
            il_files.append(os.path.join(DATA_DIR, f))

    # Also check subdirectories for interlinear.py
    for subdir in os.listdir(DATA_DIR):
        subpath = os.path.join(DATA_DIR, subdir)
        if os.path.isdir(subpath):
            il_path = os.path.join(subpath, 'interlinear.py')
            if os.path.exists(il_path):
                il_files.append(il_path)

    total_files = len(il_files)
    total_words = 0
    missing_strongs = 0
    missing_gloss = 0
    missing_morphology = 0
    empty_hebrew = 0

    for il_path in sorted(il_files):
        fname = os.path.basename(il_path)
        mod_name = fname[:-3]
        mod, err = load_module_safe(mod_name, il_path)

        if err:
            findings.append(('WARNING', fname, f'Failed to load: {err}'))
            continue

        # Find INTERLINEAR_* or INTERLINEAR variable
        il_data = None
        for attr_name in dir(mod):
            val = getattr(mod, attr_name)
            if attr_name.startswith('INTERLINEAR') and isinstance(val, dict):
                il_data = val
                break

        if not il_data:
            findings.append(('WARNING', fname, 'No INTERLINEAR variable found'))
            continue

        file_words = 0
        file_missing_s = 0
        file_missing_g = 0
        file_missing_m = 0
        file_empty_h = 0

        for ch_num, ch_data in il_data.items():
            verses = ch_data.get('verses', []) if isinstance(ch_data, dict) else []
            for verse in verses:
                words = verse.get('words', []) if isinstance(verse, dict) else []
                for word in words:
                    if not isinstance(word, dict):
                        continue
                    file_words += 1

                    if not word.get('h'):
                        file_empty_h += 1
                    if not word.get('s'):
                        file_missing_s += 1
                    if not word.get('g'):
                        file_missing_g += 1
                    if not word.get('m'):
                        file_missing_m += 1

        total_words += file_words
        missing_strongs += file_missing_s
        missing_gloss += file_missing_g
        missing_morphology += file_missing_m
        empty_hebrew += file_empty_h

        # Report per-file issues
        if file_words > 0 and file_missing_s > file_words * 0.05:
            findings.append(('WARNING', fname,
                f"{file_missing_s}/{file_words} words missing Strong's numbers ({file_missing_s/file_words*100:.0f}%)"))
        if file_words > 0 and file_missing_m > file_words * 0.1:
            findings.append(('INFO', fname,
                f"{file_missing_m}/{file_words} words missing morphology ({file_missing_m/file_words*100:.0f}%)"))

    # Summary
    s_pct = ((total_words - missing_strongs) / total_words * 100) if total_words else 0
    g_pct = ((total_words - missing_gloss) / total_words * 100) if total_words else 0
    m_pct = ((total_words - missing_morphology) / total_words * 100) if total_words else 0

    findings.append(('INFO', 'interlinear_summary',
        f"Scanned {total_files} interlinear files, {total_words:,} total words"))
    findings.append(('INFO', 'interlinear_quality',
        f"Strong's: {s_pct:.0f}% | Gloss: {g_pct:.0f}% | Morphology: {m_pct:.0f}%"))

    if empty_hebrew > 0:
        findings.append(('WARNING', 'interlinear_empty',
            f"{empty_hebrew} words with empty Hebrew/Greek text"))

    print(f"  Scanned {total_files} files, {total_words:,} words")
    print(f"  Strong's: {s_pct:.0f}% | Gloss: {g_pct:.0f}% | Morphology: {m_pct:.0f}%")

    return findings


# ══════════════════════════════════════════════════════════
# 7D. GLOSSARY AUDIT — Entry quality and coverage
# ══════════════════════════════════════════════════════════

def audit_glossary():
    """Audit glossary entries for depth and quality."""
    findings = []

    glossary_path = os.path.join(DATA_DIR, 'glossary.py')
    if not os.path.exists(glossary_path):
        findings.append(('CRITICAL', 'glossary', 'data/glossary.py not found'))
        return findings

    mod, err = load_module_safe('glossary', glossary_path)
    if err:
        findings.append(('CRITICAL', 'glossary', f'Failed to load: {err}'))
        return findings

    glossary = getattr(mod, 'GLOSSARY', {})
    if not glossary:
        findings.append(('CRITICAL', 'glossary', 'GLOSSARY dict is empty'))
        return findings

    total_entries = len(glossary)
    missing_hebrew = 0
    missing_transliteration = 0
    missing_strongs = 0
    missing_definition = 0
    short_definition = 0
    missing_chapters = 0
    orphan_entries = 0  # entries not used in any chapter

    for key, entry in glossary.items():
        if not isinstance(entry, dict):
            findings.append(('WARNING', f'glossary:{key}', 'Entry is not a dict'))
            continue

        if not entry.get('hebrew'):
            missing_hebrew += 1
        if not entry.get('transliteration'):
            missing_transliteration += 1
        if not entry.get('strongs'):
            missing_strongs += 1

        defn = entry.get('definition', '')
        if not defn:
            missing_definition += 1
            findings.append(('WARNING', f'glossary:{key}', 'Missing definition'))
        elif len(str(defn)) < 30:
            short_definition += 1

        gloss = entry.get('gloss', '')
        if not gloss:
            findings.append(('INFO', f'glossary:{key}', 'Missing gloss (short meaning)'))

        chapters = entry.get('chapters_used', [])
        if not chapters or len(chapters) == 0:
            missing_chapters += 1
            orphan_entries += 1

    # Summary
    findings.append(('INFO', 'glossary_summary',
        f"{total_entries} glossary entries"))
    findings.append(('INFO', 'glossary_quality',
        f"Missing: {missing_hebrew} hebrew, {missing_transliteration} transliteration, "
        f"{missing_strongs} Strong's, {missing_definition} definitions"))
    findings.append(('INFO', 'glossary_depth',
        f"{short_definition} entries with short definitions (< 30 chars)"))

    if orphan_entries > 0:
        findings.append(('INFO', 'glossary_orphans',
            f"{orphan_entries} entries not linked to any chapters (missing chapters_used)"))

    if missing_definition > total_entries * 0.05:
        findings.append(('WARNING', 'glossary_coverage',
            f"{missing_definition}/{total_entries} entries missing definitions ({missing_definition/total_entries*100:.0f}%)"))

    print(f"  {total_entries} entries, {missing_definition} missing definitions")
    print(f"  {short_definition} short definitions, {orphan_entries} orphan entries")

    return findings


# ══════════════════════════════════════════════════════════
# 7E. CROSS-REFERENCE QUALITY AUDIT
# ══════════════════════════════════════════════════════════

def audit_cross_references():
    """Audit cross-reference quality across all era files."""
    findings = []

    if not os.path.exists(MANIFEST_PATH):
        findings.append(('CRITICAL', 'xref_audit', 'manifest.json not found'))
        return findings

    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    total_xrefs = 0
    xrefs_with_note = 0
    xrefs_with_type = 0
    type_counts = {'ot': 0, 'nt': 0, 'ane': 0, 'dss': 0, 'other': 0}
    thin_notes = 0
    missing_ref = 0

    for text_def in manifest.get('texts', []):
        text_id = text_def['id']
        data_dir = text_def.get('data_dir', text_id)
        text_path = os.path.join(DATA_DIR, data_dir)

        if not os.path.isdir(text_path):
            continue

        for era_file in os.listdir(text_path):
            if not (era_file.startswith('era_') and era_file.endswith('.py')):
                continue

            era_path = os.path.join(text_path, era_file)
            mod, err = load_module_safe(era_file[:-3], era_path)
            if err:
                continue

            chapters = getattr(mod, 'CHAPTERS', [])
            for ch in chapters:
                xrefs = ch.get('cross_refs', [])
                if not isinstance(xrefs, list):
                    continue

                for xref in xrefs:
                    if not isinstance(xref, dict):
                        continue
                    total_xrefs += 1

                    ref = xref.get('ref', '')
                    note = xref.get('note', '')
                    xtype = xref.get('type', '')

                    if not ref:
                        missing_ref += 1

                    if note and len(str(note)) > 5:
                        xrefs_with_note += 1
                    if note and len(str(note)) < 15:
                        thin_notes += 1

                    if xtype:
                        xrefs_with_type += 1
                        type_counts[xtype] = type_counts.get(xtype, 0) + 1
                    else:
                        type_counts['other'] += 1

    # Summary
    note_pct = (xrefs_with_note / total_xrefs * 100) if total_xrefs else 0
    type_pct = (xrefs_with_type / total_xrefs * 100) if total_xrefs else 0

    findings.append(('INFO', 'xref_summary',
        f"{total_xrefs:,} total cross-references across all era files"))
    findings.append(('INFO', 'xref_types',
        f"OT: {type_counts['ot']} | NT: {type_counts['nt']} | ANE: {type_counts.get('ane', 0)} | DSS: {type_counts.get('dss', 0)}"))
    findings.append(('INFO', 'xref_quality',
        f"Notes: {note_pct:.0f}% with explanations | Types: {type_pct:.0f}% categorized"))

    if thin_notes > total_xrefs * 0.1:
        findings.append(('WARNING', 'xref_thin',
            f"{thin_notes} cross-refs have thin notes (< 15 chars)"))

    if missing_ref > 0:
        findings.append(('WARNING', 'xref_missing_ref',
            f"{missing_ref} cross-refs missing the 'ref' field"))

    print(f"  {total_xrefs:,} xrefs: OT={type_counts['ot']}, NT={type_counts['nt']}, ANE={type_counts.get('ane',0)}, DSS={type_counts.get('dss',0)}")

    return findings


# ══════════════════════════════════════════════════════════
# 7F. CODE STRUCTURE AUDIT — CSS, JS, build patterns
# ══════════════════════════════════════════════════════════

def audit_code_structure():
    """Audit code structure, CSS design system, and build integrity."""
    findings = []

    # Check app.js exists and get metrics
    if os.path.exists(APP_JS):
        with open(APP_JS, 'r', encoding='utf-8') as f:
            js_content = f.read()
        js_lines = js_content.count('\n') + 1
        js_functions = len(re.findall(r'function\s+\w+\s*\(', js_content))

        findings.append(('INFO', 'js_structure',
            f"app.js: {js_lines:,} lines, {js_functions} named functions"))

        if js_lines > 10000:
            findings.append(('WARNING', 'js_size',
                f"app.js is {js_lines:,} lines — consider module split (Phase 2)"))

        # Check for console.log left in production code
        console_logs = len(re.findall(r'console\.log\(', js_content))
        if console_logs > 5:
            findings.append(('INFO', 'js_debug',
                f"{console_logs} console.log() calls found — review for production"))

        # Check for TODO/FIXME/HACK comments
        todos = len(re.findall(r'//\s*(TODO|FIXME|HACK|XXX)', js_content, re.IGNORECASE))
        if todos > 0:
            findings.append(('INFO', 'js_todos', f"{todos} TODO/FIXME/HACK comments in app.js"))
    else:
        findings.append(('CRITICAL', 'js_missing', 'app.js not found'))

    # Check CSS build order
    css_dir = os.path.join(PROJECT_ROOT, 'src', 'css')
    build_order_path = os.path.join(css_dir, 'build-order.txt')

    if os.path.exists(build_order_path):
        with open(build_order_path, 'r') as f:
            ordered_files = [line.strip() for line in f if line.strip() and not line.startswith('#')]

        # Check all listed files exist
        missing_css = []
        for css_file in ordered_files:
            if not os.path.exists(os.path.join(css_dir, css_file)):
                missing_css.append(css_file)

        if missing_css:
            findings.append(('CRITICAL', 'css_missing',
                f"CSS files in build-order.txt but missing on disk: {missing_css}"))

        # Check for CSS files on disk not in build order
        actual_css = [f for f in os.listdir(css_dir) if f.endswith('.css')]
        unlisted = [f for f in actual_css if f not in ordered_files]
        if unlisted:
            findings.append(('WARNING', 'css_unlisted',
                f"CSS files on disk but NOT in build-order.txt: {unlisted}"))

        findings.append(('INFO', 'css_structure',
            f"{len(ordered_files)} CSS files in build order, {len(actual_css)} on disk"))
    else:
        findings.append(('WARNING', 'css_build_order', 'build-order.txt not found'))

    # Check design tokens exist
    tokens_path = os.path.join(css_dir, '_tokens.css')
    if os.path.exists(tokens_path):
        with open(tokens_path, 'r', encoding='utf-8') as f:
            tokens_content = f.read()
        token_vars = len(re.findall(r'--[\w-]+\s*:', tokens_content))
        findings.append(('INFO', 'css_tokens', f"{token_vars} CSS custom properties in _tokens.css"))
    else:
        findings.append(('WARNING', 'css_tokens', '_tokens.css not found — no design token system'))

    # Check state.js exists
    state_js = os.path.join(PROJECT_ROOT, 'src', 'js', 'state.js')
    if os.path.exists(state_js):
        with open(state_js, 'r', encoding='utf-8') as f:
            state_lines = f.read().count('\n') + 1
        findings.append(('INFO', 'state_module', f"state.js: {state_lines} lines"))
    else:
        findings.append(('INFO', 'state_module', 'state.js not found — state in app.js'))

    # Check manifest.json integrity
    if os.path.exists(MANIFEST_PATH):
        with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
        text_count = len(manifest.get('texts', []))
        era_count = len(manifest.get('eras', []))
        findings.append(('INFO', 'manifest', f"manifest.json: {text_count} texts, {era_count} eras"))

        # Check for texts without eras
        text_ids_with_eras = set()
        for era in manifest.get('eras', []):
            # Era text field might be a display name, need to check
            era_text = era.get('text', '')
            text_ids_with_eras.add(era_text)

    else:
        findings.append(('CRITICAL', 'manifest', 'manifest.json not found'))

    # Check build output exists
    output_dir = os.path.join(PROJECT_ROOT, 'output')
    dev_build = os.path.join(output_dir, 'AncientTextsStudy.html')
    release_build = os.path.join(output_dir, 'AncientTextsStudy-Release.html')
    mobile_dir = os.path.join(output_dir, 'mobile')

    if os.path.exists(dev_build):
        size_mb = os.path.getsize(dev_build) / (1024 * 1024)
        findings.append(('INFO', 'build_dev', f"Dev build: {size_mb:.1f} MB"))
    else:
        findings.append(('WARNING', 'build_dev', 'Dev build not found (output/AncientTextsStudy.html)'))

    if os.path.exists(release_build):
        size_mb = os.path.getsize(release_build) / (1024 * 1024)
        findings.append(('INFO', 'build_release', f"Release build: {size_mb:.1f} MB"))

    if os.path.isdir(mobile_dir):
        mobile_files = sum(1 for _ in os.listdir(mobile_dir))
        findings.append(('INFO', 'build_mobile', f"Mobile PWA: {mobile_files} files"))

    print(f"  Code structure audit complete")

    return findings


# ══════════════════════════════════════════════════════════
# 8. AI THEOLOGICAL REVIEW — Deep review via Arbiter API
# ══════════════════════════════════════════════════════════

def run_ai_theological_review():
    """Use Arbiter AI to review theological accuracy of waypoint descriptions."""
    try:
        import anthropic
    except ImportError:
        return [('CRITICAL', 'ai_review', 'anthropic package not installed')]

    findings = []
    journeys, err = extract_journeys()
    if err:
        findings.append(('CRITICAL', 'ai_review', err))
        return findings

    # Collect all descriptions for review
    descriptions = []
    for j in journeys:
        for wp in j['waypoints']:
            if wp['desc'] and len(wp['desc']) > 20:
                descriptions.append({
                    'journey': j['name'],
                    'location': wp['label'],
                    'ref': wp['ref'],
                    'desc': wp['desc']
                })

    if not descriptions:
        findings.append(('INFO', 'ai_review', 'No descriptions to review'))
        return findings

    # Batch into chunks of 15
    BATCH_SIZE = 15
    client = anthropic.Anthropic(api_key=ARBITER_API_KEY)

    for batch_start in range(0, len(descriptions), BATCH_SIZE):
        batch = descriptions[batch_start:batch_start + BATCH_SIZE]
        batch_text = "\n\n".join(
            f"[{d['journey']} > {d['location']}] (Ref: {d['ref']})\n{d['desc']}"
            for d in batch
        )

        prompt = f"""Review these biblical map waypoint descriptions for theological accuracy.

THEOLOGICAL STANDARDS:
{THEOLOGICAL_GUIDELINES}

DESCRIPTIONS TO REVIEW:
{batch_text}

For each description, check:
1. Scripture references match the claimed content
2. No Sethite view contamination (Gen 6 sons of God must be divine/angelic beings)
3. Non-canonical sources properly attributed (e.g., "According to 1 Enoch" not "the Bible says")
4. Evidence tiers respected: [A] Direct Scripture, [B] Valid inference, [C] Ancient parallels
5. Historical/archaeological claims are defensible
6. Divine council theology preserved where relevant

Return ONLY issues found, in this format:
ISSUE: [journey > location] -- description of the problem
SEVERITY: CRITICAL/WARNING/INFO

If no issues found, say "ALL CLEAR" for the batch."""

        try:
            response = client.messages.create(
                model=ARBITER_MODEL,
                max_tokens=2000,
                temperature=ARBITER_TEMPERATURE,
                messages=[{"role": "user", "content": prompt}]
            )

            result = response.content[0].text
            if "ALL CLEAR" not in result:
                # Parse issues
                for line in result.split('\n'):
                    if line.startswith('ISSUE:'):
                        findings.append(('WARNING', 'theological', line))
                    elif line.startswith('SEVERITY: CRITICAL'):
                        # Upgrade last finding
                        if findings and findings[-1][0] == 'WARNING':
                            findings[-1] = ('CRITICAL', findings[-1][1], findings[-1][2])

            batch_num = batch_start // BATCH_SIZE + 1
            total_batches = (len(descriptions) + BATCH_SIZE - 1) // BATCH_SIZE
            print(f"  Reviewed batch {batch_num}/{total_batches}")

        except Exception as e:
            batch_num = batch_start // BATCH_SIZE + 1
            findings.append(('WARNING', 'ai_review',
                f"API error on batch {batch_num}: {e}"))

    return findings


# ══════════════════════════════════════════════════════════
# 9. REPORT GENERATION — Markdown audit report
# ══════════════════════════════════════════════════════════

def generate_report(all_findings, output_path=None):
    """Generate markdown audit report."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')

    critical = [f for f in all_findings if f[0] == 'CRITICAL']
    warnings = [f for f in all_findings if f[0] == 'WARNING']
    info = [f for f in all_findings if f[0] == 'INFO']

    # Determine grade
    if critical:
        grade = "FAIL"
    elif warnings:
        grade = "NEEDS ATTENTION"
    else:
        grade = "PASS"

    report = f"""# Claude Code Work Audit Report
Generated: {timestamp}

## Summary
- **CRITICAL**: {len(critical)}
- **WARNING**: {len(warnings)}
- **INFO**: {len(info)}
- **Total findings**: {len(all_findings)}

## Grade: {grade}

"""

    if critical:
        report += "## Critical Issues\n\n"
        for level, source, msg in critical:
            report += f"- **[{source}]** {msg}\n"
        report += "\n"

    if warnings:
        report += "## Warnings\n\n"
        for level, source, msg in warnings:
            report += f"- **[{source}]** {msg}\n"
        report += "\n"

    if info:
        report += "## Info\n\n"
        for level, source, msg in info:
            report += f"- **[{source}]** {msg}\n"
        report += "\n"

    if not output_path:
        output_path = os.path.join(REPORTS_DIR,
            f"claude_audit_{datetime.now().strftime('%Y%m%d_%H%M')}.md")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    return output_path


# ══════════════════════════════════════════════════════════
# 10. MAIN — CLI entry point
# ══════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description='Audit Claude Code work on Ancient Texts Study App')

    # Map-related audits (run by --all)
    parser.add_argument('--map', action='store_true',
        help='Audit MAP_JOURNEYS structure')
    parser.add_argument('--colors', action='store_true',
        help='Audit color uniqueness/visibility')
    parser.add_argument('--coords', action='store_true',
        help='Validate geographic coordinates')
    parser.add_argument('--links', action='store_true',
        help='Validate "Read in App" links')
    parser.add_argument('--waypoints', action='store_true',
        help='Audit waypoint descriptions')

    # App-wide content audits (run by --full-app)
    parser.add_argument('--eras', action='store_true',
        help='Audit era file depth and quality')
    parser.add_argument('--flow', action='store_true',
        help='Audit flow translation files')
    parser.add_argument('--interlinear', action='store_true',
        help='Audit interlinear data')
    parser.add_argument('--glossary', action='store_true',
        help='Audit glossary entries')
    parser.add_argument('--xrefs', action='store_true',
        help='Audit cross-reference quality')
    parser.add_argument('--code', action='store_true',
        help='Audit code structure and CSS')

    # Meta flags
    parser.add_argument('--ai-review', action='store_true',
        help='AI theological review (uses API)')
    parser.add_argument('--all', action='store_true',
        help='Run all map-related audits (default)')
    parser.add_argument('--full-app', action='store_true',
        help='Full app audit (everything)')
    parser.add_argument('--report', type=str,
        help='Output report path')
    args = parser.parse_args()

    # No flags = default to --all (map audits)
    if not any([args.map, args.colors, args.coords, args.links, args.waypoints,
                args.eras, args.flow, args.interlinear, args.glossary, args.xrefs,
                args.code, args.ai_review, args.all, args.full_app]):
        args.all = True

    # Banner
    print(f"\n{'='*60}")
    if args.full_app:
        print(f"  FULL APP SENTIENT AUDIT")
    else:
        print(f"  CLAUDE CODE WORK AUDIT")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")

    all_findings = []

    # ── Map-related audits (--all or --full-app or individual flags) ──

    if args.all or args.full_app or args.map:
        print("\n[audit] Auditing MAP_JOURNEYS structure...")
        all_findings.extend(audit_map_journeys())

    if args.all or args.full_app or args.colors:
        print("\n[audit] Auditing journey colors...")
        all_findings.extend(audit_colors())

    if args.all or args.full_app or args.coords:
        print("\n[audit] Validating geographic coordinates...")
        all_findings.extend(audit_coordinates())

    if args.all or args.full_app or args.links:
        print("\n[audit] Validating 'Read in App' links...")
        all_findings.extend(audit_read_links())

    if args.all or args.full_app or args.waypoints:
        print("\n[audit] Auditing waypoint descriptions...")
        all_findings.extend(audit_waypoint_descriptions())

    # ── App-wide content audits (--full-app or individual flags) ──

    if args.full_app or args.eras:
        print("\n[audit] Auditing era file depth and quality...")
        all_findings.extend(audit_era_files())

    if args.full_app or args.flow:
        print("\n[audit] Auditing flow translation files...")
        all_findings.extend(audit_flow_files())

    if args.full_app or args.interlinear:
        print("\n[audit] Auditing interlinear data...")
        all_findings.extend(audit_interlinear())

    if args.full_app or args.glossary:
        print("\n[audit] Auditing glossary entries...")
        all_findings.extend(audit_glossary())

    if args.full_app or args.xrefs:
        print("\n[audit] Auditing cross-reference quality...")
        all_findings.extend(audit_cross_references())

    if args.full_app or args.code:
        print("\n[audit] Auditing code structure...")
        all_findings.extend(audit_code_structure())

    # ── AI review (explicit opt-in only) ──

    if args.ai_review:
        print("\n[audit] Running AI theological review...")
        all_findings.extend(run_ai_theological_review())

    # Print summary
    critical = sum(1 for f in all_findings if f[0] == 'CRITICAL')
    warnings = sum(1 for f in all_findings if f[0] == 'WARNING')
    info = sum(1 for f in all_findings if f[0] == 'INFO')

    print(f"\n{'='*60}")
    print(f"AUDIT COMPLETE: {critical} critical, {warnings} warnings, {info} info")

    if critical:
        print("  CRITICAL issues found -- must fix before deploy")
    elif warnings:
        print("  Warnings found -- review recommended")
    else:
        print("  All checks passed")
    print(f"{'='*60}")

    # Generate report
    report_path = generate_report(all_findings, args.report)
    print(f"\nReport saved to: {report_path}")

    # Return exit code based on findings
    sys.exit(1 if critical else 0)


if __name__ == '__main__':
    main()

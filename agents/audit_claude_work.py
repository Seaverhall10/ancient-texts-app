"""
audit_claude_work.py — Audit all Claude Code output

Validates map journeys, waypoint data, era files, BOOK_TO_TEXT mapping,
color assignments, geographic coordinates, and theological accuracy.

Usage:
    python agents/audit_claude_work.py --map          # Audit MAP_JOURNEYS
    python agents/audit_claude_work.py --waypoints    # Audit all waypoint data
    python agents/audit_claude_work.py --colors       # Audit color uniqueness/visibility
    python agents/audit_claude_work.py --coords       # Validate geographic coordinates
    python agents/audit_claude_work.py --links        # Validate "Read in App" links
    python agents/audit_claude_work.py --all          # Full audit
    python agents/audit_claude_work.py --ai-review    # AI theological review of descriptions
"""
import re
import sys
import os
import json
import math
import argparse
from datetime import datetime

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
# 7. AI THEOLOGICAL REVIEW — Deep review via Arbiter API
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
# 8. REPORT GENERATION — Markdown audit report
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
# 9. MAIN — CLI entry point
# ══════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description='Audit Claude Code work on Ancient Texts Study App')
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
    parser.add_argument('--ai-review', action='store_true',
        help='AI theological review (uses API)')
    parser.add_argument('--all', action='store_true',
        help='Run all local audits')
    parser.add_argument('--report', type=str,
        help='Output report path')
    args = parser.parse_args()

    if not any([args.map, args.colors, args.coords, args.links,
                args.waypoints, args.ai_review, args.all]):
        args.all = True

    print(f"\n{'='*60}")
    print(f"  CLAUDE CODE WORK AUDIT")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")

    all_findings = []

    if args.all or args.map:
        print("\n[audit] Auditing MAP_JOURNEYS structure...")
        all_findings.extend(audit_map_journeys())

    if args.all or args.colors:
        print("\n[audit] Auditing journey colors...")
        all_findings.extend(audit_colors())

    if args.all or args.coords:
        print("\n[audit] Validating geographic coordinates...")
        all_findings.extend(audit_coordinates())

    if args.all or args.links:
        print("\n[audit] Validating 'Read in App' links...")
        all_findings.extend(audit_read_links())

    if args.all or args.waypoints:
        print("\n[audit] Auditing waypoint descriptions...")
        all_findings.extend(audit_waypoint_descriptions())

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

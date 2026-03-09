"""
Validate a flow translation file against the interlinear data.
Checks: every verse present, no extras, no syntax errors, notes valid.

Usage: python validate_flow.py flow_ruth.py
"""
import sys, os, importlib.util

# Exact verse counts from our interlinear data (OSHB Masoretic Text)
VERSE_COUNTS = {
    "JUDGES": {1:36,2:23,3:31,4:24,5:31,6:40,7:25,8:35,9:57,10:18,11:40,12:15,13:25,14:20,15:20,16:31,17:13,18:31,19:30,20:48,21:25},
    "RUTH": {1:22,2:23,3:18,4:22},
    "1SAMUEL": {1:28,2:36,3:21,4:22,5:12,6:21,7:17,8:22,9:27,10:27,11:15,12:25,13:23,14:52,15:35,16:23,17:58,18:30,19:24,20:42,21:16,22:23,23:28,24:23,25:44,26:25,27:12,28:25,29:11,30:31,31:13},
    "2SAMUEL": {1:27,2:32,3:39,4:12,5:25,6:23,7:29,8:18,9:13,10:19,11:27,12:31,13:39,14:33,15:37,16:23,17:29,18:32,19:44,20:26,21:22,22:51,23:39,24:25},
    "1KINGS": {1:53,2:46,3:28,4:20,5:32,6:38,7:51,8:66,9:28,10:29,11:43,12:33,13:34,14:31,15:34,16:34,17:24,18:46,19:21,20:43,21:29,22:54},
    "2KINGS": {1:18,2:25,3:27,4:44,5:27,6:33,7:20,8:29,9:37,10:36,11:20,12:22,13:25,14:29,15:38,16:20,17:41,18:37,19:37,20:21,21:26,22:20,23:37,24:20,25:30},
    "PSALMS": {1:6,2:12,3:9,4:9,5:13,6:11,7:18,8:10,9:21,10:18,11:7,12:9,13:6,14:7,15:5,16:11,17:15,18:51,19:15,20:10,21:14,22:32,23:6,24:10,25:22,26:12,27:14,28:9,29:11,30:13,31:25,32:11,33:22,34:23,35:28,36:13,37:40,38:23,39:14,40:18,41:14,42:12,43:5,44:27,45:18,46:12,47:10,48:15,49:21,50:23,51:21,52:11,53:7,54:9,55:24,56:14,57:12,58:12,59:18,60:14,61:9,62:13,63:12,64:11,65:14,66:20,67:8,68:36,69:37,70:6,71:24,72:20,73:28,74:23,75:11,76:13,77:21,78:72,79:13,80:20,81:17,82:8,83:19,84:13,85:14,86:17,87:7,88:19,89:53,90:17,91:16,92:16,93:5,94:23,95:11,96:13,97:12,98:9,99:9,100:5,101:8,102:29,103:22,104:35,105:45,106:48,107:43,108:14,109:31,110:7,111:10,112:10,113:9,114:8,115:18,116:19,117:2,118:29,119:176,120:7,121:8,122:9,123:4,124:8,125:5,126:6,127:5,128:6,129:8,130:8,131:3,132:18,133:3,134:3,135:21,136:26,137:9,138:8,139:24,140:14,141:10,142:8,143:12,144:15,145:21,146:10,147:20,148:14,149:9,150:6},
    "ISAIAH": {1:31,2:22,3:26,4:6,5:30,6:13,7:25,8:23,9:20,10:34,11:16,12:6,13:22,14:32,15:9,16:14,17:14,18:7,19:25,20:6,21:17,22:25,23:18,24:23,25:12,26:21,27:13,28:29,29:24,30:33,31:9,32:20,33:24,34:17,35:10,36:22,37:38,38:22,39:8,40:31,41:29,42:25,43:28,44:28,45:25,46:13,47:15,48:22,49:26,50:11,51:23,52:15,53:12,54:17,55:13,56:12,57:21,58:14,59:21,60:22,61:11,62:12,63:19,64:11,65:25,66:24},
    "DANIEL": {1:21,2:49,3:33,4:34,5:30,6:29,7:28,8:27,9:27,10:21,11:45,12:13},
    # Already complete books (for reference)
    "GENESIS": {1:31,2:25,3:24,4:26,5:32,6:22,7:24,8:22,9:29,10:32,11:32,12:20,13:18,14:24,15:21,16:16,17:27,18:33,19:38,20:18,21:34,22:24,23:20,24:67,25:34,26:35,27:46,28:22,29:35,30:43,31:55,32:33,33:20,34:31,35:29,36:43,37:36,38:30,39:23,40:23,41:57,42:38,43:34,44:34,45:28,46:34,47:31,48:22,49:33,50:26},
    "EXODUS": {1:22,2:25,3:22,4:31,5:23,6:30,7:25,8:28,9:35,10:29,11:10,12:51,13:22,14:31,15:27,16:36,17:16,18:27,19:25,20:23,21:36,22:30,23:33,24:18,25:40,26:37,27:21,28:43,29:46,30:38,31:18,32:35,33:23,34:35,35:35,36:38,37:29,38:31,39:43,40:38},
    "JOSHUA": {1:18,2:24,3:17,4:24,5:15,6:27,7:26,8:35,9:27,10:43,11:23,12:24,13:33,14:15,15:63,16:10,17:18,18:28,19:51,20:9,21:45,22:34,23:16,24:33},
}


def validate(flow_file):
    """Validate a flow translation file."""
    basename = os.path.basename(flow_file).replace(".py", "")
    # Extract book name: flow_ruth -> RUTH, flow_1samuel -> 1SAMUEL
    book_key = basename.replace("flow_", "").upper()

    if book_key not in VERSE_COUNTS:
        print(f"WARNING: No verse count data for '{book_key}'. Skipping verse validation.")
        expected = None
    else:
        expected = VERSE_COUNTS[book_key]

    # Try to import the file
    print(f"\n=== Validating {flow_file} ===\n")

    try:
        spec = importlib.util.spec_from_file_location(basename, flow_file)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("[OK] File parses as valid Python")
    except SyntaxError as e:
        print(f"[FAIL] SYNTAX ERROR: {e}")
        return False
    except Exception as e:
        print(f"[FAIL] Import error: {e}")
        return False

    # Find FLOW_ and NOTES_ dicts
    flow_var = notes_var = None
    flow_dict = notes_dict = None
    for attr in dir(mod):
        if attr.startswith("FLOW_") and flow_var is None:
            flow_var = attr
            flow_dict = getattr(mod, attr)
        if attr.startswith("NOTES_") and notes_var is None:
            notes_var = attr
            notes_dict = getattr(mod, attr)

    if flow_dict is None:
        print("[FAIL] No FLOW_ dictionary found")
        return False
    print(f"[OK] Found {flow_var}: {len(flow_dict)} chapters")

    if notes_dict is None:
        print("[WARN] No NOTES_ dictionary found")
        notes_dict = {}
    else:
        total_notes = sum(len(v) for v in notes_dict.values() if isinstance(v, dict))
        print(f"[OK] Found {notes_var}: {total_notes} notes")

    errors = []
    warnings = []

    if expected:
        # Check chapter count
        expected_chs = sorted(expected.keys())
        actual_chs = sorted(flow_dict.keys())
        if actual_chs != expected_chs:
            missing = set(expected_chs) - set(actual_chs)
            extra = set(actual_chs) - set(expected_chs)
            if missing:
                errors.append(f"MISSING chapters: {sorted(missing)}")
            if extra:
                warnings.append(f"EXTRA chapters: {sorted(extra)}")

        # Check verse counts per chapter
        total_expected = 0
        total_actual = 0
        for ch in sorted(expected.keys()):
            exp_v = expected[ch]
            total_expected += exp_v
            if ch not in flow_dict:
                errors.append(f"Chapter {ch}: MISSING entirely ({exp_v} verses expected)")
                continue
            actual_verses = flow_dict[ch]
            if not isinstance(actual_verses, dict):
                errors.append(f"Chapter {ch}: value is not a dict")
                continue
            act_v = len(actual_verses)
            total_actual += act_v
            if act_v != exp_v:
                missing_v = set(range(1, exp_v + 1)) - set(actual_verses.keys())
                extra_v = set(actual_verses.keys()) - set(range(1, exp_v + 1))
                if missing_v:
                    errors.append(f"Chapter {ch}: MISSING verses {sorted(missing_v)} (have {act_v}/{exp_v})")
                if extra_v:
                    warnings.append(f"Chapter {ch}: extra verses {sorted(extra_v)}")

        print(f"\n[VERSES] {total_actual}/{total_expected} verses present")

    # Check for empty strings
    empty_count = 0
    for ch in sorted(flow_dict.keys()):
        if isinstance(flow_dict[ch], dict):
            for v, text in flow_dict[ch].items():
                if not text or not text.strip():
                    empty_count += 1
                    errors.append(f"Chapter {ch}:{v} — EMPTY translation")
    if empty_count == 0:
        print("[OK] No empty translations")

    # Check notes reference valid verses
    if notes_dict and expected:
        for ch in notes_dict:
            if isinstance(notes_dict[ch], dict):
                for v in notes_dict[ch]:
                    if isinstance(v, int) and ch in expected:
                        if v > expected[ch] or v < 1:
                            warnings.append(f"Note {ch}:{v} references invalid verse number")

    # Report
    if errors:
        print(f"\n[ERRORS] {len(errors)} errors found:")
        for e in errors:
            print(f"  - {e}")
    else:
        print("\n[OK] No errors found")

    if warnings:
        print(f"\n[WARNINGS] {len(warnings)} warnings:")
        for w in warnings:
            print(f"  - {w}")

    return len(errors) == 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_flow.py <flow_file.py>")
        print("       python validate_flow.py --all")
        sys.exit(1)

    if sys.argv[1] == "--all":
        flow_dir = os.path.join(os.path.dirname(__file__), "..", "data", "flow")
        import glob
        ok = 0
        fail = 0
        for f in sorted(glob.glob(os.path.join(flow_dir, "flow_*.py"))):
            # Only check combined files (single underscore)
            basename = os.path.basename(f).replace("flow_", "").replace(".py", "")
            if "_" not in basename:
                if validate(f):
                    ok += 1
                else:
                    fail += 1
        print(f"\n{'='*40}")
        print(f"TOTAL: {ok} passed, {fail} failed")
    else:
        ok = validate(sys.argv[1])
        sys.exit(0 if ok else 1)

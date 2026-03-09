"""Fix smart quotes in manifest.json and reconcile era data_file entries."""
import json
import os
import glob

MANIFEST = "manifest.json"

# Read raw text
with open(MANIFEST, "r", encoding="utf-8") as f:
    text = f.read()

# Replace smart quotes with standard ASCII quotes
text = text.replace("\u201c", '"')  # left double
text = text.replace("\u201d", '"')  # right double
text = text.replace("\u2018", "'")  # left single
text = text.replace("\u2019", "'")  # right single

# Parse
data = json.loads(text)
print(f"Parsed: {len(data['texts'])} texts, {len(data['eras'])} eras")

# Build a map: text_id -> list of actual era filenames (without .py)
actual_files = {}
for text_entry in data["texts"]:
    text_id = text_entry["id"]
    data_dir = text_entry.get("data_dir", text_id)
    dir_path = os.path.join("data", data_dir)
    if os.path.isdir(dir_path):
        era_files = glob.glob(os.path.join(dir_path, "era_*.py"))
        actual_files[text_id] = [
            os.path.splitext(os.path.basename(f))[0] for f in era_files
        ]
    else:
        actual_files[text_id] = []

# Fix data_file mismatches
fixes = 0
missing_files = []

for era in data["eras"]:
    text_id = era["text"]
    manifest_df = era["data_file"]
    disk_files = actual_files.get(text_id, [])

    if manifest_df in disk_files:
        continue

    # Extract era number
    parts = manifest_df.split("_")
    if len(parts) >= 2:
        era_num = parts[1]
        matches = [f for f in disk_files if f.startswith(f"era_{era_num}_") or f == f"era_{era_num}"]
        if len(matches) == 1:
            old = manifest_df
            new_val = matches[0]
            era["data_file"] = new_val
            print(f"  FIX: {text_id} | {old} -> {new_val}")
            fixes += 1
        elif len(matches) == 0:
            missing_files.append((text_id, manifest_df))
        else:
            print(f"  AMBIGUOUS: {text_id} | {manifest_df} -> {matches}")

# Remove duplicate eras
seen = set()
dupes = []
for i, era in enumerate(data["eras"]):
    key = (era["text"], era["data_file"])
    if key in seen:
        dupes.append(i)
    seen.add(key)

for i in reversed(dupes):
    removed = data["eras"].pop(i)
    print(f"  REMOVED DUPE at {i}: {removed['text']}/{removed['data_file']}")

print(f"\nSummary: {fixes} fixes, {len(dupes)} dupes removed, {len(missing_files)} missing")
for t, f in missing_files:
    print(f"  MISSING: {t}/{f}")

# Write clean JSON
with open(MANIFEST, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nDone: {len(data['texts'])} texts, {len(data['eras'])} eras")

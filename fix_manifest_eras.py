"""Fix manifest.json era data_file entries to match actual files on disk."""
import json
import os
import glob

MANIFEST = "manifest.json"

with open(MANIFEST, "r", encoding="utf-8") as f:
    data = json.load(f)

# Build a map: text_id -> list of actual era filenames (without .py extension)
actual_files = {}
for text_entry in data["texts"]:
    text_id = text_entry["id"]
    data_dir = text_entry.get("data_dir", text_id)
    dir_path = os.path.join("data", data_dir)
    if os.path.isdir(dir_path):
        era_files = glob.glob(os.path.join(dir_path, "era_*.py"))
        # Strip path and .py extension
        actual_files[text_id] = [
            os.path.splitext(os.path.basename(f))[0] for f in era_files
        ]
    else:
        actual_files[text_id] = []

print("=== Actual era files on disk ===")
for tid, files in sorted(actual_files.items()):
    if files:
        print(f"  {tid}: {files}")

fixes = 0
missing = []

for era in data["eras"]:
    text_id = era["text"]
    manifest_df = era["data_file"]
    disk_files = actual_files.get(text_id, [])

    # Check if manifest data_file matches any actual file exactly
    if manifest_df in disk_files:
        continue  # Already correct

    # Try to find a match by era number
    # Extract era number from manifest data_file (e.g. "era_67_call" -> "67")
    parts = manifest_df.split("_")
    if len(parts) >= 2:
        era_num = parts[1]  # e.g. "67"
        # Find actual files starting with era_{num}
        matches = [f for f in disk_files if f.startswith(f"era_{era_num}_") or f == f"era_{era_num}"]
        if len(matches) == 1:
            old = manifest_df
            new = matches[0]
            era["data_file"] = new
            print(f"  FIX: {text_id} | {old} -> {new}")
            fixes += 1
        elif len(matches) == 0:
            print(f"  MISSING: {text_id} | {manifest_df} - no file on disk!")
            missing.append((text_id, manifest_df))
        else:
            print(f"  AMBIGUOUS: {text_id} | {manifest_df} -> {matches}")
    else:
        print(f"  WEIRD: {text_id} | {manifest_df}")

# Also check for duplicate eras (same text + same data_file)
seen = set()
dupes = []
for i, era in enumerate(data["eras"]):
    key = (era["text"], era["data_file"])
    if key in seen:
        dupes.append(i)
        print(f"  DUPLICATE at index {i}: {era['text']} / {era['data_file']}")
    seen.add(key)

# Remove duplicates (reverse order to preserve indices)
for i in reversed(dupes):
    data["eras"].pop(i)
    print(f"  Removed duplicate era at index {i}")

print(f"\n=== Summary ===")
print(f"  Fixes applied: {fixes}")
print(f"  Duplicates removed: {len(dupes)}")
print(f"  Missing files: {len(missing)}")
for t, f in missing:
    print(f"    {t}: {f}")

# Write corrected manifest
with open(MANIFEST, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\nManifest updated: {len(data['texts'])} texts, {len(data['eras'])} eras")

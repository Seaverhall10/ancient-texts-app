"""Combine partial Numbers flow files into one flow_numbers.py"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from flow_numbers_1_4 import FLOW_NUMBERS_1_4, NOTES_NUMBERS_1_4
from flow_numbers_5_8 import FLOW_NUMBERS_5_8, NOTES_NUMBERS_5_8
from flow_numbers_9_12 import FLOW_NUMBERS_9_12, NOTES_NUMBERS_9_12
from flow_numbers_13_16 import FLOW_NUMBERS_13_16, NOTES_NUMBERS_13_16
from flow_numbers_17_20 import FLOW_NUMBERS_17_20, NOTES_NUMBERS_17_20
from flow_numbers_21_24 import FLOW_NUMBERS_21_24, NOTES_NUMBERS_21_24
from flow_numbers_25_28 import FLOW_NUMBERS_25_28, NOTES_NUMBERS_25_28
from flow_numbers_29_32 import FLOW_NUMBERS_29_32, NOTES_NUMBERS_29_32
from flow_numbers_33_36 import FLOW_NUMBERS_33_36, NOTES_NUMBERS_33_36

FLOW_NUMBERS = {}
NOTES_NUMBERS = {}
for d in [FLOW_NUMBERS_1_4, FLOW_NUMBERS_5_8, FLOW_NUMBERS_9_12,
          FLOW_NUMBERS_13_16, FLOW_NUMBERS_17_20, FLOW_NUMBERS_21_24,
          FLOW_NUMBERS_25_28, FLOW_NUMBERS_29_32, FLOW_NUMBERS_33_36]:
    FLOW_NUMBERS.update(d)
for d in [NOTES_NUMBERS_1_4, NOTES_NUMBERS_5_8, NOTES_NUMBERS_9_12,
          NOTES_NUMBERS_13_16, NOTES_NUMBERS_17_20, NOTES_NUMBERS_21_24,
          NOTES_NUMBERS_25_28, NOTES_NUMBERS_29_32, NOTES_NUMBERS_33_36]:
    NOTES_NUMBERS.update(d)

out_path = os.path.join(os.path.dirname(__file__), "flow_numbers.py")
with open(out_path, "w", encoding="utf-8") as f:
    f.write('"""\nFlow translations for Numbers \u2014 accurate, literal English renderings.\n')
    f.write('Every verse of all 36 chapters. Formal equivalence style.\n')
    f.write('YHWH = the LORD. Original translation from the Hebrew Masoretic Text.\n')
    f.write('Study notes included for key theological moments and Christ typology.\n"""\n\n')

    f.write("FLOW_NUMBERS = {\n")
    for ch in sorted(FLOW_NUMBERS.keys()):
        f.write(f"    {ch}: {{  # Chapter {ch}\n")
        verses = FLOW_NUMBERS[ch]
        for v in sorted(verses.keys()):
            # Escape for Python string
            text = verses[v].replace("\\", "\\\\").replace("'", "\\'")
            f.write(f"        {v}: '{text}',\n")
        f.write("    },\n")
    f.write("}\n\n")

    f.write("NOTES_NUMBERS = {\n")
    for ch in sorted(NOTES_NUMBERS.keys()):
        notes = NOTES_NUMBERS[ch]
        if notes:
            f.write(f"    {ch}: {{\n")
            int_keys = [k for k in notes.keys() if isinstance(k, int)]
            for v in sorted(int_keys):
                text = str(notes[v]).replace("\\", "\\\\").replace("'", "\\'")
                f.write(f"        {v}: '{text}',\n")
            f.write("    },\n")
    f.write("}\n")

total_verses = sum(len(v) for v in FLOW_NUMBERS.values())
total_notes = sum(len(v) for v in NOTES_NUMBERS.values())
file_size = os.path.getsize(out_path)
print(f"Combined: {len(FLOW_NUMBERS)} chapters, {total_verses} verses")
print(f"Notes: {len(NOTES_NUMBERS)} chapters, {total_notes} notes")
print(f"File: {out_path}")
print(f"Size: {file_size:,} bytes ({file_size/1024:.1f} KB)")

# Verify all 36 chapters present
missing = [c for c in range(1, 37) if c not in FLOW_NUMBERS]
if missing:
    print(f"WARNING: Missing chapters: {missing}")
else:
    print("All 36 chapters present.")

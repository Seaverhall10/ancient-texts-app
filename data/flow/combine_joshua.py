"""Combine partial Joshua flow files into one flow_joshua.py"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from flow_joshua_1_6 import FLOW_JOSHUA_1_6, NOTES_JOSHUA_1_6
from flow_joshua_7_12 import FLOW_JOSHUA_7_12, NOTES_JOSHUA_7_12
from flow_joshua_13_19 import FLOW_JOSHUA_13_19, NOTES_JOSHUA_13_19
from flow_joshua_20_24 import FLOW_JOSHUA_20_24, NOTES_JOSHUA_20_24

FLOW_JOSHUA = {}
NOTES_JOSHUA = {}
for d in [FLOW_JOSHUA_1_6, FLOW_JOSHUA_7_12, FLOW_JOSHUA_13_19, FLOW_JOSHUA_20_24]:
    FLOW_JOSHUA.update(d)
for d in [NOTES_JOSHUA_1_6, NOTES_JOSHUA_7_12, NOTES_JOSHUA_13_19, NOTES_JOSHUA_20_24]:
    NOTES_JOSHUA.update(d)

out_path = os.path.join(os.path.dirname(__file__), "flow_joshua.py")
with open(out_path, "w", encoding="utf-8") as f:
    f.write('"""\nFlow translations for Joshua \u2014 accurate, literal English renderings.\n')
    f.write('Every verse of all 24 chapters. Formal equivalence style.\n')
    f.write('YHWH = the LORD. Original translation from the Hebrew Masoretic Text.\n')
    f.write('Study notes included for key theological moments and Christ typology.\n"""\n\n')

    f.write("FLOW_JOSHUA = {\n")
    for ch in sorted(FLOW_JOSHUA.keys()):
        f.write(f"    {ch}: {{  # Chapter {ch}\n")
        verses = FLOW_JOSHUA[ch]
        for v in sorted(verses.keys()):
            # Escape for Python string
            text = verses[v].replace("\\", "\\\\").replace("'", "\\'")
            f.write(f"        {v}: '{text}',\n")
        f.write("    },\n")
    f.write("}\n\n")

    f.write("NOTES_JOSHUA = {\n")
    for ch in sorted(NOTES_JOSHUA.keys()):
        notes = NOTES_JOSHUA[ch]
        if notes:
            f.write(f"    {ch}: {{\n")
            int_keys = [k for k in notes.keys() if isinstance(k, int)]
            for v in sorted(int_keys):
                text = str(notes[v]).replace("\\", "\\\\").replace("'", "\\'")
                f.write(f"        {v}: '{text}',\n")
            f.write("    },\n")
    f.write("}\n")

total_verses = sum(len(v) for v in FLOW_JOSHUA.values())
total_notes = sum(len(v) for v in NOTES_JOSHUA.values())
file_size = os.path.getsize(out_path)
print(f"Combined: {len(FLOW_JOSHUA)} chapters, {total_verses} verses")
print(f"Notes: {len(NOTES_JOSHUA)} chapters, {total_notes} notes")
print(f"File: {out_path}")
print(f"Size: {file_size:,} bytes ({file_size/1024:.1f} KB)")

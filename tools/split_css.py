import os, sys
D = chr(9472)
M = chr(8212)
BASE = os.path.join(os.environ["USERPROFILE"], "Desktop", "ANCIENT_TEXTS Study App")
OUT = os.path.join(BASE, "split_css.py")
SRC = os.path.join(BASE, "src", "css", "styles.css")
SRC_DIR = os.path.join(BASE, "src", "css")

sections = [
    ("_tokens.css", "ANCIENT TEXTS LIBRARY", False),
    ("_reset.css", "Reset & Base", True),
    ("layout.css", D+D+" Layout "+D, True),
    ("sidebar.css", D+D+" Sidebar "+D, True),
    ("main-content.css", D+D+" Main Content "+D, True),
    ("terms-callouts.css", D+D+" Hebrew Terms Grid", True),
    ("crossrefs.css", D+D+" Cross References", True),
    ("crossref-drawer.css", D+D+" Cross-Reference Drawer", True),
    ("glossary.css", D+D+" Glossary Overlay", True),
    ("map.css", D+D+" Ancient World Map", True),
    ("resources.css", D+D+" Resources Overlay", True),
    ("search.css", D+D+" Search Bar", True),
    ("bookmarks.css", D+D+" Bookmarks "+D, True),
    ("sidebar-toggle.css", D+D+" Sidebar Toggle", True),
    ("responsive.css", D+D+" Responsive "+D, True),
    ("interlinear.css", D+D+" Interlinear Reading Pane", True),
    ("scroll-flash.css", D+D+" Scroll Flash Animation", True),
    ("overlays.css", D+D+" Development Progress Overlay", True),
    ("fullscreen.css", D+D+" Reading Pane Fullscreen", True),
    ("print.css", D+D+" Print Styles", True),
    ("library.css", "LIBRARY VIEW", True),
    ("accessibility.css", "UX / ACCESSIBILITY", True),
    ("text-intro.css", "TEXT INTRODUCTION PANEL", True),
    ("thc.css", "THE HEAVENLY COURT", True),
    ("learn-hebrew.css", "LEARN HEBREW", True),
    ("study-controls.css", D+D+" Study View Controls", True),
    ("prophecy.css", D+D+" Prophecy Tracker", True),
    ("core-beliefs.css", D+D+" Core Beliefs", True),
    ("breadcrumbs.css", "BREADCRUMB NAVIGATION", True),
    ("chapter-nav.css", "PREV/NEXT CHAPTER", True),
    ("hai.css", "HALLELUJAH AI "+M+" Chat Panel", True),
    ("trails.css", "STUDY TRAILS", True),
    ("related-studies.css", "RELATED STUDIES", True),
    ("matrix.css", "BIBLE TRUTH MATRIX", True),
    ("religion-detail.css", "RELIGION DETAIL OVERLAY", True),
    ("analytics.css", "USAGE ANALYTICS", True),
    ("timeline.css", "BIBLICAL + WORLD HISTORY", True),
    ("animations.css", "VIEW TRANSITIONS", True),
    ("keyboard-help.css", "KEYBOARD SHORTCUT HELP", True),
]

# Now do the actual split
with open(SRC, "rb") as fh:
    original = fh.read()
all_lines = original.splitlines(keepends=True)
total = len(all_lines)
print("Read %d lines from %s" % (total, SRC))
print()

def find_marker_line(lines, marker, top_level_only, start_search=0):
    for i in range(start_search, len(lines)):
        if marker in lines[i]:
            if top_level_only:
                indent = len(lines[i]) - len(lines[i].lstrip())
                if indent > 3:
                    continue
            return i
    return None

boundaries = []
for filename, marker, top_level in sections:
    idx = find_marker_line(all_lines, marker.encode("utf-8"), top_level)
    if idx is None:
        print("  WARNING: no marker for %s" % filename)
        continue
    boundaries.append((idx, filename))

boundaries.sort(key=lambda x: x[0])

if boundaries and boundaries[0][0] != 0:
    ti = [i for i, b in enumerate(boundaries) if b[1] == "_tokens.css"]
    if ti:
        boundaries.pop(ti[0])
    boundaries.insert(0, (0, "_tokens.css"))
elif boundaries and boundaries[0][1] == "_tokens.css" and boundaries[0][0] != 0:
    boundaries[0] = (0, boundaries[0][1])

os.makedirs(SRC_DIR, exist_ok=True)
written_files = []
total_written = 0

for i, (start, fname) in enumerate(boundaries):
    end = boundaries[i + 1][0] if i + 1 < len(boundaries) else total
    chunk = all_lines[start:end]
    out_path = os.path.join(SRC_DIR, fname)
    with open(out_path, "wb") as fh:
        fh.writelines(chunk)
    n = len(chunk)
    total_written += n
    written_files.append(fname)
    print("  %-25s  lines %5d-%5d  (%5d lines)" % (fname, start + 1, end, n))

print()
print("  %-25s  %12s  (%5d lines)" % ("TOTAL", "", total_written))
print("  Original:                                (%5d lines)" % total)

if total_written != total:
    print("  ERROR: line count mismatch! %d vs %d" % (total_written, total))
    sys.exit(1)
else:
    print("  Line counts match.")

order_path = os.path.join(SRC_DIR, "build-order.txt")
with open(order_path, "w", encoding="utf-8") as fh:
    for fn in written_files:
        fh.write(fn + "\n")
print()
print("  Wrote " + order_path)

print()
print("  Verifying concatenation reproduces original ...")
concat = []
for fn in written_files:
    fpath = os.path.join(SRC_DIR, fn)
    with open(fpath, "rb") as fh:
        concat.append(fh.read())
reassembled = b"".join(concat)

if reassembled == original:
    print("  PASS: concatenated output is byte-identical to styles.css")
else:
    ml = min(len(reassembled), len(original))
    ln = reassembled[:dp].count("\n") + 1
    print("  FAIL: first diff at char %d (line ~%d)" % (dp, ln))
    print("    Original len: %d" % len(original))
    print("    Rebuilt len:  %d" % len(reassembled))
    sys.exit(1)

print()
print("  Done. %d component files written to %s/" % (len(written_files), SRC_DIR))

# Also save as split_css.py for re-running
print()
print("  Re-run with: python split_css.py")

"""Combine partial flow files into single per-book flow files.
Auto-discovers all flow_*.py partials and merges by book name."""
import sys, os, glob, importlib, importlib.util
sys.path.insert(0, os.path.dirname(__file__))

FLOW_DIR = os.path.dirname(__file__)


def write_combined(out_name, book_name, flow_dict, notes_dict):
    """Write a combined flow file."""
    out_path = os.path.join(FLOW_DIR, out_name)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f'"""\nFlow translations for {book_name} \u2014 accurate, literal English renderings.\n')
        f.write(f'Every verse of all {len(flow_dict)} chapters. Formal equivalence style.\n')
        f.write('YHWH = the LORD. Original translation from the Hebrew Masoretic Text.\n')
        f.write('Study notes included for key theological moments and Christ typology.\n"""\n\n')

        var_name = "FLOW_" + book_name.upper()
        f.write(f"{var_name} = {{\n")
        for ch in sorted(flow_dict.keys()):
            f.write(f"    {ch}: {{  # Chapter {ch}\n")
            verses = flow_dict[ch]
            for v in sorted(verses.keys()):
                text = verses[v].replace("\n", " ").replace("\r", "").replace("\\", "\\\\").replace("'", "\\'")
                f.write(f"        {v}: '{text}',\n")
            f.write("    },\n")
        f.write("}\n\n")

        notes_name = "NOTES_" + book_name.upper()
        f.write(f"{notes_name} = {{\n")
        for ch in sorted(notes_dict.keys()):
            notes = notes_dict[ch]
            if notes:
                f.write(f"    {ch}: {{\n")
                int_keys = [k for k in notes.keys() if isinstance(k, int)]
                for v in sorted(int_keys):
                    text = str(notes[v]).replace("\n", " ").replace("\r", "").replace("\\", "\\\\").replace("'", "\\'")
                    f.write(f"        {v}: '{text}',\n")
                f.write("    },\n")
        f.write("}\n")

    total_v = sum(len(v) for v in flow_dict.values())
    total_n = sum(len(v) for v in notes_dict.values())
    size = os.path.getsize(out_path)
    print(f"  {book_name}: {len(flow_dict)} chapters, {total_v} verses, {total_n} notes ({size:,} bytes)")
    return out_path


def load_module_safe(mod_name, path):
    """Load a module from a specific path, return None on failure."""
    try:
        spec = importlib.util.spec_from_file_location(mod_name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    except Exception as e:
        print(f"  SKIP: {os.path.basename(path)} ({e})")
        return None


def get_dicts(mod):
    """Get FLOW_ and NOTES_ dicts from a module."""
    flow = notes = None
    for attr in sorted(dir(mod)):
        if attr.startswith("FLOW") and flow is None:
            flow = getattr(mod, attr)
        if attr.startswith("NOTES") and notes is None:
            notes = getattr(mod, attr)
    return flow or {}, notes or {}


def discover_and_combine(book_key, book_display):
    """Auto-discover all partial files for a book and combine."""
    print(f"[{book_display}]")
    parts_flow = {}
    parts_notes = {}

    # Find all files matching flow_<book>*.py (but not the combined output)
    pattern = os.path.join(FLOW_DIR, f"flow_{book_key}*.py")
    combined_name = f"flow_{book_key}.py"

    # Also check notes_<book>*.py for standalone notes files
    notes_pattern = os.path.join(FLOW_DIR, f"notes_{book_key}*.py")

    for path in sorted(glob.glob(pattern)):
        fname = os.path.basename(path)
        if fname == combined_name:
            continue  # skip the output file
        mod_name = fname.replace(".py", "")
        mod = load_module_safe(mod_name, path)
        if mod:
            f, n = get_dicts(mod)
            parts_flow.update(f)
            parts_notes.update(n)

    # Load standalone notes files
    for path in sorted(glob.glob(notes_pattern)):
        fname = os.path.basename(path)
        mod_name = fname.replace(".py", "")
        mod = load_module_safe(mod_name, path)
        if mod:
            _, n = get_dicts(mod)
            # Notes files may have NOTES_ prefix
            for attr in dir(mod):
                if attr.startswith("NOTES"):
                    nd = getattr(mod, attr)
                    if isinstance(nd, dict):
                        parts_notes.update(nd)

    if parts_flow:
        write_combined(combined_name, book_display, parts_flow, parts_notes)
    else:
        print(f"  NO DATA for {book_display}")


if __name__ == "__main__":
    print("=== Combining flow translation files ===\n")

    for key, display in [
        ("genesis", "Genesis"),
        ("exodus", "Exodus"),
        ("leviticus", "Leviticus"),
        ("numbers", "Numbers"),
        ("deuteronomy", "Deuteronomy"),
        ("joshua", "Joshua"),
        ("judges", "Judges"),
        ("ruth", "Ruth"),
        ("1samuel", "1Samuel"),
        ("2samuel", "2Samuel"),
        ("1kings", "1Kings"),
        ("2kings", "2Kings"),
        ("psalms", "Psalms"),
        ("isaiah", "Isaiah"),
        ("daniel", "Daniel"),
    ]:
        discover_and_combine(key, display)

    print("\nDone! Run build.py to integrate.")

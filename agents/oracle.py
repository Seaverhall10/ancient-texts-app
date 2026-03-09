"""
THE ORACLE — Planning & Prioritization Agent

Surveys the project state, identifies gaps, and creates a prioritized
task queue for THE SCRIBE, THE LECTOR, and THE ARBITER.

Usage:
    python agents/oracle.py --plan           # Generate task queue
    python agents/oracle.py --plan --dry-run # Show plan without creating tasks
"""
import os
import sys
import json
import argparse
import importlib.util
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.config import (
    ORACLE_API_KEY, ORACLE_MODEL, ORACLE_TEMPERATURE,
    DATA_DIR, MANIFEST_PATH, PENDING_DIR, REPORTS_DIR,
    THEOLOGICAL_GUIDELINES, ERA_DATA_FORMAT, MAX_TOKENS_ORACLE
)


def get_client():
    """Create Anthropic client with ORACLE's own API key."""
    if not ORACLE_API_KEY:
        print("ERROR: Set ORACLE_API_KEY in agents/config.py or environment")
        sys.exit(1)
    from anthropic import Anthropic
    return Anthropic(api_key=ORACLE_API_KEY)


def load_manifest():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def survey_project():
    """Survey the entire project and return a status summary."""
    manifest = load_manifest()
    status = {
        "texts": [],
        "missing_eras": [],
        "thin_chapters": [],
        "missing_info": [],
        "empty_texts": [],
        "glossary_count": 0,
        "total_chapters": 0,
        "total_fragments": 0,
    }

    # Glossary count
    gpath = os.path.join(DATA_DIR, "glossary.py")
    if os.path.exists(gpath):
        mod = load_module("glossary", gpath)
        status["glossary_count"] = len(getattr(mod, "GLOSSARY", {}))

    for text_def in manifest["texts"]:
        text_id = text_def["id"]
        data_dir = text_def.get("data_dir", text_id)
        eras = [e for e in manifest["eras"] if e.get("text") == text_id]

        text_status = {
            "id": text_id,
            "name": text_def["name"],
            "category": text_def["category"],
            "era_count": len(eras),
            "chapter_count": 0,
            "has_info": os.path.exists(os.path.join(DATA_DIR, data_dir, "info.py")),
            "content_type": text_def.get("content_type", "python_data"),
        }

        for era in eras:
            if era.get("content_type") == "html_fragment":
                frags = era.get("fragments", [])
                frag_count = 0
                for frag in frags:
                    fpath = os.path.join(DATA_DIR, "heavenly_court", "chapters", frag["file"])
                    if os.path.exists(fpath):
                        frag_count += 1
                text_status["chapter_count"] += frag_count
                status["total_fragments"] += frag_count
            else:
                data_file = era.get("data_file")
                if not data_file:
                    status["missing_eras"].append({"era": era["id"], "text": text_id})
                    continue

                path = os.path.join(DATA_DIR, data_dir, data_file + ".py")
                if not os.path.exists(path):
                    path = os.path.join(DATA_DIR, data_file + ".py")
                if not os.path.exists(path):
                    status["missing_eras"].append({"era": era["id"], "text": text_id, "file": data_file})
                    continue

                try:
                    mod = load_module(data_file, path)
                    chapters = getattr(mod, "CHAPTERS", [])
                    ch_count = len([c for c in chapters if c.get("type") == "chapter"])
                    text_status["chapter_count"] += ch_count
                    status["total_chapters"] += ch_count

                    # Check for thin chapters (fewer than 2 sections)
                    for ch in chapters:
                        if ch.get("type") == "chapter":
                            sections = ch.get("sections", [])
                            if len(sections) < 2:
                                status["thin_chapters"].append({
                                    "id": ch.get("id"),
                                    "title": ch.get("title"),
                                    "era": era["id"],
                                    "text": text_id,
                                    "sections": len(sections)
                                })
                except Exception:
                    pass

        if not text_status["has_info"]:
            status["missing_info"].append(text_id)
        if text_status["chapter_count"] == 0 and text_status["era_count"] > 0:
            status["empty_texts"].append(text_id)

        status["texts"].append(text_status)

    return status


def generate_tasks(status, use_ai=True):
    """Generate prioritized task queue from project status."""
    tasks = []
    priority = 0

    # Priority 1: Missing era data files (content gaps)
    for missing in status["missing_eras"]:
        priority += 1
        tasks.append({
            "id": f"task_{priority:03d}",
            "agent": "scribe",
            "priority": priority,
            "description": f"Write era data file for {missing['era']} (text: {missing['text']}). "
                          f"Create CHAPTERS list with study content covering this era's scope. "
                          f"Follow the ERA_DATA_FORMAT template. Include cross-references, "
                          f"hebrew_terms, divine_council_note, and 3-6 sections per chapter.",
            "output_path": os.path.join(DATA_DIR, missing['text'],
                                       missing.get('file', missing['era']) + ".py"),
            "metadata": {"text": missing["text"], "era": missing["era"], "type": "era_data"}
        })

    # Priority 2: Thin chapters that need expansion
    for thin in status["thin_chapters"]:
        priority += 1
        tasks.append({
            "id": f"task_{priority:03d}",
            "agent": "scribe",
            "priority": priority,
            "description": f"Expand thin chapter '{thin['title']}' (id: {thin['id']}, "
                          f"era: {thin['era']}). Currently has only {thin['sections']} section(s). "
                          f"Add 3-5 more sections with detailed analysis, cross-references, "
                          f"ANE context, and Second Temple sources where relevant.",
            "metadata": {"chapter_id": thin["id"], "era": thin["era"],
                        "text": thin["text"], "type": "expansion"}
        })

    # Priority 3: Missing info.py files
    for text_id in status["missing_info"]:
        priority += 1
        tasks.append({
            "id": f"task_{priority:03d}",
            "agent": "scribe",
            "priority": priority,
            "description": f"Write info.py scholarly introduction for text '{text_id}'. "
                          f"Include: display_name, canonical_status, authorship, date, "
                          f"audience, language, scripture_alignment, manuscripts, "
                          f"historical_context, divine_council relevance, and reader_notes.",
            "output_path": os.path.join(DATA_DIR, text_id, "info.py"),
            "metadata": {"text": text_id, "type": "info"}
        })

    # Priority 4: Glossary expansion (LECTOR tasks)
    # One task per text to add missing glossary terms
    for text_status in status["texts"]:
        if text_status["chapter_count"] > 0:
            priority += 1
            tasks.append({
                "id": f"task_{priority:03d}",
                "agent": "lector",
                "priority": priority,
                "description": f"Review all chapters in '{text_status['name']}' and identify "
                              f"Hebrew/Aramaic/Greek terms that should be in the glossary but "
                              f"are not. Generate new glossary entries with proper transliteration, "
                              f"Strong's numbers, definitions, and chapters_used arrays.",
                "metadata": {"text": text_status["id"], "type": "glossary_expansion"}
            })

    # Priority 5: Full audit (ARBITER task)
    priority += 1
    tasks.append({
        "id": f"task_{priority:03d}",
        "agent": "arbiter",
        "priority": priority,
        "description": "Run full audit of all content. Check theological accuracy, "
                      "canonical language violations, cross-reference integrity, "
                      "transliteration consistency, and formatting.",
        "metadata": {"type": "full_audit"}
    })

    return tasks


def save_tasks(tasks, dry_run=False):
    """Save tasks as JSON files to the pending directory."""
    if dry_run:
        print(f"\n[oracle] DRY RUN — {len(tasks)} tasks would be created:\n")
        for task in tasks:
            agent = task.get("agent", "scribe").upper()
            print(f"  [{agent:>10}] P{task['priority']:02d} — {task['description'][:80]}...")
        return

    os.makedirs(PENDING_DIR, exist_ok=True)
    for task in tasks:
        task["status"] = "pending"
        task["created_at"] = datetime.now().isoformat()
        task["created_by"] = "oracle"
        fpath = os.path.join(PENDING_DIR, f"{task['id']}.json")
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(task, f, indent=2, ensure_ascii=False)

    print(f"[oracle] Created {len(tasks)} tasks in {PENDING_DIR}")


def generate_report(status, tasks):
    """Generate a planning report."""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(REPORTS_DIR, f"oracle_plan_{timestamp}.md")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# THE ORACLE -- Project Plan\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write(f"## Project Status\n\n")
        f.write(f"| Metric | Value |\n|--------|-------|\n")
        f.write(f"| Total texts | {len(status['texts'])} |\n")
        f.write(f"| Total chapters | {status['total_chapters']} |\n")
        f.write(f"| Total fragments | {status['total_fragments']} |\n")
        f.write(f"| Glossary terms | {status['glossary_count']} |\n")
        f.write(f"| Missing eras | {len(status['missing_eras'])} |\n")
        f.write(f"| Thin chapters | {len(status['thin_chapters'])} |\n")
        f.write(f"| Missing info.py | {len(status['missing_info'])} |\n\n")

        f.write(f"## Text Status\n\n")
        f.write(f"| Text | Category | Eras | Chapters | Info |\n")
        f.write(f"|------|----------|------|----------|------|\n")
        for t in status["texts"]:
            info = "[OK]" if t["has_info"] else "[X]"
            f.write(f"| {t['name']} | {t['category']} | {t['era_count']} | {t['chapter_count']} | {info} |\n")

        if tasks:
            f.write(f"\n## Task Queue ({len(tasks)} tasks)\n\n")
            for task in tasks:
                agent = task.get("agent", "scribe").upper()
                f.write(f"- **[{agent}]** P{task['priority']:02d} -- {task['description'][:100]}\n")

    print(f"[oracle] Report saved: {report_path}")
    return report_path


def main():
    parser = argparse.ArgumentParser(description="THE ORACLE -- Planning Agent")
    parser.add_argument("--plan", action="store_true", help="Generate task queue")
    parser.add_argument("--dry-run", action="store_true", help="Show plan without creating tasks")
    parser.add_argument("--status", action="store_true", help="Show project status only")
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"  THE ORACLE -- Project Planning")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}\n")

    status = survey_project()

    if args.status:
        print(f"  Texts: {len(status['texts'])}")
        print(f"  Chapters: {status['total_chapters']}")
        print(f"  Fragments: {status['total_fragments']}")
        print(f"  Glossary: {status['glossary_count']} terms")
        print(f"  Missing eras: {len(status['missing_eras'])}")
        print(f"  Thin chapters: {len(status['thin_chapters'])}")
        print(f"  Missing info: {len(status['missing_info'])}")
        return

    if args.plan:
        print("[oracle] Surveying project state...")
        tasks = generate_tasks(status)
        report = generate_report(status, tasks)
        save_tasks(tasks, dry_run=args.dry_run)

        scribe_tasks = sum(1 for t in tasks if t.get("agent") == "scribe")
        lector_tasks = sum(1 for t in tasks if t.get("agent") == "lector")
        arbiter_tasks = sum(1 for t in tasks if t.get("agent") == "arbiter")

        print(f"\n  Plan: {len(tasks)} tasks total")
        print(f"    SCRIBE:  {scribe_tasks} content tasks")
        print(f"    LECTOR:  {lector_tasks} language tasks")
        print(f"    ARBITER: {arbiter_tasks} audit tasks")
        print(f"\n{'='*60}")
    else:
        print("Usage:")
        print("  python agents/oracle.py --plan           # Generate task queue")
        print("  python agents/oracle.py --plan --dry-run # Preview without creating")
        print("  python agents/oracle.py --status         # Show project status")


if __name__ == "__main__":
    main()

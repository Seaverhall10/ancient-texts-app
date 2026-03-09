"""
run_council.py — The Builder's Council Orchestrator

Runs the full 5-agent pipeline:
1. ORACLE surveys project and creates task queue
2. SCRIBE processes content generation tasks
3. LECTOR processes language/glossary tasks
4. ARBITER audits all content
5. ARCHITECT builds and reports status

Usage:
    python agents/run_council.py                    # Full pipeline
    python agents/run_council.py --skip-plan        # Skip ORACLE (use existing tasks)
    python agents/run_council.py --scribe-only      # Just SCRIBE tasks
    python agents/run_council.py --lector-only      # Just LECTOR tasks
    python agents/run_council.py --audit-only       # Just ARBITER audit
    python agents/run_council.py --build-only       # Just ARCHITECT build
"""
import os
import sys
import json
import argparse
import time
from datetime import datetime

# Fix Windows console encoding for Unicode (Hebrew/Greek transliterations)
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.config import PENDING_DIR, IN_PROGRESS_DIR, COMPLETED_DIR, REPORTS_DIR


def get_pending_tasks(agent_filter=None):
    """List all pending task files, optionally filtered by agent."""
    if not os.path.isdir(PENDING_DIR):
        return []
    tasks = []
    for fname in sorted(os.listdir(PENDING_DIR)):
        if fname.endswith(".json"):
            fpath = os.path.join(PENDING_DIR, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                task = json.load(f)
            task["_file"] = fpath
            task["_name"] = fname
            if agent_filter and task.get("agent") != agent_filter:
                continue
            tasks.append(task)
    return tasks


def move_task(task, dest_dir):
    """Move a task file to a different status directory."""
    os.makedirs(dest_dir, exist_ok=True)
    src = task["_file"]
    dst = os.path.join(dest_dir, task["_name"])
    os.rename(src, dst)
    task["_file"] = dst


def run_oracle():
    """Phase 1: THE ORACLE creates the task queue."""
    from agents.oracle import survey_project, generate_tasks, save_tasks, generate_report

    print("\n[council] Phase 1: THE ORACLE surveys and plans...")
    status = survey_project()
    tasks = generate_tasks(status)
    report = generate_report(status, tasks)
    save_tasks(tasks)

    scribe_tasks = sum(1 for t in tasks if t.get("agent") == "scribe")
    lector_tasks = sum(1 for t in tasks if t.get("agent") == "lector")
    arbiter_tasks = sum(1 for t in tasks if t.get("agent") == "arbiter")

    print(f"[council] ORACLE created {len(tasks)} tasks:")
    print(f"  SCRIBE:  {scribe_tasks}")
    print(f"  LECTOR:  {lector_tasks}")
    print(f"  ARBITER: {arbiter_tasks}")
    return tasks


def run_scribe_tasks():
    """Phase 2: THE SCRIBE processes content tasks."""
    from agents.scribe import run_scribe

    tasks = get_pending_tasks(agent_filter="scribe")
    if not tasks:
        print("[council] No pending SCRIBE tasks.")
        return 0

    print(f"\n[council] Phase 2: THE SCRIBE — {len(tasks)} content task(s)")
    completed = 0

    for task in tasks:
        print(f"\n  [{completed+1}/{len(tasks)}] {task.get('description', task['_name'])[:70]}...")
        move_task(task, IN_PROGRESS_DIR)

        try:
            output_path = task.get("output_path")

            # Auto-generate output path for expansion tasks that don't specify one
            if not output_path and task.get("metadata", {}).get("type") == "expansion":
                task_id = task.get("id", task["_name"].replace(".json", ""))
                output_path = os.path.join(REPORTS_DIR, f"scribe_expansion_{task_id}.py")

            content = run_scribe(task["description"], output_path)

            task["completed_at"] = datetime.now().isoformat()
            task["status"] = "completed"
            if output_path:
                task["output_path"] = output_path
            with open(task["_file"], "w", encoding="utf-8") as f:
                json.dump(task, f, indent=2, ensure_ascii=False)
            move_task(task, COMPLETED_DIR)
            completed += 1
            print(f"  [OK] Task completed")

        except Exception as e:
            print(f"  [X] Task failed: {e}")
            task["error"] = str(e)
            task["status"] = "failed"
            with open(task["_file"], "w", encoding="utf-8") as f:
                json.dump(task, f, indent=2, ensure_ascii=False)

        # Brief pause between API calls
        time.sleep(2)

    return completed


def run_lector_tasks():
    """Phase 3: THE LECTOR processes language tasks."""
    from agents.lector import generate_glossary_entries, merge_glossary_entries

    tasks = get_pending_tasks(agent_filter="lector")
    if not tasks:
        print("[council] No pending LECTOR tasks.")
        return 0

    print(f"\n[council] Phase 3: THE LECTOR — {len(tasks)} language task(s)")
    completed = 0

    for task in tasks:
        print(f"\n  [{completed+1}/{len(tasks)}] {task.get('description', task['_name'])[:70]}...")
        move_task(task, IN_PROGRESS_DIR)

        try:
            new_entries, usage = generate_glossary_entries(task["description"])
            if new_entries:
                added, skipped = merge_glossary_entries(new_entries)
                task["result"] = {"added": added, "skipped": skipped}

            task["completed_at"] = datetime.now().isoformat()
            task["status"] = "completed"
            task["tokens"] = {"input": usage.input_tokens, "output": usage.output_tokens}
            with open(task["_file"], "w", encoding="utf-8") as f:
                json.dump(task, f, indent=2, ensure_ascii=False)
            move_task(task, COMPLETED_DIR)
            completed += 1
            print(f"  [OK] Task completed")

        except Exception as e:
            print(f"  [X] Task failed: {e}")
            task["error"] = str(e)
            task["status"] = "failed"
            with open(task["_file"], "w", encoding="utf-8") as f:
                json.dump(task, f, indent=2, ensure_ascii=False)

        time.sleep(2)

    return completed


def run_arbiter_audit():
    """Phase 4: THE ARBITER audits all content."""
    from agents.arbiter import run_local_audit, generate_report

    print("\n[council] Phase 4: THE ARBITER audits...")
    findings = run_local_audit()
    report = generate_report(findings, "council_audit")

    critical = sum(1 for f in findings if f["level"] == "CRITICAL")
    warnings = sum(1 for f in findings if f["level"] == "WARNING")
    infos = sum(1 for f in findings if f["level"] == "INFO")

    print(f"[council] Audit: {critical} critical, {warnings} warnings, {infos} info")

    # Also process any pending arbiter tasks (AI deep audits)
    tasks = get_pending_tasks(agent_filter="arbiter")
    for task in tasks:
        move_task(task, IN_PROGRESS_DIR)
        task["completed_at"] = datetime.now().isoformat()
        task["status"] = "completed"
        task["result"] = {
            "critical": critical,
            "warnings": warnings,
            "info": infos,
            "total": len(findings)
        }
        with open(task["_file"], "w", encoding="utf-8") as f:
            json.dump(task, f, indent=2, ensure_ascii=False)
        move_task(task, COMPLETED_DIR)

    return findings


def run_architect_build():
    """Phase 5: THE ARCHITECT builds and reports."""
    from agents.architect import run_build, print_status, save_status_report

    print("\n[council] Phase 5: THE ARCHITECT builds...")
    success = run_build()

    if success:
        save_status_report()
        print_status()
    else:
        print("[council] [X] Build failed!")

    return success


def main():
    parser = argparse.ArgumentParser(description="The Builder's Council Orchestrator")
    parser.add_argument("--skip-plan", action="store_true", help="Skip ORACLE planning")
    parser.add_argument("--scribe-only", action="store_true", help="Only run SCRIBE tasks")
    parser.add_argument("--lector-only", action="store_true", help="Only run LECTOR tasks")
    parser.add_argument("--audit-only", action="store_true", help="Only run ARBITER audit")
    parser.add_argument("--build-only", action="store_true", help="Only run ARCHITECT build")
    args = parser.parse_args()

    start_time = datetime.now()

    print(f"\n{'='*60}")
    print(f"  THE BUILDER'S COUNCIL")
    print(f"  {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")

    if args.scribe_only:
        completed = run_scribe_tasks()
        print(f"\n  SCRIBE completed {completed} tasks")
    elif args.lector_only:
        completed = run_lector_tasks()
        print(f"\n  LECTOR completed {completed} tasks")
    elif args.audit_only:
        run_arbiter_audit()
    elif args.build_only:
        run_architect_build()
    else:
        # Full pipeline
        if not args.skip_plan:
            print("\n=== Phase 1: THE ORACLE ===")
            oracle_tasks = run_oracle()

        print("\n=== Phase 2: THE SCRIBE ===")
        scribe_completed = run_scribe_tasks()

        print("\n=== Phase 3: THE LECTOR ===")
        lector_completed = run_lector_tasks()

        print("\n=== Phase 4: THE ARBITER ===")
        findings = run_arbiter_audit()
        critical = sum(1 for f in findings if f["level"] == "CRITICAL")

        if critical > 3:
            print(f"\n  [!] {critical} CRITICAL issues. Review before building.")
            print(f"  Continuing with build anyway (review report after)...")

        print("\n=== Phase 5: THE ARCHITECT ===")
        build_ok = run_architect_build()

        elapsed = (datetime.now() - start_time).total_seconds()

        print(f"\n{'='*60}")
        print(f"  COUNCIL SESSION COMPLETE")
        print(f"  Duration: {elapsed/60:.1f} minutes")
        print(f"  SCRIBE:    {scribe_completed} tasks completed")
        print(f"  LECTOR:    {lector_completed} tasks completed")
        print(f"  ARBITER:   {len(findings)} findings")
        print(f"  ARCHITECT: {'BUILD OK' if build_ok else 'BUILD FAILED'}")
        print(f"{'='*60}")

        # Save session summary
        os.makedirs(REPORTS_DIR, exist_ok=True)
        summary_path = os.path.join(REPORTS_DIR, f"council_session_{start_time.strftime('%Y%m%d_%H%M%S')}.md")
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(f"# Builder's Council Session Report\n\n")
            f.write(f"**Date:** {start_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Duration:** {elapsed/60:.1f} minutes\n\n")
            f.write(f"## Results\n\n")
            f.write(f"| Agent | Result |\n|-------|--------|\n")
            f.write(f"| ORACLE | Planned tasks |\n")
            f.write(f"| SCRIBE | {scribe_completed} tasks completed |\n")
            f.write(f"| LECTOR | {lector_completed} tasks completed |\n")
            f.write(f"| ARBITER | {len(findings)} findings ({critical} critical) |\n")
            f.write(f"| ARCHITECT | {'SUCCESS' if build_ok else 'FAILED'} |\n")
        print(f"\n  Session report: {summary_path}")


if __name__ == "__main__":
    main()

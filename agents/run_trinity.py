"""
run_trinity.py — Orchestrator for the Agent Trinity.

Runs THE SCRIBE, THE ARBITER, and THE ARCHITECT in sequence:
1. SCRIBE generates content from pending tasks
2. ARBITER audits all content
3. ARCHITECT builds and reports status

Usage:
    python agents/run_trinity.py                    # Full pipeline
    python agents/run_trinity.py --scribe-only      # Just content generation
    python agents/run_trinity.py --audit-only       # Just audit
    python agents/run_trinity.py --build-only       # Just build + status
"""
import os
import sys
import json
import argparse
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.config import PENDING_DIR, IN_PROGRESS_DIR, COMPLETED_DIR


def get_pending_tasks():
    """List all pending task files."""
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
            tasks.append(task)
    return tasks


def move_task(task, dest_dir):
    """Move a task file to a different status directory."""
    os.makedirs(dest_dir, exist_ok=True)
    src = task["_file"]
    dst = os.path.join(dest_dir, task["_name"])
    os.rename(src, dst)
    task["_file"] = dst


def run_scribe_tasks():
    """Process all pending SCRIBE tasks."""
    from agents.scribe import run_scribe

    tasks = get_pending_tasks()
    scribe_tasks = [t for t in tasks if t.get("agent", "scribe") == "scribe"]

    if not scribe_tasks:
        print("[trinity] No pending SCRIBE tasks.")
        return 0

    print(f"[trinity] Found {len(scribe_tasks)} SCRIBE task(s)")

    completed = 0
    for task in scribe_tasks:
        print(f"\n[trinity] Processing: {task.get('description', task['_name'])}")
        move_task(task, IN_PROGRESS_DIR)

        try:
            output_path = task.get("output_path")
            content = run_scribe(task["description"], output_path)

            # Mark completed
            task["completed_at"] = datetime.now().isoformat()
            task["status"] = "completed"
            with open(task["_file"], "w", encoding="utf-8") as f:
                json.dump(task, f, indent=2)
            move_task(task, COMPLETED_DIR)
            completed += 1
            print(f"[trinity] \u2714 Task completed")

        except Exception as e:
            print(f"[trinity] \u2718 Task failed: {e}")
            task["error"] = str(e)
            task["status"] = "failed"
            with open(task["_file"], "w", encoding="utf-8") as f:
                json.dump(task, f, indent=2)

    return completed


def run_arbiter_audit():
    """Run THE ARBITER full audit."""
    from agents.arbiter import run_local_audit, generate_report

    print("\n[trinity] Running ARBITER audit...")
    findings = run_local_audit()
    report = generate_report(findings, "trinity_audit")

    critical = sum(1 for f in findings if f["level"] == "CRITICAL")
    warnings = sum(1 for f in findings if f["level"] == "WARNING")
    infos = sum(1 for f in findings if f["level"] == "INFO")

    print(f"[trinity] Audit: {critical} critical, {warnings} warnings, {infos} info")

    return findings


def run_architect_build():
    """Run THE ARCHITECT build + status."""
    from agents.architect import run_build, print_status, save_status_report

    print("\n[trinity] Running ARCHITECT build...")
    success = run_build()

    if success:
        save_status_report()
        print_status()
    else:
        print("[trinity] \u2718 Build failed!")

    return success


def main():
    parser = argparse.ArgumentParser(description="Agent Trinity Orchestrator")
    parser.add_argument("--scribe-only", action="store_true", help="Only run SCRIBE tasks")
    parser.add_argument("--audit-only", action="store_true", help="Only run ARBITER audit")
    parser.add_argument("--build-only", action="store_true", help="Only run ARCHITECT build")
    args = parser.parse_args()

    print(f"\n{'='*60}")
    print(f"  AGENT TRINITY \u2014 Orchestrator")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")

    if args.scribe_only:
        run_scribe_tasks()
    elif args.audit_only:
        run_arbiter_audit()
    elif args.build_only:
        run_architect_build()
    else:
        # Full pipeline
        print("\n\u2550\u2550\u2550 Phase 1: THE SCRIBE \u2550\u2550\u2550")
        completed = run_scribe_tasks()

        print("\n\u2550\u2550\u2550 Phase 2: THE ARBITER \u2550\u2550\u2550")
        findings = run_arbiter_audit()

        critical = sum(1 for f in findings if f["level"] == "CRITICAL")
        if critical > 0:
            print(f"\n\u26A0 {critical} CRITICAL issues found. Review before building.")
            response = input("Continue with build? (y/N): ").strip().lower()
            if response != 'y':
                print("[trinity] Aborted. Fix critical issues first.")
                return

        print("\n\u2550\u2550\u2550 Phase 3: THE ARCHITECT \u2550\u2550\u2550")
        run_architect_build()

        print(f"\n{'='*60}")
        print(f"  TRINITY COMPLETE")
        print(f"  SCRIBE: {completed} tasks processed")
        print(f"  ARBITER: {len(findings)} findings")
        print(f"{'='*60}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import argparse
import ast
import os
import shutil
from pathlib import Path

CHALLENGES_DIR = Path(__file__).resolve().parent.parent / "challenges"
BACKUP_DIR = Path(__file__).resolve().parent.parent / ".backup"


def wipe_solution_py(solution_path, backup_dir=None, dry_run=False):
    with open(solution_path, "r") as f:
        tree = ast.parse(f.read(), filename=str(solution_path))
    new_body = []
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.FunctionDef):
            # Keep docstring if present
            func_body = []
            if (
                node.body
                and isinstance(node.body[0], ast.Expr)
                and isinstance(node.body[0].value, ast.Str)
            ):
                func_body.append(node.body[0])
            # Add a pass statement
            func_body.append(ast.Pass())
            node.body = func_body
        new_body.append(node)
    tree.body = new_body
    wiped_code = ast.unparse(tree)
    if dry_run:
        print(f"Would wipe: {solution_path}")
        return
    if backup_dir:
        backup_path = backup_dir / solution_path.relative_to(
            CHALLENGES_DIR.parent
        )
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(solution_path, backup_path)
    with open(solution_path, "w") as f:
        f.write(wiped_code)
    print(f"Wiped: {solution_path}")


def wipe_explanation_md(problem_dir, backup_dir=None, dry_run=False):
    exp_path = problem_dir / "EXPLANATION.md"
    if exp_path.exists():
        if dry_run:
            print(f"Would remove: {exp_path}")
            return
        if backup_dir:
            backup_path = backup_dir / exp_path.relative_to(
                CHALLENGES_DIR.parent
            )
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(exp_path, backup_path)
        exp_path.unlink()
        print(f"Removed: {exp_path}")


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Wipe all solution implementations (replace with 'pass', keep "
            "docstrings) in solution.py files. Optionally remove "
            "EXPLANATION.md files and/or backup wiped files to .backup. By "
            "default, runs in dry-run mode (shows what would be wiped). Use "
            "--yes to actually wipe."
        )
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Actually perform the wipe (not just dry run)",
    )
    parser.add_argument(
        "--wipe-explanations",
        action="store_true",
        help="Also remove EXPLANATION.md files",
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Backup wiped files to .backup directory",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be wiped (default)",
    )
    args = parser.parse_args()
    dry_run = not args.yes or args.dry_run
    backup_dir = BACKUP_DIR if args.backup else None
    if not dry_run:
        print(
            "WARNING: This will irreversibly wipe all solution "
            "implementations!\n"
        )
        if args.backup:
            print(f"Backups will be saved to: {BACKUP_DIR}\n")
    for category in CHALLENGES_DIR.iterdir():
        if category.is_dir():
            for problem in category.iterdir():
                if problem.is_dir():
                    solution_path = problem / "solution.py"
                    if solution_path.exists():
                        wipe_solution_py(solution_path, backup_dir, dry_run)
                    if args.wipe_explanations:
                        wipe_explanation_md(problem, backup_dir, dry_run)
    if dry_run:
        print("\n(Dry run only. Use --yes to actually wipe solutions.)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import argparse
import ast
import os
from pathlib import Path

CHALLENGES_DIR = Path(__file__).resolve().parent.parent / "challenges"


# Helper to find all problem directories
def iter_problem_dirs():
    for category in CHALLENGES_DIR.iterdir():
        if category.is_dir():
            for problem in category.iterdir():
                if problem.is_dir():
                    yield problem


def has_explanation(problem_dir):
    return (problem_dir / "EXPLANATION.md").exists()


def get_canonical_method(tree):
    # Look for a function with 'canonical' in the name
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.FunctionDef) and "canonical" in node.name:
            return node
    # Fallback: if only one function, return it
    funcs = [
        n for n in ast.iter_child_nodes(tree) if isinstance(n, ast.FunctionDef)
    ]
    if len(funcs) == 1:
        return funcs[0]
    return None


def is_stub_method(func_node):
    # Only a docstring and a single 'pass' statement
    body = func_node.body
    if not body:
        return True
    if len(body) == 1:
        if isinstance(body[0], ast.Pass):
            return True
        if isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Str):
            # Only docstring, so stub
            return True
    if len(body) == 2:
        # Docstring + pass
        if (
            isinstance(body[0], ast.Expr)
            and isinstance(body[0].value, ast.Str)
            and isinstance(body[1], ast.Pass)
        ):
            return True
    return False


def get_problem_status(problem_dir):
    solution_path = problem_dir / "solution.py"
    if not solution_path.exists():
        return None  # Not a valid problem
    try:
        with open(solution_path, "r") as f:
            tree = ast.parse(f.read(), filename=str(solution_path))
    except Exception:
        return None
    canonical = get_canonical_method(tree)
    if canonical is None:
        return None
    stub = is_stub_method(canonical)
    explanation = has_explanation(problem_dir)
    return {
        "path": str(problem_dir.relative_to(CHALLENGES_DIR)),
        "implemented": not stub,
        "unimplemented": stub,
        "has_explanation": explanation,
        "missing_explanation": not explanation,
    }


def print_missing_explanations(statuses):
    for s in statuses:
        if s["missing_explanation"]:
            print(f"  {s['path']}")


def print_with_explanations(statuses):
    for s in statuses:
        if s["has_explanation"]:
            print(f"  {s['path']}")


def main():
    parser = argparse.ArgumentParser(
        description=(
            "List coding problems by implementation and explanation status."
        )
    )
    parser.add_argument(
        "--unimplemented",
        action="store_true",
        help="List problems with unimplemented canonical solution.",
    )
    parser.add_argument(
        "--implemented",
        action="store_true",
        help="List problems with implemented canonical solution.",
    )
    parser.add_argument(
        "--missing-explanation",
        action="store_true",
        help="List problems missing EXPLANATION.md.",
    )
    parser.add_argument(
        "--has-explanation",
        action="store_true",
        help="List problems with EXPLANATION.md.",
    )
    parser.add_argument(
        "--all", action="store_true", help="Show summary of all categories."
    )
    args = parser.parse_args()

    statuses = []
    for problem_dir in iter_problem_dirs():
        status = get_problem_status(problem_dir)
        if status:
            statuses.append(status)

    if args.all or not any(
        [
            args.unimplemented,
            args.implemented,
            args.missing_explanation,
            args.has_explanation,
        ]
    ):
        print(f"Total problems: {len(statuses)}")
        print(f"Unimplemented: {sum(s['unimplemented'] for s in statuses)}")
        print(f"Implemented: {sum(s['implemented'] for s in statuses)}")
        print(
            "Missing EXPLANATION.md: "
            f"{sum(s['missing_explanation'] for s in statuses)}"
        )
        print(
            "Has EXPLANATION.md: "
            f"{sum(s['has_explanation'] for s in statuses)}"
        )
        print("\nSample unimplemented problems:")
        for s in statuses:
            if s["unimplemented"]:
                print(f"  {s['path']}")
        print("\nSample implemented problems:")
        for s in statuses:
            if s["implemented"]:
                print(f"  {s['path']}")
        print()
        print("With EXPLANATION.md:")
        print_with_explanations(statuses)
        return

    if args.unimplemented:
        print("Problems with unimplemented canonical solution:")
        for s in statuses:
            if s["unimplemented"]:
                print(f"  {s['path']}")
    if args.implemented:
        print("Problems with implemented canonical solution:")
        for s in statuses:
            if s["implemented"]:
                print(f"  {s['path']}")
    if args.missing_explanation:
        print("Problems missing EXPLANATION.md:")
        print_missing_explanations(statuses)
    if args.has_explanation:
        print("Problems with EXPLANATION.md:")
        print_with_explanations(statuses)


if __name__ == "__main__":
    main()

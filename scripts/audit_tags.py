import os
import re

def find_problem_dirs(base_dir="challenges"):
    problem_dirs = set()
    for root, dirs, files in os.walk(base_dir):
        # Skip the tags.md file and any hidden/system files
        if root == base_dir:
            continue
        if "README.md" in files or "solution.py" in files:
            rel_path = os.path.relpath(root, base_dir)
            if rel_path != ".":
                problem_dirs.add(rel_path.replace(os.sep, "/"))
    return problem_dirs

def parse_tags_md(tags_path="challenges/tags.md"):
    listed_dirs = set()
    with open(tags_path) as f:
        for line in f:
            m = re.match(r"\|\s*([a-zA-Z0-9_\/-]+)\s*\|", line)
            if m:
                listed_dirs.add(m.group(1))
    return listed_dirs

if __name__ == "__main__":
    codebase_dirs = find_problem_dirs()
    tags_dirs = parse_tags_md()
    missing_in_tags = codebase_dirs - tags_dirs
    missing_in_codebase = tags_dirs - codebase_dirs

    print("Problems in codebase but missing from tags.md:")
    for d in sorted(missing_in_tags):
        print("  ", d)
    print("\nProblems in tags.md but missing from codebase:")
    for d in sorted(missing_in_codebase):
        print("  ", d)
    if missing_in_tags or missing_in_codebase:
        exit(1)  # Block commit if there are discrepancies 
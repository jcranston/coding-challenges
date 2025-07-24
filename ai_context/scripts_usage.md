# Scripts Usage Guide

This file describes how and when to use project scripts, especially for adding new problems or automating workflows.

## Adding a New Problem
- Use the script `scripts/add_challenge.sh <problem_name>` to generate a new problem directory and starter files.
- The script will:
  - Create a new directory under the appropriate topic (e.g., `arrays/`, `graphs/`).
  - Add `solution.py`, `test_solution.py`, `README.md`, and `__init__.py` (if needed).
- After running the script, follow the steps in `ai_context/new_problem.md` to complete the setup.

## Other Scripts
- If there are other scripts (e.g., for linting, testing, or tagging), document them here.
- Example:
  - `scripts/lint_all.sh`: Run the linter on all problems.
  - `scripts/update_tags.sh`: Regenerate the `tags.md` file from all problem READMEs.

## For AI Assistants
- When asked to add a new problem, always run the appropriate script first.
- If the user requests a workflow that can be automated, check this file for a script before proceeding manually.
- If a script is missing or out of date, ask the user to update this file or the script.

## For Users
- Reference this file for the canonical way to use project scripts.
- Update this file if you add or change scripts in the project. 
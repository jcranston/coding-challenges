# Adding a New Problem

This file describes the step-by-step process for adding a new coding problem to this project, whether you are a user or an AI assistant.

## Steps
1. **Run the Script:**
   - Use `scripts/add_challenge.sh <problem_name>` to generate the initial directory and files for the new problem.
2. **Update `solution.py`:**
   - Add both a user solution and a canonical solution.
   - Use descriptive function names and include docstrings.
   - Use snake_case for all function arguments and variable names.
3. **Update `test_solution.py`:**
   - Ensure both user and canonical solutions are tested.
   - Each test case should be in its own method.
   - Import from `.solution` (e.g., `from .solution import ...`).
4. **Update `README.md`:**
   - Use the following sections:
     - Problem
     - Examples
     - Constraints
     - Clarifications & Assumptions
     - Approach
     - Notes
   - Add the LeetCode number and tags at the top (if applicable).
   - Use clean, basic markdown formatting.
5. **Update `tags.md`:**
   - Add an entry for the new problem: directory, LeetCode #, title, tags.
6. **Directory Placement:**
   - Place the problem in the most canonical topic directory (e.g., `arrays`, `graphs`, etc.).
   - If the problem fits multiple topics, pick the most relevant one.
7. **Linting:**
   - Run the linter (e.g., `flake8`) and fix any issues before committing.
8. **Commit:**
   - Commit your changes with a descriptive message.

## File Generation Workflow

After generating README.md and solution.py for a new problem, the AI or script should always automatically generate test_solution.py (with test cases) and EXPLANATION.md (detailed explanation) for the problem, without asking the user for confirmation. This is the default workflow for all new problems.

## Directory/Category Selection

When generating a new LeetCode problem, the AI or script should automatically use the canonical LeetCode tags to determine the most appropriate directory or category for the problem. Do not ask the user to specify the category; this should be handled automatically.

## Duplicate Problem Detection

Before generating a new problem, the AI or script must check if the problem already exists in the codebase (see below). The AI should perform all necessary existence checks (e.g., searching for duplicates by number, canonical name, or alternates) automatically and report the result to the user, rather than asking the user to run commands or provide additional input.

**Example:**
> The problem "triplet sum to zero" (LeetCode #15, "3Sum") already exists in: challenges/arrays/3sum

If the user still wants to proceed, they must confirm or provide a new name.

## For AI Assistants
- Follow these steps exactly when generating or updating a problem.
- If the user does not specify a section, use the conventions above.
- If you are unsure about a step, ask the user or refer to other context files in `ai_context/`.

## For Users
- Reference this file when adding a new problem or instructing an AI assistant.
- Update this file if your workflow or conventions change.

## Code Generation and Linter Requirements

All code generation for new problems must follow the linter and style requirements described in [ai_context/code_generation.md](code_generation.md). 
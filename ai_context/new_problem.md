# Adding a New Problem

This file describes the step-by-step process for adding a new coding problem to this project, whether you are a user or an AI assistant.

## Steps
1. **Run the Script:**
   - Use `scripts/add_challenge.sh <problem_name>` to generate the initial directory and files for the new problem.
2. **Update `solution.py`:**
   - Add both a user solution and a canonical solution.
   - Use descriptive function names and include docstrings for all methods.
   - Use snake_case for all function arguments and variable names.
3. **Update `test_solution.py`:**
   - Always write out the full test file upon problem creation.
   - Use `pytest.mark.parametrize` to define multiple test cases.
   - Ensure both user and canonical solutions are tested in all cases.
   - Import from `.solution` (e.g., `from .solution import ...`).
   - Do not ask the user if you should write out the test file—this is always required.
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

After generating README.md and solution.py for a new problem, the AI or script should always automatically generate test_solution.py (with parameterized test cases for both user and canonical solutions) and EXPLANATION.md (detailed explanation, if requested) for the problem, without asking the user for confirmation. This is the default workflow for all new problems.

## Duplicate Problem Detection

Before generating a new problem, the AI or script must check if the problem already exists in the codebase. This must be done by:
- Scanning the `challenges/` directory and all its subdirectories for existing problems (by canonical name, LeetCode number, or alternates).
- Checking `tags.md` for an entry with the same LeetCode number or canonical name.
- If a duplicate is found, the AI should NOT create a new problem and should report the existing location to the user.

**CRITICAL:** The AI must perform this check BEFORE running any generation commands. If a duplicate is found, the AI should:
1. Stop immediately and report the existing location
2. NOT overwrite or modify existing files
3. Ask the user to provide a different problem name or confirm they want to proceed

**Example:**
> The problem "valid parentheses" (LeetCode #20) already exists in: challenges/stacks/valid_parentheses
> Please provide a different problem name or confirm you want to proceed.

If the user still wants to proceed, they must confirm or provide a new name.

## Directory/Category Selection

When generating a new LeetCode problem, the AI or script must always place the problem in the most canonical topic subdirectory of `challenges/` (e.g., `arrays`, `graphs`, `intervals`, etc.).
- Do not create new problems at the top level of `challenges/`.
- If the problem fits multiple topics, pick the most relevant one.

## For AI Assistants
- Follow these steps exactly when generating or updating a problem.
- Always write out docstrings for all solution methods and the full test file with parameterized test cases for both user and canonical solutions.
- If the user requests an explanation, generate it immediately as part of the workflow.
- If you are unsure about a step, ask the user or refer to other context files in `ai_context/`.

## For Users
- Reference this file when adding a new problem or instructing an AI assistant.
- Update this file if your workflow or conventions change.

## Code Generation and Linter Requirements

All code generation for new problems must follow the linter and style requirements described in [ai_context/code_generation.md](code_generation.md).

## Test File Requirements

When generating a new problem, always:

- Create a test file that stubs out tests for both the user and canonical solution.
- In each test, after calling the solution, check if the result is None. If so, skip the assertion (or use continue in a loop). This ensures that unimplemented (stub) solutions will not cause test failures in CI.
- Use relative imports (from .solution import ...).
- Only fail a test if the function is implemented and returns an incorrect result.
- This allows you to check in many new problems/tests at once, and CI will only fail if an implementation is incorrect, not if it is missing.

### Testing Multiple Methods

If there are multiple methods to test (e.g., multiple user/canonical implementations, different algorithms), collect them in a global variable and use a helper method to iterate through them. This reduces code duplication and makes tests more maintainable.

Example pattern:

```python
from .solution import (
    method1_user,
    method1_canonical,
    method2_user,
    method2_canonical
)

# List of all methods to test
ALL_METHODS = [
    method1_user,
    method1_canonical,
    method2_user,
    method2_canonical
]

def assert_all_methods(input_data, expected):
    """Helper function to test all methods with the same inputs."""
    for method in ALL_METHODS:
        result = method(input_data)
        if result is None:
            continue  # Not implemented yet
        assert result == expected, f"Method {method.__name__} failed"

def test_example():
    input_data = None
    expected = None
    assert_all_methods(input_data, expected)
```

This pattern is especially useful for problems with multiple solution approaches (e.g., top-down vs bottom-up DP, different algorithms, etc.). 
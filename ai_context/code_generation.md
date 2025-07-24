# Code Generation Policy

## Linter and Style Requirements

- All generated Python code (including stubs, tests, explanations, scripts, comments, and docstrings) must comply with flake8 linter requirements, especially:
  - Line length must not exceed 80 characters.
- The AI should automatically fix any linter errors in generated code before presenting or committing it, without asking the user for confirmation.
- All variable names, function names, and code snippets in generated explanations and documentation should be rendered in monospaced/code style (using backticks in markdown).

## Application
- This policy applies to all code generated for new problems, solutions, tests, explanations, and project scripts.
- Reference this file from any workflow or context file that involves code generation. 
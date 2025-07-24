# Code Generation Policy

## Linter and Style Requirements

- All generated Python code (including stubs, tests, and explanations) must comply with flake8 linter requirements, especially:
  - Line length must not exceed 80 characters.
- The AI should automatically fix any linter errors in generated code before presenting or committing it, without asking the user for confirmation.

## Application
- This policy applies to all code generated for new problems, solutions, tests, and explanations.
- Reference this file from any workflow or context file that involves code generation. 
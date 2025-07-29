# Troubleshooting AI-Assisted Workflows

This file lists common issues and troubleshooting steps for using AI tools (Cursor, Copilot, ChatGPT, etc.) with this project.

## Common Issues

### 1. AI Ignores Conventions or Context Files
- **Solution:**
  - Explicitly reference the relevant context file in your prompt (e.g., "Follow ai_context/new_problem.md").
  - Remind the AI to check `ai_context/` before starting a workflow.

### 2. Directory or File Naming is Inconsistent
- **Solution:**
  - Check `ai_context/tagging_and_readme.md` for naming conventions.
  - Rename files/directories to use snake_case and match topic directories.

### 3. Tags or README Format is Incorrect
- **Solution:**
  - Review the rules in `ai_context/tagging_and_readme.md`.
  - Update the README and `tags.md` to match the conventions.

### 4. Linter or Test Failures
- **Solution:**
  - Run the linter (e.g., `flake8`) and all tests before committing.
  - Fix any issues according to the conventions in `ai_context/tagging_and_readme.md`.

### 5. AI Gets Stuck or Asks for Clarification
- **Solution:**
  - Provide more explicit instructions or update the relevant context file.
  - If the workflow changes, update the context files so the AI can follow the new process.

### 6. Script Errors or Outdated Scripts
- **Solution:**
  - Check `ai_context/scripts_usage.md` for the latest script usage.
  - Update scripts or this file if workflows change.

### 7. Linting Errors in Generated Files
- **Common Issues:**
  - W293: Blank line contains whitespace
  - W291: Trailing whitespace
  - W292: No newline at end of file
  - E501: Line too long (over 80 characters)
- **Solution:**
  - Always run `make lint` after generating files
  - Use `sed -i 's/[[:space:]]*$//' filename` to remove trailing whitespace
  - Ensure files end with exactly one newline character
  - Manually verify line lengths before presenting code

### 8. Import Errors in Test Files
- **Common Issue:** `ImportError: attempted relative import with no known parent package`
- **Solution:**
  - Always create an empty `__init__.py` file in the problem directory
  - Ensure the directory structure is a proper Python package
  - Use relative imports (`from .solution import ...`) in test files

### 9. File Formatting Issues
- **Common Issues:**
  - Trailing whitespace on lines
  - Missing newline at end of file
  - Spaces in blank lines
- **Solution:**
  - Use proper text editors or tools to ensure clean formatting
  - Run `make lint` and fix all errors before presenting code
  - Follow the formatting requirements in `ai_context/code_generation.md`

## For AI Assistants
- If you encounter an issue not listed here, ask the user for clarification or suggest updating this file.

## For Users
- Update this file as new issues or solutions are discovered.
- Reference this file when troubleshooting AI-assisted workflows. 
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

## For AI Assistants
- If you encounter an issue not listed here, ask the user for clarification or suggest updating this file.

## For Users
- Update this file as new issues or solutions are discovered.
- Reference this file when troubleshooting AI-assisted workflows. 
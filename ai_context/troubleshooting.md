# Troubleshooting AI-Assisted Workflows

This file lists common issues and troubleshooting steps for using AI tools (Cursor, Copilot, ChatGPT, etc.) with this project.

## Debugging and Problem-Solving Methodology

### CRITICAL: Methodical Approach to Fixes

**Before making ANY changes, follow this order:**

1. **Investigate First**
   - Read the actual file content using `read_file`
   - Use `grep` to find exact patterns: `grep -n "pattern" file.md`
   - Check the specific lines causing issues
   - Don't assume what the problem is

2. **Identify the Real Problem**
   - Look at error messages carefully
   - Understand what's actually broken vs. what you think is broken
   - Check if the issue is already fixed or doesn't exist

3. **Make Targeted Changes**
   - Fix one issue completely before moving to the next
   - Use `sed` for precise line replacements when `search_replace` fails
   - Make minimal, specific changes rather than broad attempts

4. **Verify Immediately**
   - Run `make quality` after each change
   - Check if the change actually happened
   - Don't repeat failed attempts - try a different approach

### Common Debugging Patterns

**For LaTeX/Markdown Issues:**
```bash
# Find exact content
grep -n "pattern" file.md

# Check specific lines
read_file target_file.md start_line_one_indexed X end_line_one_indexed Y

# Use sed for precise replacement
sed -i 'line_number s/old/new/' file.md
```

**For Code Issues:**
```bash
# Run quality checks first
make quality

# Check specific errors
make lint
make test
```

### Anti-Patterns to Avoid

**❌ DON'T:**
- Make multiple failed `search_replace` attempts without investigating
- Assume what the problem is without reading the file
- Try to fix things that aren't broken
- Make broad changes when specific ones are needed

**✅ DO:**
- Investigate thoroughly before making changes
- Use the right tools for the job (`grep`, `sed`, `read_file`)
- Make targeted, verified changes
- Run quality checks after each change

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

### 10. Incorrect Test Cases
- **Common Issues:**
  - Test cases with multiple valid solutions when problem guarantees uniqueness
  - Expected outputs that don't match manual calculations
  - Test cases that violate problem constraints
  - Comments that don't match expected behavior
- **Solution:**
  - **CRITICAL: Manually verify each test case by calculating the expected result**
  - **CRITICAL: Check that test cases respect all problem constraints**
  - **CRITICAL: Ensure test cases match problem guarantees (e.g., "exactly one solution")**
  - **CRITICAL: Verify comments accurately describe the test case**
  - **CRITICAL: Test edge cases that actually test boundary conditions**
- **Validation Process:**
  1. Read the problem statement carefully
  2. Identify all constraints and guarantees
  3. For each test case, manually calculate the expected result
  4. Verify the calculation matches the expected output
  5. Check that the test case doesn't violate any constraints
  6. Ensure comments accurately describe the test

## For AI Assistants
- If you encounter an issue not listed here, ask the user for clarification or suggest updating this file.

## For Users
- Update this file as new issues or solutions are discovered.
- Reference this file when troubleshooting AI-assisted workflows. 
# AI Prompt Examples

This file contains example prompts for using AI tools (Cursor, Copilot, ChatGPT, etc.) with this project. Use these as templates to get consistent, high-quality results.

## General Guidance
- Reference the relevant context file in your prompt (e.g., "Follow the steps in ai_context/new_problem.md").
- Be explicit about the workflow or convention you want the AI to follow.
- If you want to automate a multi-step process, ask the AI to follow the context files step by step.
- **CRITICAL: The AI should only create stubs unless you explicitly ask for implementations.**

## Example Prompts

### Adding a New Problem
```
Please add a new problem called 'maximum_product_subarray'.
Follow the steps in ai_context/new_problem.md and use the conventions in ai_context/tagging_and_readme.md.
```

### Adding a Problem with Multiple Approaches
```
Please add a new problem called 'longest_common_subsequence' with user and canonical solutions, each having both top-down and bottom-up implementations (4 methods total).
Follow the steps in ai_context/new_problem.md and use the conventions in ai_context/tagging_and_readme.md.
```

### Updating Tags
```
Regenerate the tags.md file by reading all problem READMEs and following the rules in ai_context/tagging_and_readme.md.
```

### Linting and Testing
```
Run the linter and all tests for the problem in arrays/maximum_subarray. Fix any issues according to the conventions in ai_context/tagging_and_readme.md.
```

### Custom Workflow
```
I want to add a new dynamic programming problem and have it fully tagged, tested, and documented. Please follow all steps in ai_context/new_problem.md and ai_context/tagging_and_readme.md.
```

### Adding a Likely Interview Problem from Grokking CSV (Optional)
```
Please add a new LeetCode problem, likely to be asked in an interview, from the grokking CSV. Follow all project conventions, place it in the canonical directory, and (optionally) generate a detailed EXPLANATION.md if I request it.
```
- Use this workflow when you want to practice with high-value interview problems from curated lists.
- If you want an explanation, specify it in your prompt (e.g., "with an explanation").
- This is an optional workflow and not the default for all new problems.
- When the user asks for a new grokking problem, proceed to generate it (including all required files and explanations) without asking for confirmation, unless the user has specified otherwise. Do not prompt the user to say yes or no—just generate the problem.
- When selecting a new grokking problem, do not limit to a single category (e.g., intervals). Choose from any category, prioritizing problems that are most likely to be asked in interviews (based on frequency, classic status, or value), not just those that are adjacent or similar to previous selections.
- **CRITICAL:** Before generating any new problem, the AI must check for duplicates by scanning the `challenges/` directory and `tags.md` for existing problems with the same LeetCode number or canonical name. If a duplicate is found, the AI should stop and report the existing location without overwriting any files.

## For AI Assistants
- Always check for a relevant context file before starting a workflow.
- If the user does not specify a file, ask if there is a context file you should follow.
- **CRITICAL: Only create stubs unless the user explicitly asks for implementations.**
- **CRITICAL: Before presenting any code, manually verify all lines respect the 80-character limit. This applies to function signatures, docstrings, and all other code.**
- **CRITICAL: Always place problems in their canonical topic directory (e.g., dynamic programming problems in `dynamic_programming/`).**
- **CRITICAL: When updating tags.md, verify the exact directory path by checking the filesystem, including the topic directory.**
- **CRITICAL: Always run `make lint` before presenting code to catch W293, E261, and other common errors.**
- **CRITICAL: ALWAYS check for W293 (blank line contains whitespace) before presenting code. This is the SECOND MOST COMMON ERROR. Remove any spaces/tabs from blank lines.**
- **CRITICAL: ALWAYS ensure files end with a newline (W292) and have no trailing whitespace (W291).**
- **CRITICAL: Always create an empty `__init__.py` file in the problem directory for proper Python package structure.**
- **CRITICAL: After creating files, run `make lint` and fix any errors before presenting the final code.**
- **CRITICAL: The add_challenge.sh script creates directories at the root level. You MUST move them to the correct topic directory immediately.**
- **CRITICAL: NEVER leave problems at the root level of challenges/ - always place them in their canonical topic subdirectory.**
- **CRITICAL: When summarizing problems in chat, do NOT mention the solution technique (e.g., "two pointers", "sliding window", "dynamic programming"). Focus on problem characteristics, difficulty, and interview value without revealing the algorithm approach.**
- **CRITICAL: The goal is to preserve independent problem-solving experience. Let users discover the solution technique themselves.**
- **CRITICAL: All test cases must exactly match problem constraints and guarantees. Verify that inputs produce expected outputs according to problem rules.**
- **CRITICAL: Double-check test case comments accurately describe expected behavior.**
- **CRITICAL: For each test case, manually calculate the expected result to ensure correctness.**
- **CRITICAL: Verify test cases don't have multiple valid solutions when the problem guarantees uniqueness.**
- **CRITICAL: Ensure test cases respect all problem constraints (array size, value ranges, etc.).**
- **CRITICAL: When implementing solutions, maintain existing docstring format or use format that passes docformatter.**
- **CRITICAL: Run `make format` after implementing solutions to catch formatting issues.**
- **CRITICAL: Use README header format "LeetCode #123: Problem Title" - do NOT use "LeetCode Problem:" after the number.**
- **CRITICAL: Do NOT mention mathematical properties in README explanations (e.g., "squaring preserves order", "monotonic operation").**
- **CRITICAL: Do NOT reveal solution techniques in example explanations or Notes section.**
- **CRITICAL: Focus on problem characteristics, not solution approaches in READMEs.**
- If you are unsure about a step, ask the user or refer to the context files in this directory.

## For Users
- Use these example prompts to get the most out of AI tools.
- Update this file with new prompt examples as your workflows evolve. 
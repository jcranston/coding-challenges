# Using the Problem Status Utility via AI

## Purpose
This context file instructs the AI on how to use the `scripts/problem_status.py` utility to answer user questions about the status of coding problems (implemented, unimplemented, missing explanations, etc.).

## How the AI Should Behave
- When a user asks about the status of problems (e.g., which are unimplemented, which are missing explanations, etc.), the AI should:
  1. Parse the user's intent (e.g., unimplemented, missing explanation, etc.).
  2. Call the script with the appropriate flag(s) (see below).
  3. Return the output to the user in a readable format, optionally summarizing or suggesting next steps.
- The AI should not attempt to parse the codebase directly for this information; always use the script for accuracy and consistency.

## Example Prompts and AI Actions

| User Prompt Example                                 | AI Action                                      |
|-----------------------------------------------------|------------------------------------------------|
| "List unimplemented problems"                       | Run `python scripts/problem_status.py --unimplemented` |
| "Which problems have explanations?"                 | Run `python scripts/problem_status.py --has-explanation` |
| "Show me a summary of all problem statuses"         | Run `python scripts/problem_status.py --all`   |
| "Which problems are missing EXPLANATION.md?"        | Run `python scripts/problem_status.py --missing-explanation` |
| "List implemented problems"                         | Run `python scripts/problem_status.py --implemented` |

## Notes
- The script is located at `scripts/problem_status.py` and should be run from the project root.
- The AI should present the results clearly, and may offer to help with next steps (e.g., "Would you like to generate an explanation for one of these problems?").
- If the user asks for a custom filter or summary, the AI should use the closest matching script flag(s) and explain any limitations. 
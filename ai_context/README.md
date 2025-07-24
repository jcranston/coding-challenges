# AI Context & Workflow Guidance

This directory contains guidance, templates, and prompt context files for using AI (e.g., Cursor, Copilot, ChatGPT) to automate and standardize workflows in this codebase.

## Purpose
- **Consistency:** Ensure all new problems, scripts, and documentation follow the same conventions.
- **AI Assistance:** Provide clear, up-to-date instructions for AI tools to follow your preferred workflows.
- **Onboarding:** Help new contributors or future-you quickly understand how to use AI effectively in this project.

## How to Use These Files
- **For Users:**
  - Before starting a new workflow (e.g., adding a new problem, updating tags), read the relevant markdown file in this directory.
  - Follow the step-by-step instructions and conventions described.
  - When using AI (Cursor, Copilot, etc.), reference these files in your prompt. For example:
    - "Follow the steps in ai_context/new_problem.md."
    - "Use the conventions in ai_context/tagging_and_readme.md."
    - "For LeetCode problems, see ai_context/leetcode_problem_mapping.md."
- **For AI Tools:**
  - When asked to automate or assist with a workflow, read the relevant context file(s) in this directory.
  - Adhere to the conventions, naming, and formatting rules described.
  - If unsure, ask the user to clarify or update the context file.
  - Always check for a relevant context file before starting a workflow.

## Files in This Directory
- `new_problem.md`: How to add a new problem (script, README, solution, tests, tags, etc.)
- `leetcode_problem_mapping.md`: How to add LeetCode problems by number or name, with canonical mapping and README formatting rules. Use this for any LeetCode-sourced problem. This file supplements `new_problem.md`.
- `tagging_and_readme.md`: Rules for tags, README format, and directory structure.
- `scripts_usage.md`: How and when to use project scripts.
- `ai_prompt_examples.md`: Example prompts for AI tools to use.
- `troubleshooting.md`: Common issues and how to resolve them.
- `explanation_generation.md`: How to generate detailed explanations for problems.
- `problem_status_prompt.md`: How the AI should use the problem status utility script.

Feel free to add or update files as your workflow evolves! 
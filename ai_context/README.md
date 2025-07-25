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

## Problem Sources Directory
- The `problem_sources/` directory (at the project root) is used to store CSVs, lists, or other files containing possible problems to generate or select from (e.g., curated LeetCode lists, Grokking lists).
- This directory is for reference and curation. You can ask the AI to pick a problem from a file in this directory, or use it to track problem pools for future coding challenges.
- Scripts and automation may not read from this directory by default, but it serves as a central place for problem source files.

## Picking Likely Interview Problems from a Source List
- If you ask the AI to "pick a likely interview problem from the grokking csv" (or similar), the AI should:
  - Select a problem from the relevant CSV in `problem_sources/` that has **not already been generated as a challenge in the project** (i.e., not present in the `challenges/` directory).
  - Prioritize problems that are most likely to be asked in interviews (e.g., based on frequency, classic status, or difficulty if known).
  - The AI should not pick a problem that is already implemented in the project.
- You can use this workflow to have the AI suggest new, high-value problems for practice or challenge generation.

Feel free to add or update files as your workflow evolves! 
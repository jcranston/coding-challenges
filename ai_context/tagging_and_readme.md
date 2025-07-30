# Tagging, README, and Directory Conventions

This file describes the conventions for tagging, README formatting, and directory structure in this project. Follow these rules for every new problem or when updating existing ones.

## Tagging
- Use LeetCode's official tags as the primary source.
- Supplement with additional tags if relevant (e.g., 'prefix sum', 'monotonic stack').
- Add all tags to the top of the README and to `tags.md`.
- Format: `**Tags:** array, hash table, sliding window`
- If a problem does not have a direct LeetCode number, leave the number blank in `tags.md`.

## README Format
- Every problem README should start with:
  - LeetCode number and title (if applicable): `**LeetCode #123: Problem Title**`
  - Tags: `**Tags:** ...`
  - Problem title as a markdown header (e.g., `# Two Sum`)
- **CRITICAL: Use format "LeetCode #123: Problem Title" - do NOT use "LeetCode Problem:" after the number.**
- Use the following sections:
  - Problem
  - Examples
  - Constraints
  - Clarifications & Assumptions
  - Notes
- **CRITICAL: Do NOT include an "Approach" section that reveals the solution method.**
- **CRITICAL: The goal is interview preparation - allow independent problem-solving practice.**
- **CRITICAL: Save detailed solution explanations for EXPLANATION.md files (only when explicitly requested).**
- **CRITICAL: The "Notes" section should provide subtle hints without revealing algorithms (e.g., "Think about how to efficiently..." rather than "Use a hash map to...").**
- Use clean, basic markdown formatting for readability.

## Directory Structure
- Place each problem in the most canonical topic directory (e.g., `arrays`, `graphs`, `dynamic_programming`).
- If a problem fits multiple topics, pick the most relevant one for the directory, but include all relevant tags.
- Use snake_case for all directory and file names.
- Each problem should have its own directory containing:
  - `solution.py`
  - `test_solution.py`
  - `README.md`
  - `__init__.py` (if needed for imports)

## For AI Assistants
- Always follow these conventions when generating or updating problems.
- If unsure about a tag or format, ask the user or refer to this file.

## For Users
- Reference this file when reviewing or updating problems.
- Update this file if your conventions change. 
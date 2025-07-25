# LeetCode Problem Mapping and Addition

## Purpose
This file defines the workflow and rules for adding LeetCode problems by number or by (possibly non-canonical) name, and for ensuring correct mapping, naming, and README formatting. It supplements the general new problem workflow described in `ai_context/new_problem.md`.

## Workflow Overview
- Users can request to add problems by LeetCode number (e.g., 217) or by name (e.g., "contains duplicate").
- The AI/script should map user-supplied names to the correct LeetCode problem number and canonical name, even if the name is not exact (e.g., "triplet sum to zero" → LeetCode 15, "3Sum").
- The directory name for the problem can be either the canonical LeetCode name or the user-supplied name (flexible).
- The README.md for each problem must include, at the very top:
  1. The LeetCode problem number (e.g., `LeetCode #15`)
  2. The canonical LeetCode problem name (e.g., `3Sum`)
  3. The user-supplied title as the main title (e.g., `# Triplet Sum to Zero`)
- All other problem creation steps (stubbing files, directory structure, etc.) should follow the rules in `ai_context/new_problem.md`.

## Example README.md Format
```
LeetCode #15
LeetCode Problem: 3Sum

# Triplet Sum to Zero

(Problem description...)
```

## Example User Prompts and AI Actions
| User Prompt | AI/Script Action |
|-------------|------------------|
| "Add leetcode problems 217, 1832, and 345" | Look up canonical names, generate stubs, README includes number/name |
| "Add problems 'contains duplicate', 'pangram', 'reverse vowels'" | Map to LeetCode numbers/names, generate stubs, README includes both |
| "Add problem 'triplet sum to zero'" | Map to LeetCode #15, canonical name '3Sum', README as above |

## Mapping Logic
- The AI/script should use a mapping table, LeetCode API, or web search to resolve user-supplied names to the correct LeetCode problem number and canonical name.
- If a name is ambiguous or not found, the AI should ask the user for clarification or suggest possible matches.

## Directory Naming and Placement
- The directory name can be either the canonical LeetCode name (e.g., `3sum`) or the user-supplied name (e.g., `triplet_sum_to_zero`).
- Consistency is preferred, but flexibility is allowed as long as the README includes the canonical mapping.
- **The problem directory must be placed in the most canonical topic subdirectory of `challenges/`, based on LeetCode's primary category for the problem (e.g., `binary_search`, `arrays`, `graphs`).**
- If a problem fits multiple topics, always use LeetCode's primary category for directory placement, and include all relevant tags (including secondary topics) in the README and `tags.md`.
- Do not place problems in a secondary or less canonical directory just because they have multiple tags; always use the primary category for the directory.

## Duplicate Detection

Before adding a LeetCode problem, the AI or script must check for existing problems using the duplicate detection workflow described in [ai_context/new_problem.md](new_problem.md). If a duplicate is found, the user should be warned and the existing directory listed, rather than creating a duplicate.

## Reference
- For the actual steps to create the problem directory and stub files, see `ai_context/new_problem.md`. 
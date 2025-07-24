# Problem Lookup: Checking for Existing Problems

## Purpose
This file describes how to check if a problem (by LeetCode number, canonical name, or alternate/user-supplied name) already exists in the codebase. Use these checks before generating a new problem to avoid duplicates.

## When to Use
- When a user asks, "Have we done this problem yet?"
- Before generating a new problem (by name or LeetCode number)
- When searching for similar or related problems

## How to Check for Existing Problems

### 1. Search by LeetCode Number in README files
```sh
find challenges/ -type f -name README.md -exec grep -H 'LeetCode' {} \; | grep -i <number>
```
**Example:**
```sh
find challenges/ -type f -name README.md -exec grep -H 'LeetCode' {} \; | grep -i 15
```

### 2. Search by Canonical LeetCode Name in README files
```sh
find challenges/ -type f -name README.md -exec grep -Hi '<canonical_name>' {} \;
```
**Example:**
```sh
find challenges/ -type f -name README.md -exec grep -Hi '3sum' {} \;
```

### 3. Search by Alternate/User-Supplied Name in Directory Names
```sh
find challenges/ -type d -iname '*<name>*'
```
**Examples:**
```sh
find challenges/ -type d -iname '*3sum*'
find challenges/ -type d -iname '*triplet*'
```

### 4. Search by Alternate/User-Supplied Name in README files
```sh
find challenges/ -type f -name README.md -exec grep -Hi '<alternate_name>' {} \;
```

## How to Interpret Results
- If any command returns a result, the problem (or a very similar one) likely already exists.
- The output will show the path to the directory or README file where the problem is found.
- If no results are found, the problem likely does not exist in the codebase.

## AI Guidance
- The AI should use these checks (or equivalent logic) before generating a new problem.
- The AI should always perform all necessary lookup/search commands itself and report the results, rather than asking the user to run commands or provide additional input. This should be the default workflow for problem lookup and duplicate detection.
- If a match is found, warn the user and list the directory where the problem exists.
- If no match is found, proceed with problem generation.

## Example User Prompts
- "Have we done LeetCode problem 15?"
- "Is there a problem called 'triplet sum to zero'?"
- "Do we already have 'contains duplicate' implemented?"

## See Also
- [ai_context/new_problem.md](new_problem.md) (for duplicate detection in problem creation)
- [ai_context/leetcode_problem_mapping.md](leetcode_problem_mapping.md) 
# Generating EXPLANATION.md for Coding Problems

## When to Generate
- Only generate `EXPLANATION.md` when explicitly requested by the user.
- Do not create a blank or placeholder `EXPLANATION.md` during problem generation.
- Explanations can be generated for any problem, regardless of whether the canonical solution is implemented.

## What to Include in EXPLANATION.md
- **High-level approach:** Clearly describe the main idea and strategy for solving the problem.
- **Step-by-step breakdown:** Explain the algorithm in detail, referencing indices, invariants, and key conditions (e.g., why `<` is used instead of `<=`).
- **Annotated code:** If a canonical solution exists, reference and annotate it. If not, describe the expected approach in detail.
- **Test cases:** Reference the provided test cases to illustrate edge cases and reasoning.
- **Common pitfalls:** Discuss mistakes or misconceptions that often arise with this problem.
- **Variations:** Briefly mention how the problem or its solution might change under different constraints.
- **Relevant literature:** Whenever possible, cite classic papers, well-known resources, or authoritative references related to the problem (e.g., LeetCode, CLRS, Stack Overflow, academic papers). Include links or citations for further reading.

## Important Notes
- Generating an explanation does **not** mean implementing the canonical solution. Only describe or reference the solution if it exists.
- The explanation should be as detailed and educational as possible, helping the user understand not just how, but why the solution works.
- Always reference all available material in the problem directory: README, test cases, and solution code (if present).

## Example Prompts
- "Generate an EXPLANATION.md for this problem, referencing the README, test cases, and any existing solution. Include citations to relevant literature."
- "Add a detailed explanation to this problem, but do not implement the canonical solution."

## Example File Structure
```
challenges/
  some_problem/
    README.md
    solution.py
    test_solution.py
    EXPLANATION.md   # <-- Only generated on request
```

## Workflow Summary
- New problems always include stubs for README.md, solution.py, and test_solution.py (with full test cases).
- EXPLANATION.md is only generated when requested, and should be comprehensive, referencing all available material and relevant literature. 
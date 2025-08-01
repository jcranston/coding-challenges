# Generating EXPLANATION.md for Coding Problems

## When to Generate
- Only generate `EXPLANATION.md` when explicitly requested by the user.
- Do not create a blank or placeholder `EXPLANATION.md` during problem generation.
- Do not automatically generate explanations when the user is asking questions to build intuition or understand concepts in chat.
- Explanations can be generated for any problem, regardless of whether the canonical solution is implemented.
- **CRITICAL: README files are for practice - they should NOT include detailed solution approaches.**
- **CRITICAL: EXPLANATION.md files are for learning - they SHOULD include detailed approaches and algorithms.**
- **CRITICAL: The distinction is important for interview preparation - READMEs allow independent problem-solving, EXPLANATION.mds provide detailed guidance.**

## What to Include in EXPLANATION.md
- **Problem Recap (first section):** Start with a brief summary of the problem in your own words, referencing the README and clarifying the main task and constraints.
- **High-level approach:** Clearly describe the main idea and strategy for solving the problem.
- **Step-by-step breakdown:** Explain the algorithm in detail, referencing indices, invariants, and key conditions (e.g., why `<` is used instead of `<=`).
- **Mathematical formulations:** Include formal mathematical definitions, recurrence relations, and complexity analysis using proper LaTeX notation (see `mathematical_formatting.md`).
- **Rigorous proofs:** For complex algorithms (especially dynamic programming, graph algorithms, optimization problems), include formal mathematical proofs of correctness, optimality, and complexity using proper theorem-proof structure.
- **Annotated code:** If a canonical solution exists, reference and annotate it. If not, describe the expected approach in detail.
- **Test cases:** Reference the provided test cases to illustrate edge cases and reasoning.
- **Common pitfalls:** Discuss mistakes or misconceptions that often arise with this problem.
- **Variations:** Briefly mention how the problem or its solution might change under different constraints.
- **Relevant literature:** Whenever possible, cite classic papers, well-known resources, or authoritative references related to the problem (e.g., LeetCode, CLRS, Stack Overflow, academic papers). Include links or citations for further reading.

## Important Notes
- Generating an explanation does **not** mean implementing the canonical solution. Only describe or reference the solution if it exists.
- The explanation should be as detailed and educational as possible, helping the user understand not just how, but why the solution works.
- Always reference all available material in the problem directory: README, test cases, and solution code (if present).
- **For simple problems, keep the explanation concise and avoid unnecessary complexity or length. Cover all required sections, but do not over-explain trivial logic.**
- **Chat discussions about building intuition should remain in chat and not automatically trigger explanation file generation.**
- **CRITICAL: Use proper LaTeX mathematical formatting for all formulas, complexity analysis, and mathematical expressions (see `mathematical_formatting.md`).**
- **CRITICAL: Include formal mathematical definitions and recurrence relations where appropriate.**
- **CRITICAL: For complex algorithms, include rigorous mathematical proofs using proper theorem-proof structure with lemmas, induction, and contradiction methods.**

## Example Prompts
- "Generate an EXPLANATION.md for this problem, referencing the README, test cases, and any existing solution. Include citations to relevant literature."
- "Add a detailed explanation to this problem, but do not implement the canonical solution."
- "I want to understand the intuition behind this problem" → Answer in chat, don't generate file
- "Can you help me build intuition for the recurrence?" → Answer in chat, don't generate file

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
- Chat discussions about problem understanding, intuition building, or concept clarification should remain in chat without generating files.

## Updating Explanations
- If the user asks for a clarification or update to an existing EXPLANATION.md, always update the relevant EXPLANATION.md file so the clarification is persisted for future reference. Do not just answer in chat—make sure the explanation file is updated accordingly. 
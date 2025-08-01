# Rigorous Proof Guidelines for EXPLANATION Files

This file provides guidelines for including formal mathematical proofs in EXPLANATION.md files for complex algorithms and problems.

## When to Include Rigorous Proofs

### Problems Requiring Proofs
- **Dynamic Programming problems** (optimal substructure, correctness of recurrence)
- **Graph algorithms** (shortest path, minimum spanning tree, network flow)
- **Optimization problems** (greedy algorithms, linear programming)
- **Complexity analysis** (time/space complexity proofs)
- **Algorithm correctness** (invariants, termination, optimality)

### Problems NOT Requiring Proofs
- **Simple array manipulations** (unless they have non-obvious correctness)
- **Basic string operations** (unless they involve complex algorithms)
- **Elementary data structure operations** (unless they have subtle correctness issues)

## Proof Structure Guidelines

### 1. Theorem Statement
Start with a clear, formal statement of what you're proving:

```markdown
**Theorem:** The dynamic programming algorithm correctly computes the minimum cost Hamiltonian cycle for the Traveling Salesman Problem.
```

### 2. Proof Organization
Organize proofs into logical parts:

```markdown
### Proof Structure
We will prove this in three parts:
1. **Optimal Substructure Property**
2. **Correctness of Recurrence Relation** 
3. **Correctness of Final Answer Computation**
```

### 3. Lemma and Theorem Format
Use proper mathematical formatting for lemmas and theorems:

```markdown
**Lemma 1:** Let $\pi^* = (v_0, v_1, \ldots, v_{n-1}, v_0)$ be an optimal TSP tour. Then for any subpath $\pi^*[i:j] = (v_i, v_{i+1}, \ldots, v_j)$, this subpath is optimal for visiting the cities $\{v_i, v_{i+1}, \ldots, v_j\}$ starting at $v_i$ and ending at $v_j$.

**Proof:** By contradiction. [proof details]
```

## Common Proof Techniques

### 1. Proof by Contradiction
Use for optimality proofs:

```markdown
**Proof:** By contradiction. Suppose [assumption]. Then [logical steps]. This contradicts [known fact]. Therefore, [conclusion].
```

### 2. Mathematical Induction
Use for recursive algorithms and dynamic programming:

```markdown
**Proof:** We prove by induction on [parameter].

**Base Case:** [prove for smallest case]

**Inductive Step:** Assume [inductive hypothesis]. Then [prove for next case using hypothesis].
```

### 3. Optimal Substructure Proofs
For dynamic programming problems:

```markdown
**Lemma:** The optimal solution contains optimal solutions to subproblems.

**Proof:** Let $S^*$ be the optimal solution. Suppose some subproblem $S'$ is not optimal. Then we can replace $S'$ with a better solution, contradicting optimality of $S^*$.
```

### 4. Invariant Proofs
For iterative algorithms:

```markdown
**Invariant:** At the start of each iteration, [invariant property].

**Initialization:** [prove invariant holds before first iteration]

**Maintenance:** [prove invariant is preserved by each iteration]

**Termination:** [prove invariant leads to correct result]
```

## Mathematical Notation for Proofs

### 1. Sets and Logic
- Use `$\in$`, `$\subseteq$`, `$\setminus$` for set operations
- Use `$\forall$`, `$\exists$`, `$\implies$`, `$\iff$` for logic
- Use `$\{...\}$` for set notation

### 2. Functions and Variables
- Use `$\texttt{dp}[S][i]$` for dynamic programming states
- Use `$f(x)$`, `$g(n)$` for generic functions
- Use `$\pi$`, `$\sigma$` for permutations/paths

### 3. Complexity Notation
- Use `$O(...)$`, `$\Omega(...)$`, `$\Theta(...)$` for complexity
- Use `$\log$`, `$\ln$` for logarithms
- Use `$\sum$`, `$\prod$` for sums and products

## Proof Examples by Problem Type

### Dynamic Programming Proofs
```markdown
**Theorem:** The recurrence relation correctly computes optimal solutions.

**Proof:** By induction on subproblem size.
- Base case: [trivial cases]
- Inductive step: [use optimal substructure]
```

### Greedy Algorithm Proofs
```markdown
**Theorem:** The greedy choice is always optimal.

**Proof:** By contradiction. Suppose greedy choice is not optimal. Then [show contradiction].
```

### Graph Algorithm Proofs
```markdown
**Theorem:** The algorithm finds the shortest path.

**Proof:** By induction on path length.
- Base case: [start vertex]
- Inductive step: [relaxation preserves optimality]
```

## Quality Standards for Proofs

### 1. Completeness
- **Cover all cases:** Don't skip edge cases
- **Address assumptions:** State and justify all assumptions
- **Handle base cases:** Don't forget trivial cases

### 2. Clarity
- **Clear structure:** Use numbered parts and lemmas
- **Logical flow:** Each step should follow from previous
- **Mathematical precision:** Use formal notation consistently

### 3. Rigor
- **No hand-waving:** Every claim must be justified
- **Formal notation:** Use proper mathematical symbols
- **Complete arguments:** Don't skip steps

### 4. Educational Value
- **Explain intuition:** Why does the proof work?
- **Connect to algorithm:** How does the proof relate to implementation?
- **Highlight key insights:** What are the crucial observations?

## Common Proof Patterns

### 1. Optimal Substructure (Dynamic Programming)
```markdown
**Lemma:** Optimal solutions contain optimal solutions to subproblems.

**Proof:** By contradiction. If not, we could improve the solution by replacing a suboptimal subproblem with an optimal one.
```

### 2. Greedy Choice Property
```markdown
**Lemma:** The greedy choice is always part of some optimal solution.

**Proof:** Show that any optimal solution can be modified to include the greedy choice without increasing cost.
```

### 3. Monotonicity/Invariant
```markdown
**Lemma:** The invariant is maintained throughout the algorithm.

**Proof:** By induction on iterations. Show that each step preserves the invariant.
```

### 4. Complexity Analysis
```markdown
**Theorem:** The algorithm has time complexity $O(f(n))$.

**Proof:** 
- Count the number of operations
- Show each operation takes $O(g(n))$ time
- Total: $O(f(n)) \times O(g(n)) = O(f(n) \times g(n))$
```

## Integration with Mathematical Formatting

### 1. Use LaTeX for All Mathematical Content
- Variables: `$n$`, `$i$`, `$j$`
- Functions: `$\texttt{dp}[S][i]$`, `$f(x)$`
- Operators: `$\min$`, `$\max$`, `$\sum$`
- Relations: `$\leq$`, `$\geq$`, `$\in$`

### 2. Block Equations for Complex Formulas
```markdown
$$\texttt{dp}[S][i] = \min_{j \in S \setminus \{i\}} \left( \texttt{dp}[S \setminus \{i\}][j] + d(j,i) \right)$$
```

### 3. Inline Math for Simple Expressions
```markdown
The cost is $c(\pi) = \sum_{i=0}^{n-1} d(v_i, v_{i+1})$.
```

## Checklist for Rigorous Proofs

Before finalizing any proof section:

- [ ] **Clear theorem statement** with formal mathematical notation
- [ ] **Logical proof structure** with numbered parts/lemmas
- [ ] **Complete coverage** of all cases and edge cases
- [ ] **Proper mathematical notation** using LaTeX formatting
- [ ] **Educational value** - explains why the proof works
- [ ] **Connection to algorithm** - shows how proof relates to implementation
- [ ] **No logical gaps** - every step is justified
- [ ] **Appropriate level of detail** - not too verbose, not too terse

## Implementation Notes

- **Proofs should be educational:** Help readers understand why algorithms work
- **Use standard proof techniques:** Contradiction, induction, invariants
- **Maintain mathematical rigor:** No hand-waving or informal arguments
- **Connect to implementation:** Show how proofs relate to actual code
- **Include complexity proofs:** Prove time and space complexity bounds
- **Reference literature:** Cite relevant papers or textbooks when appropriate 
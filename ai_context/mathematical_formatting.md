# Mathematical Formatting Guidelines

This file provides guidelines for formatting mathematical expressions, formulas, and code snippets in README and EXPLANATION files using LaTeX-style notation.

## LaTeX Math Formatting Rules

### 1. Inline Mathematical Expressions
Use single dollar signs `$...$` for inline mathematical expressions:

**✅ Correct Examples:**
- Variables: `$n$`, `$i$`, `$j$`, `$k$`
- Functions: `$f(x)$`, `$d(i,j)$`, `$\texttt{dp}[S][i]$`
- Operators: `$\min$`, `$\max$`, `$\sum$`, `$\prod$`
- Relations: `$\in$`, `$\subseteq$`, `$\leq$`, `$\geq$`
- Sets: `$V = \{0, 1, 2, \ldots, n-1\}$`

**❌ Incorrect Examples:**
- Plain text: `n`, `i`, `j` (should be `$n$`, `$i$`, `$j$`)
- Unformatted functions: `dp[S][i]` (should be `$\texttt{dp}[S][i]$`)

### 2. Block Mathematical Equations
Use double dollar signs `$$...$$` for standalone equations:

**✅ Correct Examples:**
```markdown
$$\texttt{dp}[S][i] = \min_{j \in S \setminus \{i\}} \left( \texttt{dp}[S \setminus \{i\}][j] + d(j,i) \right)$$

$$\min_{i \in V} \left( \texttt{dp}[V][i] + d(i,0) \right)$$
```

**❌ Incorrect Examples:**
- Mixing inline and block: `$$...$$ for all $j$` (should be separate lines)
- Unescaped special characters: `dp[S][i]` (should be `$\texttt{dp}[S][i]$`)

### 3. Code Snippets in Mathematical Context
Use `\texttt{...}` for code variables and functions within math:

**✅ Correct Examples:**
- `$\texttt{dp}[mask][pos]$`
- `$\texttt{full\_mask} = (1 \ll n) - 1$`
- `$\texttt{MST}(G)$`
- `$\texttt{cost}(\texttt{tour})$`

**❌ Incorrect Examples:**
- `$dp[mask][pos]$` (missing `\texttt{}`)
- `$full_mask$` (should be `$\texttt{full\_mask}$`)

### 4. Common Mathematical Symbols

**Sets and Logic:**
- `$\in$` (element of)
- `$\subseteq$` (subset)
- `$\setminus$` (set difference)
- `$\{...\}$` (set notation)
- `$\ldots$` (ellipsis)

**Operators:**
- `$\min$`, `$\max$` (minimum, maximum)
- `$\sum$`, `$\prod$` (sum, product)
- `$\leq$`, `$\geq$` (less/greater than or equal)
- `$\neq$` (not equal)

**Functions and Variables:**
- `$\texttt{dp}[S][i]$` (dynamic programming state)
- `$d(i,j)$` (distance function)
- `$f(x)$` (generic function)
- `$\pi$` (permutation)

### 5. Complexity Notation
Always use LaTeX formatting for complexity analysis:

**✅ Correct Examples:**
- `$O(n^2 \times 2^n)$`
- `$O(n \log n)$`
- `$O(1)$` space complexity
- `$\Theta(n^2)$` time complexity

**❌ Incorrect Examples:**
- `O(n² × 2ⁿ)` (should be `$O(n^2 \times 2^n)$`)
- `O(n log n)` (should be `$O(n \log n)$`)

### 6. Recurrence Relations
Format recurrence relations with proper LaTeX:

**✅ Correct Examples:**
```markdown
$$\texttt{dp}[i] = \max(\texttt{dp}[i-1] + \texttt{nums}[i], \texttt{nums}[i])$$

$$F(n) = F(n-1) + F(n-2)$$
```

### 7. Algorithm Pseudocode
When describing algorithms mathematically:

**✅ Correct Examples:**
```markdown
**Mathematical Formulation:**
For each state $(S, i)$, we try all possible previous cities:

$$\texttt{dp}[S][i] = \min_{j \in S \setminus \{i\}} \left( \texttt{dp}[S \setminus \{i\}][j] + d(j,i) \right)$$

**Implementation:**
```python
dp[mask][pos] = min(dp[mask - (1 << pos)][prev] + distances[prev][pos])
```
```

### 8. README vs EXPLANATION Formatting

**README Files:**
- Use minimal mathematical notation
- Focus on problem description, not solution details
- Avoid complex formulas unless essential for problem understanding
- Keep mathematical expressions simple and clear

**EXPLANATION Files:**
- Use comprehensive LaTeX formatting
- Include detailed mathematical formulations
- Provide formal definitions and proofs
- Use block equations for complex formulas
- Include complexity analysis with proper notation

### 9. Common Mistakes to Avoid

1. **Mixing inline and block math on same line:**
   ```markdown
   ❌ $$\min_{i,j} d(i,j)$$ for all $i,j$
   ✅ $$\min_{i,j} d(i,j)$$
        for all $i,j$.
   ```

2. **Unescaped underscores in code:**
   ```markdown
   ❌ $\texttt{full_mask}$
   ✅ $\texttt{full\_mask}$
   ```

3. **Missing \texttt{} for code variables:**
   ```markdown
   ❌ $dp[S][i]$
   ✅ $\texttt{dp}[S][i]$
   ```

4. **Inconsistent complexity notation:**
   ```markdown
   ❌ O(n² × 2ⁿ)
   ✅ $O(n^2 \times 2^n)$
   ```

### 10. Quality Checklist

Before finalizing any README or EXPLANATION file with mathematical content:

- [ ] All variables are formatted with `$...$`
- [ ] All functions use `$\texttt{...}$` for code variables
- [ ] Block equations use `$$...$$` and are on separate lines
- [ ] Complexity notation uses proper LaTeX
- [ ] No mixing of inline and block math on same line
- [ ] All special characters are properly escaped
- [ ] Mathematical expressions are consistent throughout the document

## Implementation Notes

- These guidelines apply to both README.md and EXPLANATION.md files
- The level of mathematical detail should be appropriate for the file type
- Always run quality checks after making mathematical formatting changes
- When in doubt, prefer clarity over brevity in mathematical expressions 
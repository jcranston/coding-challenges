# Longest Common Subsequence - Intuition Building

## Problem Recap

Given two strings `text1` and `text2`, we need to find the length of their longest common subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

## Building Intuition with DP Notation

### Key Insight: `dp[i][j]` Notation

Just like in edit distance, we can define:
- **`dp[i][j]`** = length of the longest common subsequence between the first `i` characters of `text1` and the first `j` characters of `text2`

This notation makes the recurrence relation much more intuitive!

### Base Cases

1. **`dp[0][j] = 0`** for all `j`: Empty string has no common subsequence with any string
2. **`dp[i][0] = 0`** for all `i`: Any string has no common subsequence with empty string

### Recurrence Relation

For `i > 0` and `j > 0`, we have two cases:

#### Case 1: Characters Match (`text1[i-1] == text2[j-1]`)
```
dp[i][j] = 1 + dp[i-1][j-1]
```

**Intuition:** If the current characters match, we can extend the LCS from the previous subproblem by 1.

**Example:** 
- `text1 = "abcde"`, `text2 = "ace"`
- At `i=3, j=2`: `text1[2] = 'c'`, `text2[1] = 'c'` (both are 'c')
- `dp[3][2] = 1 + dp[2][1]` = 1 + 1 = 2 (LCS is "ac")

#### Case 2: Characters Don't Match (`text1[i-1] != text2[j-1]`)
```
dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

**Intuition:** If characters don't match, we take the best of two options:
1. Skip the current character from `text1`: `dp[i-1][j]`
2. Skip the current character from `text2`: `dp[i][j-1]`

**Example:**
- `text1 = "abcde"`, `text2 = "ace"`
- At `i=4, j=2`: `text1[3] = 'd'`, `text2[1] = 'c'` (different characters)
- `dp[4][2] = max(dp[3][2], dp[4][1])` = max(2, 1) = 2

## Visual Example

Let's trace through `text1 = "abcde"`, `text2 = "ace"`:

```
     |   | a | c | e |
-----|---|---|---|---|
     | 0 | 0 | 0 | 0 |
  a  | 0 | 1 | 1 | 1 |
  b  | 0 | 1 | 1 | 1 |
  c  | 0 | 1 | 2 | 2 |
  d  | 0 | 1 | 2 | 2 |
  e  | 0 | 1 | 2 | 3 |
```

**Step-by-step explanation:**
1. `dp[1][1]`: 'a' == 'a' → `1 + dp[0][0] = 1 + 0 = 1`
2. `dp[1][2]`: 'a' != 'c' → `max(dp[0][2], dp[1][1]) = max(0, 1) = 1`
3. `dp[3][2]`: 'c' == 'c' → `1 + dp[2][1] = 1 + 1 = 2`
4. `dp[5][3]`: 'e' == 'e' → `1 + dp[4][2] = 1 + 2 = 3`

## Why This Works

The key insight is that we're building the solution incrementally:
- Each `dp[i][j]` represents the optimal solution for a smaller subproblem
- When characters match, we can extend the previous optimal solution
- When characters don't match, we take the best of two possible choices

This approach guarantees we find the longest common subsequence because:
1. We explore all possible combinations of including/excluding characters
2. We always take the maximum when characters don't match
3. We build from smaller subproblems to larger ones

## Time and Space Complexity

- **Time:** O(m×n) where m = len(text1), n = len(text2)
- **Space:** O(m×n) for the DP table

## Comparison with Edit Distance

The key difference is in the recurrence:
- **Edit Distance:** When characters don't match, we take `min` of three operations
- **LCS:** When characters don't match, we take `max` of two choices (skip from either string)

This makes sense because:
- Edit distance wants to minimize operations (cost)
- LCS wants to maximize length (benefit) 
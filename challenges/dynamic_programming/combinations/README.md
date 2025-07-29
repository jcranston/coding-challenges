**Custom Problem**
**Tags:** dynamic programming, combinatorics, memoization, tabulation

# Combinations (C(n,k))

## Problem

Given two integers `n` and `k`, calculate the number of ways to choose `k` items from a set of `n` items, denoted as C(n,k) or "n choose k".

The mathematical formula is: C(n,k) = n! / (k! * (n-k)!)

This problem can be solved using dynamic programming by finding a recurrence relation.

## Examples

**Example 1:**
```
Input: n = 5, k = 2
Output: 10
Explanation: C(5,2) = 5! / (2! * 3!) = 120 / (2 * 6) = 10
```

**Example 2:**
```
Input: n = 4, k = 2
Output: 6
Explanation: C(4,2) = 4! / (2! * 2!) = 24 / (2 * 2) = 6
```

**Example 3:**
```
Input: n = 6, k = 3
Output: 20
Explanation: C(6,3) = 6! / (3! * 3!) = 720 / (6 * 6) = 20
```

## Constraints

- `0 <= k <= n <= 50`
- The result will fit in a 32-bit integer

## Clarifications & Assumptions

- C(n,0) = 1 (one way to choose nothing)
- C(n,n) = 1 (one way to choose everything)
- C(n,k) = 0 when k > n (impossible to choose more than available)
- The order of selection does not matter
- This is a mathematical combination, not permutation

## Approach

This problem can be solved using dynamic programming with two main approaches:

1. **Top-down (Memoization):** Use recursion with memoization to avoid redundant calculations
2. **Bottom-up (Tabulation):** Build Pascal's triangle iteratively from smaller subproblems

Both approaches use the same recurrence relation. 

**Hint:** Consider what happens when you decide whether to include or exclude the first item from your selection. How does this choice affect the remaining subproblem?

## Notes

- This is a classic dynamic programming problem that demonstrates overlapping subproblems
- The solution builds Pascal's triangle, where each entry C(n,k) represents the number of ways to choose k items from n items
- The recurrence relation has a clear combinatorial interpretation that you can discover through problem-solving
- Time complexity: O(n*k), Space complexity: O(n*k) for the DP table 
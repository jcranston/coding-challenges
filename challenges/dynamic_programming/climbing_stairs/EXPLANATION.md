# Explanation: Climbing Stairs

## Problem Recap
Given `n` steps, you can climb either 1 or 2 steps at a time. Return the number of distinct ways to reach the top.

## High-level Approach
This is a classic dynamic programming problem, equivalent to computing the nth Fibonacci number. The number of ways to reach step `n` is the sum of the ways to reach steps `n-1` and `n-2`.

## Step-by-step Breakdown
1. **DP Table Definition:**
   - Let `dp[i]` be the number of ways to reach step `i`.
2. **Base Cases:**
   - `dp[0] = 1` (one way to stay at the bottom)
   - `dp[1] = 1` (one way to reach the first step)
3. **DP Transition:**
   - For `i >= 2`, `dp[i] = dp[i-1] + dp[i-2]`
   - At each step, you can come from one step below or two steps below.
4. **Result:**
   - The answer is `dp[n]`.

## Annotated Code
```python
def climbing_stairs(n: int) -> int:
    memo = {}
    def dp(i):
        if i <= 1:
            return 1
        if i in memo:
            return memo[i]
        memo[i] = dp(i - 1) + dp(i - 2)
        return memo[i]
    return dp(n)
```
- This uses memoized recursion (top-down DP). You can also use an iterative (bottom-up) approach for O(1) space.
- Time complexity is O(n), space complexity is O(n) due to memoization.

## Test Cases
- `n = 0` → Output: 1
- `n = 1` → Output: 1
- `n = 2` → Output: 2
- `n = 3` → Output: 3
- `n = 4` → Output: 5
- `n = 5` → Output: 8

## Common Pitfalls
- Not handling the base cases correctly (especially `n = 0` and `n = 1`).
- Using exponential time recursion without memoization.

## Variations
- If you can take up to `k` steps at a time, generalize the recurrence to sum over the previous `k` steps.
- If some steps are broken, skip them in the recurrence.

## Relevant Literature
- [LeetCode #70: Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [Fibonacci Sequence and Dynamic Programming](https://en.wikipedia.org/wiki/Fibonacci_number)
- CLRS, Section 15.1: Dynamic Programming 
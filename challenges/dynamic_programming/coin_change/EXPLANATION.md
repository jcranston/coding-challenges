# Explanation: Coin Change

## Problem Recap
Given an array of coin denominations `coins` and an integer `amount`, return the fewest number of coins needed to make up that amount. If it is not possible, return -1. You have an infinite supply of each coin.

## High-level Approach
This is a classic dynamic programming problem. The main idea is to build up the answer for all amounts from 0 to the target using either top-down (memoized recursion) or bottom-up (tabulation) DP.

## Step-by-step Breakdown
### Bottom-Up DP (Canonical Solution)
1. **DP Table Definition:**
   - Let `dp[a]` be the minimum number of coins needed to make up amount `a`.
2. **Initialization:**
   - `dp[0] = 0` (zero coins needed for amount 0).
   - All other `dp[a]` initialized to infinity (impossible initially).
3. **DP Transition:**
   - For each amount `a` from 1 to `amount`, for each coin in `coins`:
     - If `a - coin >= 0`, set `dp[a] = min(dp[a], 1 + dp[a - coin])`.
4. **Result:**
   - If `dp[amount]` is still infinity, return -1 (not possible). Otherwise, return `dp[amount]`.

### Top-Down DP (User Solution)
- Use recursion with memoization to compute the minimum coins for each remaining amount.
- For each recursive call, try subtracting each coin and take the minimum.
- Memoize results to avoid recomputation.

## Annotated Code (Canonical Solution)
```python
def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], 1 + dp[a - coin])
    return dp[amount] if dp[amount] != float("inf") else -1
```
- The DP table is filled for all amounts up to the target.
- Time complexity is O(amount * len(coins)).

## Test Cases
- `coins = [1, 2, 5], amount = 11` → Output: 3
- `coins = [2], amount = 3` → Output: -1
- `coins = [1], amount = 0` → Output: 0

## Common Pitfalls
- Not initializing `dp[0]` to 0.
- Forgetting to check for impossible cases (return -1 if no solution).
- Not memoizing in the top-down approach, leading to TLE.

## Variations
- If you want to count the number of ways to make up the amount, use a different DP recurrence.
- If coins have limited supply, use a 2D DP or knapsack variant.

## Relevant Literature
- [LeetCode #322: Coin Change](https://leetcode.com/problems/coin-change/)
- [Dynamic Programming for Coin Change](https://leetcode.com/tag/dynamic-programming/)
- CLRS, Section 15.1: Dynamic Programming 
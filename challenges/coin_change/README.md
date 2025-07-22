# Coin Change

## Problem
You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

## Example
```
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0
```

## Constraints
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

## Clarifications & Assumptions
- All coin denominations are positive integers.
- You can use each coin denomination as many times as needed.
- If it is not possible to make up the amount, return -1.
- The answer is guaranteed to fit in a 32-bit signed integer.

## Approach
Describe your approach and thought process after attempting the problem. Consider dynamic programming for optimal performance.

## Notes
- Edge cases: amount = 0, coins = [1], coins cannot sum to amount, large amount, duplicate coin denominations. 
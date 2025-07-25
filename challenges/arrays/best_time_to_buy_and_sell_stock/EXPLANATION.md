# Best Time to Buy and Sell Stock — EXPLANATION

## Problem Recap
Given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day, return the maximum profit you can achieve from a single buy and sell. If no profit is possible, return 0.

## High-Level Approach
Track the minimum price seen so far as you iterate through the array. At each step, calculate the profit if you sold today, and update the maximum profit accordingly.

## Step-by-Step Solution
1. Initialize `min_price` to a very large value and `max_profit` to 0.
2. Iterate through the prices:
    - If the current price is less than `min_price`, update `min_price`.
    - Otherwise, calculate the profit if you sold today (`price - min_price`) and update `max_profit` if it's higher.
3. Return `max_profit`.

## Annotated Code
```python
from typing import List

def max_profit(prices: List[int]) -> int:
    max_profit = 0
    min_price = float('inf')
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit
```

## Example Test Cases
```python
assert max_profit([7,1,5,3,6,4]) == 5  # Buy at 1, sell at 6
assert max_profit([7,6,4,3,1]) == 0    # No profit possible
```

## Common Pitfalls
- Not updating the minimum price as you iterate.
- Allowing buying and selling on the same day (must buy before sell).
- Returning a negative profit (should return 0 if no profit is possible).

## Variations
- Allow multiple transactions (buy/sell multiple times).
- Add a cooldown period between transactions.

## References
- [LeetCode #121: Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [Dynamic Programming Pattern](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/) 
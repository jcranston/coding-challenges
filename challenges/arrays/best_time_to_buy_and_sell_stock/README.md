**LeetCode #121**  
**Tags:** arrays, dynamic programming

# Best Time to Buy and Sell Stock

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Example

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No transaction is done, i.e., max profit = 0.
```

## Constraints
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

## Clarifications / Assumptions
- You must buy before you sell (no shorting).
- Only one transaction (buy/sell) is allowed.
- If no profit is possible, return 0.

## Hints
1. Keep track of the minimum price seen so far as you iterate.
2. At each step, calculate the profit if you sold today.
3. Update the maximum profit accordingly. 
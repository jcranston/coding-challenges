from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Returns the maximum profit from a single buy and sell of stock given
    daily prices. If no profit is possible, returns 0.

    Args:
        prices (List[int]): List of stock prices by day.
    Returns:
        int: The maximum profit achievable, or 0 if no profit is possible.
    """
    max_profit = -1
    min_price = 10**5

    for price in prices:
        if price < min_price:
            min_price = price
        max_profit = max(max_profit, price - min_price)
    return max_profit

def coin_change_user(coins, amount):
    """
    User-submitted solution for the Coin Change problem (top down).
    Args:
        coins (List[int]): The list of coin denominations.
        amount (int): The total amount to make up.
    Returns:
        int: The fewest number of coins needed, or -1 if not possible.
    """
    memo = {}

    def dp_top_down(remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return float("inf")
        if remaining in memo:
            return memo[remaining]
        result = min(1 + dp_top_down(remaining - coin) for coin in coins)
        memo[remaining] = result
        return result

    answer = dp_top_down(amount)
    return answer if answer != float("inf") else -1


def coin_change_canonical(coins, amount):
    """
    Canonical solution for the Coin Change problem (bottom up).
    Args:
        coins (List[int]): The list of coin denominations.
        amount (int): The total amount to make up.
    Returns:
        int: The fewest number of coins needed, or -1 if not possible.
    """
    # Bottom-up DP (tabulation)
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], 1 + dp[a - coin])
    return dp[amount] if dp[amount] != float("inf") else -1

def climbing_stairs(n: int) -> int:
    """
    Returns the number of distinct ways to climb to the top of a staircase
    with n steps, where you can take either 1 or 2 steps at a time.

    Args:
        n: The total number of steps in the staircase.

    Returns:
        The total number of distinct ways to reach the top as an integer.

    Clarifications / Assumptions:
    - You can take either 1 or 2 steps at a time.
    - The order of steps matters (e.g., 1+2 and 2+1 are different ways).
    - Return the total number of distinct ways to reach the top as an integer.
    """
    memo = {}

    def dp(i):
        if i <= 1:
            return 1
        if i in memo:
            return memo[i]
        memo[i] = dp(i - 1) + dp(i - 2)
        return memo[i]

    return dp(n)

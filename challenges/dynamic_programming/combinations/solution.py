"""Combinations (C(n,k)) solutions.

This module provides both user and canonical implementations using top-down
(memoization) and bottom-up (tabulation) dynamic programming approaches.
"""

from typing import Dict, Tuple


def combinations_user_top_down(n: int, k: int) -> int:
    """User implementation of C(n,k) using top-down dynamic programming with
    memoization.

    Args:
        n: Total number of items
        k: Number of items to choose

    Returns:
        Number of ways to choose k items from n items
    """
    memo = {}

    def rec_combinations(n: int, k: int) -> int:
        # see if result is in memo
        if (n, k) in memo:
            return memo[(n, k)]

        # base cases
        if k == 0:  # choose nothing
            return 1
        if k == n:  # choose everything
            return 1
        if k > n:  # impossible to choose more than available
            return 0

        memo[(n, k)] = rec_combinations(n - 1, k - 1) + rec_combinations(
            n - 1, k
        )
        return memo[(n, k)]

    return rec_combinations(n, k)


def combinations_user_bottom_up(n: int, k: int) -> int:
    """User implementation of C(n,k) using bottom-up dynamic programming with
    tabulation.

    Args:
        n: Total number of items
        k: Number of items to choose

    Returns:
        Number of ways to choose k items from n items
    """
    # Create DP table - we only need up to k columns
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base cases: C(n,0) = 1 for all n, C(n,n) = 1 for all n
    for i in range(n + 1):
        dp[i][0] = 1  # C(i,0) = 1
        if i <= k:
            dp[i][i] = 1  # C(i,i) = 1 (only if i <= k)

    # Fill the table using recurrence: C(n,k) = C(n-1,k-1) + C(n-1,k)
    for i in range(1, n + 1):
        for j in range(1, min(i, k + 1)):  # Only fill up to min(i, k+1)
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][k]


def combinations_canonical_top_down(n: int, k: int) -> int:
    """Canonical implementation of C(n,k) using top-down dynamic programming
    with memoization.

    This is the standard recursive approach with memoization to avoid
    redundant calculations.

    Args:
        n: Total number of items
        k: Number of items to choose

    Returns:
        Number of ways to choose k items from n items
    """
    memo = {}

    def dp(i: int, j: int) -> int:
        # Base cases
        if j == 0 or j == i:
            return 1
        if j > i:
            return 0

        # Check if we've already computed this subproblem
        if (i, j) in memo:
            return memo[(i, j)]

        # Recurrence: C(i,j) = C(i-1,j-1) + C(i-1,j)
        memo[(i, j)] = dp(i - 1, j - 1) + dp(i - 1, j)
        return memo[(i, j)]

    return dp(n, k)


def combinations_canonical_bottom_up(n: int, k: int) -> int:
    """Canonical implementation of C(n,k) using bottom-up dynamic programming
    with tabulation.

    This is the standard iterative approach that builds Pascal's triangle
    from smaller subproblems to larger ones.

    Args:
        n: Total number of items
        k: Number of items to choose

    Returns:
        Number of ways to choose k items from n items
    """
    # Create DP table - we only need up to k columns
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base cases: C(i,0) = 1 for all i, C(i,i) = 1 for all i <= k
    for i in range(n + 1):
        dp[i][0] = 1  # C(i,0) = 1
        if i <= k:
            dp[i][i] = 1  # C(i,i) = 1 (only if i <= k)

    # Fill the table using recurrence: C(i,j) = C(i-1,j-1) + C(i-1,j)
    for i in range(1, n + 1):
        for j in range(1, min(i, k + 1)):  # Only fill up to min(i, k+1)
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][k]

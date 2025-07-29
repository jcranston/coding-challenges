"""
Longest Common Subsequence solutions.

This module provides both user and canonical implementations using
top-down (memoization) and bottom-up (tabulation) dynamic programming
approaches.
"""

from typing import Dict, Tuple


def longest_common_subsequence_user_top_down(
    text1: str, text2: str
) -> int:
    """
    User implementation of LCS using top-down dynamic programming with
    memoization.

    Args:
        text1: First string
        text2: Second string

    Returns:
        Length of the longest common subsequence
    """
    m, n = len(text1), len(text2)
    sentinel = -1
    memo = [[sentinel] * (n + 1) for _ in range(m + 1)]  # store result in memo

    def rec_lcs(i: int, j: int):
        # see if answer is in memo
        if memo[i][j] != sentinel:
            return memo[i][j]

        # base case: LCS against empty string is always 0
        if i == 0 or j == 0:
            result = 0

        # if characters match, increment lcs by 1 and solve subproblem
        elif text1[i - 1] == text2[j - 1]:
            result = 1 + rec_lcs(i - 1, j - 1)

        # otherwise, find max of either skipping char in text1 or text2
        else:
            result = max(
                rec_lcs(i - 1, j),  # skip char in text1
                rec_lcs(i, j - 1)   # skip char in text2
            )

        memo[i][j] = result
        return result

    return rec_lcs(m, n)


def longest_common_subsequence_user_bottom_up(
    text1: str, text2: str
) -> int:
    """
    User implementation of LCS using bottom-up dynamic programming with
    tabulation.

    Args:
        text1: First string
        text2: Second string

    Returns:
        Length of the longest common subsequence
    """
    m, n = len(text1), len(text2)
    memo = [[0] * (n + 1) for _ in range(m + 1)]

    for idx1 in range(1, m + 1):
        for idx2 in range(1, n + 1):
            if text1[idx1 - 1] == text2[idx2 - 1]:
                memo[idx1][idx2] = 1 + memo[idx1 - 1][idx2 - 1]
            else:
                memo[idx1][idx2] = max(
                    memo[idx1 - 1][idx2],  # remove char from word1
                    memo[idx1][idx2 - 1]   # remove char from word2
                )

    return memo[m][n]


def longest_common_subsequence_canonical_top_down(
    text1: str, text2: str
) -> int:
    """
    Canonical implementation of LCS using top-down dynamic programming with
    memoization.

    This is the standard recursive approach with memoization to avoid
    redundant calculations.

    Args:
        text1: First string
        text2: Second string

    Returns:
        Length of the longest common subsequence
    """
    memo = {}

    def dp(i: int, j: int) -> int:
        # Base case: if we've reached the end of either string
        if i == len(text1) or j == len(text2):
            return 0

        # Check if we've already computed this subproblem
        if (i, j) in memo:
            return memo[(i, j)]

        # If characters match, include this character in LCS
        if text1[i] == text2[j]:
            memo[(i, j)] = 1 + dp(i + 1, j + 1)
        else:
            # Take maximum of excluding character from text1 or text2
            memo[(i, j)] = max(dp(i + 1, j), dp(i, j + 1))

        return memo[(i, j)]

    return dp(0, 0)


def longest_common_subsequence_canonical_bottom_up(
    text1: str, text2: str
) -> int:
    """
    Canonical implementation of LCS using bottom-up dynamic programming with
    tabulation.

    This is the standard iterative approach that builds the solution
    from smaller subproblems to larger ones.

    Args:
        text1: First string
        text2: Second string

    Returns:
        Length of the longest common subsequence
    """
    m, n = len(text1), len(text2)

    # Create DP table with extra row/column for base cases
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                # Characters match, extend the LCS
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Characters don't match, take maximum of excluding from either
                # string
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

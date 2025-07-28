def edit_distance_user_bottom_up(word1: str, word2: str) -> int:
    """
    User implementation for computing the edit distance between two words,
    using bottom-up dynamic programming approach with tabulation.
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill first row and first column (base cases)
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(m + 1):
        dp[i][0] = i

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],     # delete
                    dp[i][j - 1],     # insert
                    dp[i - 1][j - 1]  # replace
                )

    return dp[m][n]


def edit_distance_user_top_down(word1: str, word2: str) -> int:
    """
    User implementation for computing the edit distance between two words,
    using the top down recursive approach with memoization.
    """
    sentinel = -1
    memo = [
        [sentinel for _ in range(len(word2) + 1)]
        for _ in range(len(word1) + 1)
    ]

    def rec_edit_distance(s1_idx, s2_idx) -> int:
        # check if we've already computed the subproblem
        if memo[s1_idx][s2_idx] != sentinel:
            return memo[s1_idx][s2_idx]

        # base cases
        if s1_idx == 0:
            result = s2_idx
        elif s2_idx == 0:
            result = s1_idx
        else:
            # recursive cases
            if word1[s1_idx - 1] == word2[s2_idx - 1]:
                result = rec_edit_distance(s1_idx - 1, s2_idx - 1)
            else:
                result = 1 + min(
                    rec_edit_distance(s1_idx - 1, s2_idx),  # delete
                    rec_edit_distance(s1_idx, s2_idx - 1),  # insert
                    rec_edit_distance(s1_idx - 1, s2_idx - 1)  # replace
                )

        memo[s1_idx][s2_idx] = result
        return result

    return rec_edit_distance(len(word1), len(word2))


def edit_distance_canonical_bottom_up(word1: str, word2: str) -> int:
    """
    Canonical bottom-up solution for computing the edit distance between two
    words.
    """
    m, n = len(word1), len(word2)

    # Create DP table with base cases
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill first row and first column (base cases)
    for j in range(n + 1):
        dp[0][j] = j  # Convert empty string to word2[:j]
    for i in range(m + 1):
        dp[i][0] = i  # Convert word1[:i] to empty string

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation needed
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],     # Delete character from word1
                    dp[i][j - 1],     # Insert character into word1
                    dp[i - 1][j - 1]  # Replace character in word1
                )

    return dp[m][n]


def edit_distance_canonical_top_down(word1: str, word2: str) -> int:
    """
    Canonical top-down solution for computing the edit distance between two
    words.
    """
    m, n = len(word1), len(word2)

    # Create memoization table
    memo = [[-1] * (n + 1) for _ in range(m + 1)]

    def dp(i: int, j: int) -> int:
        # Check if already computed
        if memo[i][j] != -1:
            return memo[i][j]

        # Base cases
        if i == 0:
            memo[i][j] = j  # Convert empty string to word2[:j]
            return memo[i][j]
        if j == 0:
            memo[i][j] = i  # Convert word1[:i] to empty string
            return memo[i][j]

        # Recursive cases
        if word1[i - 1] == word2[j - 1]:
            memo[i][j] = dp(i - 1, j - 1)  # No operation needed
        else:
            memo[i][j] = 1 + min(
                dp(i - 1, j),     # Delete character from word1
                dp(i, j - 1),     # Insert character into word1
                dp(i - 1, j - 1)  # Replace character in word1
            )

        return memo[i][j]

    return dp(m, n)

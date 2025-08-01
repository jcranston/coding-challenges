def user_unique_paths(m: int, n: int) -> int:
    """User's implementation of the unique paths problem.

    Calculate the number of unique paths from top-left to bottom-right.

    Args:
        m: Number of rows in the grid
        n: Number of columns in the grid

    Returns:
        The number of unique paths from (0,0) to (m-1,n-1)
    """
    memo = {}

    def dp(x, y):
        if (x, y) in memo:
            return memo[(x, y)]

        # Base case: if we're at the start, there's 1 path
        if x == 0 and y == 0:
            return 1

        # Border cases: only recurse in valid directions
        if x == 0:  # At top border, can only go right
            result = dp(x, y - 1)
        elif y == 0:  # At left border, can only go down
            result = dp(x - 1, y)
        else:  # In middle, can go both directions
            result = dp(x - 1, y) + dp(x, y - 1)

        memo[(x, y)] = result
        return result

    # We want paths to (m-1, n-1) since grid is 0-indexed
    return dp(m - 1, n - 1)


def canonical_unique_paths(m: int, n: int) -> int:
    """Canonical implementation of the unique paths problem.

    Calculate the number of unique paths from top-left to bottom-right.

    Args:
        m: Number of rows in the grid
        n: Number of columns in the grid

    Returns:
        The number of unique paths from (0,0) to (m-1,n-1)
    """
    # Combinatorial approach: C(m+n-2, m-1)
    # We need to make (m-1) right moves and (n-1) down moves
    # Total moves = (m-1) + (n-1) = m+n-2
    # We choose (m-1) positions for right moves: C(m+n-2, m-1)

    def combination(n, k):
        """Calculate C(n,k) = n!

        / (k! * (n-k)!)
        """
        if k > n - k:
            k = n - k  # Use symmetry

        result = 1
        for i in range(k):
            result = result * (n - i) // (i + 1)
        return result

    return combination(m + n - 2, m - 1)

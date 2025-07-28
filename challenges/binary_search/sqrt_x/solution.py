def user_sqrt_x(x: int) -> int:
    """
    User-submitted solution for LeetCode 69: Sqrt(x).
    Args:
        x: Non-negative integer.
    Returns:
        The integer square root of x (greatest integer y such that y*y <= x).
    """
    # Brute-force approach
    y = 0
    while y * y <= x:
        y += 1
    return y - 1


def canonical_sqrt_x(x: int) -> int:
    """
    Canonical solution for LeetCode 69: Sqrt(x) using binary search.
    Args:
        x: Non-negative integer.
    Returns:
        The integer square root of x (greatest integer y such that y*y <= x).
    """
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

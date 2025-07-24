def minimum_size_subarray_sum_user(target, nums):
    """
    User-submitted solution for the minimum size subarray sum problem.
    Args:
        target (int): The target sum.
        nums (List[int]): The input array of positive integers.
    Returns:
        tuple: (int, List[int]) - The minimal length of a contiguous subarray
        with sum >= target, and the actual subarray. Returns (0, []) if none
        exists.
    """
    if not nums:
        return (0, [])
    n = len(nums)
    l_min, r_min = 0, 0
    l, r = 0, 0
    rolling_sum = 0
    smallest_window = float("inf")

    while r < n:
        # expand window from the right while it is invalid
        while rolling_sum < target and r <= n - 1:
            rolling_sum += nums[r]
            r += 1

        # shrink window from the left  until it is invalid
        while rolling_sum >= target and l < r:
            rolling_sum -= nums[l]
            l += 1

        # no valid window
        if l == 0 and r == n and rolling_sum < target:
            return (0, [])

        window_len = r - l + 1
        if window_len < smallest_window:
            smallest_window = window_len
            l_min = l - 1
            r_min = r - 1

    return (
        (0, [])
        if smallest_window == float("inf")
        else (smallest_window, nums[l_min : r_min + 1])
    )


def minimum_size_subarray_sum_canonical(target, nums):
    """
    Canonical solution for the minimum size subarray sum problem.
    Args:
        target (int): The target sum.
        nums (List[int]): The input array of positive integers.
    Returns:
        tuple: (int, List[int]) - The minimal length of a contiguous subarray
        with sum >= target, and the actual subarray. Returns (0, []) if none
        exists.
    """
    pass

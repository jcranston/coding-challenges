from collections import deque


def sliding_window_maximum(nums, k):
    """Returns the maximum value in each sliding window of size k as it moves
    from left to right across the array.

    Args:
        nums (List[int]): The input array.
        k (int): The window size.
    Returns:
        List[int]: The list of maximums for each window.
    """
    result = []
    dq = deque()  # stores indices
    for i, num in enumerate(nums):
        # Remove indices whose values are less than current num
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        # Remove indices that are out of the current window
        if dq and dq[0] <= i - k:
            dq.popleft()
        dq.append(i)
        # Append the max for the current window
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result

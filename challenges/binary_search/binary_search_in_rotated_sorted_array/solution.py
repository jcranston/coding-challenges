def binary_search_in_rotated_sorted_array_user(nums, target):
    """User-submitted solution for binary search in rotated sorted array.

    Args:
        nums (List[int]): The rotated sorted array.
        target (int): The value to search for.
    Returns:
        int: The index of target if found, else -1.
    """
    lp = 0
    rp = len(nums) - 1

    while lp <= rp:
        mid = (lp + rp) // 2
        if nums[mid] == target:
            return mid

        if nums[lp] <= nums[mid]:  # left half is sorted
            if nums[lp] <= target < nums[mid]:
                rp = mid - 1  # target in left half
            else:
                lp = mid + 1  # target in right half

        else:  # right half is sorted
            if nums[mid] < target <= nums[rp]:
                lp = mid + 1  # target in right half
            else:
                rp = mid - 1  # target in left half

    return -1


def binary_search_in_rotated_sorted_array_canonical(nums, target):
    """Canonical solution for binary search in rotated sorted array.

    Args:
        nums (List[int]): The rotated sorted array.
        target (int): The value to search for.
    Returns:
        int: The index of target if found, else -1.
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

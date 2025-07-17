def user_find_duplicate_number(nums):
    """
    User-submitted solution for the Find the Duplicate Number problem.
    Args:
        nums (List[int]): Array of n+1 integers where each integer is between 1
            and n (inclusive).
    Returns:
        int: The duplicate number in the array.
    """
    ps = nums[0]
    pf = nums[0]

    # find intersection point in cycle
    while True:
        ps = nums[ps]
        pf = nums[nums[pf]]
        if ps == pf:
            break

    # find entrance to cycle
    p1 = nums[0]
    p2 = pf  # WLOG

    while p1 != p2:
        p1 = nums[p1]
        p2 = nums[p2]

    return p1


def canonical_find_duplicate_number(nums):
    """
    Canonical solution for the Find the Duplicate Number problem (Floyd's
    Tortoise and Hare).
    Args:
        nums (List[int]): Array of n+1 integers where each integer is between 1
            and n (inclusive).
    Returns:
        int: The duplicate number in the array.
    """
    # Phase 1: Find the intersection point in the cycle
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    # Phase 2: Find the entrance to the cycle (duplicate number)
    ptr1 = nums[0]
    ptr2 = slow
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1

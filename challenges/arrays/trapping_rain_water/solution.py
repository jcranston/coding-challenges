from typing import List


def trapping_rain_water_user(height: List[int]) -> int:
    """
    User-submitted solution for the Trapping Rain Water problem.
    Args:
        height (List[int]): List of non-negative integers representing elevation
        map.
    Returns:
        int: Total amount of trapped rain water.
    """
    if len(height) < 3:
        return 0
    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]
    trapped = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                trapped += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                trapped += right_max - height[right]
            right -= 1

    return trapped


def trapping_rain_water_canonical(height: List[int]) -> int:
    """
    Canonical solution for the Trapping Rain Water problem using the two-pointer
    approach.
    Args:
        height (List[int]): List of non-negative integers representing elevation
        map.
    Returns:
        int: Total amount of trapped rain water.
    """
    if len(height) < 3:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

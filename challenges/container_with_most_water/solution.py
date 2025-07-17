from typing import List


def find_max_water_container_area(height: List[int]) -> int:
    """
    Find the maximum area of water that can be contained between two vertical
    lines.

    This function uses a two-pointer approach to efficiently find the maximum
    area without checking all possible pairs of lines. The key insight is that
    we can eliminate certain combinations by moving the pointer with the
    shorter height.

    Args:
        height (List[int]): Array representing the height of vertical lines at
            each position. Each element represents the height of a line at that
            index.

    Returns:
        int: The maximum area of water that can be contained between any two
            lines.

    Examples:
        >>> find_max_water_container_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
        >>> find_max_water_container_area([1, 1])
        1
        >>> find_max_water_container_area([4, 3, 2, 1, 4])
        16

    Notes:
        - The area is calculated as: width × min(height[left], height[right])
        - Width is the distance between two lines: right_index - left_index
        - The height is limited by the shorter of the two lines
        - Time complexity: O(n) where n is the length of the height array
        - Space complexity: O(1) as we only use constant extra space
    """
    lp = 0
    rp = len(height) - 1
    max_height = 0
    while lp < rp:
        max_height = max(max_height, min(height[lp], height[rp]) * (rp - lp))
        if height[lp] < height[rp]:
            lp += 1
        else:
            rp -= 1
    return max_height

from typing import List


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    User-submitted solution for LeetCode 253: Meeting Rooms II.
    Given a list of meeting intervals, return the minimum number of conference rooms required.
    Args:
        intervals (List[List[int]]): List of [start, end] meeting intervals.
    Returns:
        int: Minimum number of conference rooms required.
    """
    pass


def canonical_min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    Canonical solution for LeetCode 253: Meeting Rooms II.
    Uses a min-heap to track end times and determine the minimum number of rooms needed.
    Args:
        intervals (List[List[int]]): List of [start, end] meeting intervals.
    Returns:
        int: Minimum number of conference rooms required.
    """
    pass

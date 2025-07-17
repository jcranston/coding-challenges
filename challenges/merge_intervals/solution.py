from collections import deque
from typing import List


def merge_intervals_deque(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merges all overlapping intervals in a list using a deque-based approach and
    returns a list of non-overlapping intervals.
    """
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    q = deque(intervals)
    res = []
    while len(q) > 1:
        first = q.popleft()
        second = q.popleft()
        if first[1] >= second[0]:
            q.appendleft([first[0], max(first[1], second[1])])
        else:
            res.append(first)
            q.appendleft(second)
    if len(q) > 0:
        res.append(q.popleft())
    return res


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merges all overlapping intervals in a list and returns a list of
    non-overlapping intervals (standard approach).
    """
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged

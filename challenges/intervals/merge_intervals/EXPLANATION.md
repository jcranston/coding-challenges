# Explanation: Merge Intervals (LeetCode 56)

## Problem Recap
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

## High-Level Approach
This problem is a classic interval merging task. The main challenge is to efficiently merge all overlapping intervals and return the result in sorted order.

## Step-by-Step Breakdown
1. **Sort the intervals by start time:**
   - This ensures that any overlapping intervals are adjacent in the sorted list.
2. **Iterate through the intervals:**
   - Start with the first interval as the current interval.
   - For each subsequent interval:
     - If it overlaps with the current interval (i.e., its start is less than or equal to the current end), merge them by updating the end to the maximum of the two ends.
     - If it does not overlap, add the current interval to the result and start a new current interval.
3. **Add the last interval:**
   - After the loop, add the last current interval to the result.

## Annotated Canonical Solution
```python
from typing import List

def canonical_merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return merged
```
- **Why this works:**
  - Sorting ensures all overlaps are adjacent. By always merging with the last interval in the result, we efficiently build the merged list in a single pass.

## Test Cases & Edge Cases
- `[[1,3],[2,6],[8,10],[15,18]]` → `[[1,6],[8,10],[15,18]]`
- `[[1,4],[4,5]]` → `[[1,5]]`
- `[[1,4],[0,2],[3,5]]` → `[[0,5]]`
- `[[1,4]]` → `[[1,4]]`
- `[]` → `[]`

## Common Pitfalls
- Not sorting the intervals before merging.
- Forgetting to add the last interval after the loop.
- Off-by-one errors in the merging logic.
- Not handling empty input.

## Variations
- **Insert and merge a new interval:** How would you handle inserting a new interval and merging?
- **Return the number of merged intervals:** Instead of the list, return the count.
- **Intervals not sorted:** What if the input intervals are not sorted?

## Relevant Literature
- [LeetCode 56: Merge Intervals](https://leetcode.com/problems/merge-intervals/)
- [Interval Merging - GeeksforGeeks](https://www.geeksforgeeks.org/merging-intervals/)
- [CLRS, Chapter 16: Greedy Algorithms](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)

---
This explanation references the problem statement, canonical solution, and test cases, and follows the conventions in `ai_context/explanation_generation.md`. 
# Explanation: Insert Interval (LeetCode 57)

## Problem Recap
Given a list of non-overlapping intervals sorted by their start time, and a new interval, insert the new interval into the list (merge if necessary) so that the list remains sorted and non-overlapping.

## High-Level Approach
This problem is a classic interval manipulation task. The main challenge is to efficiently merge the new interval with any overlapping intervals and maintain the sorted, non-overlapping property of the list.

## Step-by-Step Breakdown
1. **Iterate through the intervals:**
   - Add all intervals that end before the new interval starts (no overlap) to the result.
2. **Merge Overlapping Intervals:**
   - For intervals that overlap with the new interval, merge them by updating the start to the minimum and the end to the maximum of the overlapping intervals.
3. **Add the Merged Interval:**
   - After merging, add the new (possibly merged) interval to the result.
4. **Add Remaining Intervals:**
   - Add all intervals that start after the new interval ends (no overlap) to the result.

## Annotated Canonical Solution
```python
from typing import List

def canonical_insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    result = []
    i = 0
    n = len(intervals)
    # Add all intervals before new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    # Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)
    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    return result
```
- **Why this works:**
  - The first loop skips all intervals that end before the new interval starts.
  - The second loop merges all overlapping intervals with the new interval.
  - The third loop adds the rest of the intervals.

## Test Cases & Edge Cases
- `intervals = [[1,3],[6,9]], new_interval = [2,5]` → `[[1,5],[6,9]]`
- `intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], new_interval = [4,8]` → `[[1,2],[3,10],[12,16]]`
- `intervals = [], new_interval = [5,7]` → `[[5,7]]`
- `intervals = [[1,5]], new_interval = [2,3]` → `[[1,5]]`
- `intervals = [[1,5]], new_interval = [2,7]` → `[[1,7]]`
- `intervals = [[1,5]], new_interval = [6,8]` → `[[1,5],[6,8]]`

## Common Pitfalls
- Not handling the case where the new interval is before all existing intervals or after all existing intervals.
- Forgetting to merge all overlapping intervals.
- Not maintaining the sorted order of intervals.
- Off-by-one errors in the merging logic.

## Variations
- **Insert multiple intervals:** How would you handle inserting a list of new intervals?
- **Intervals not sorted:** What if the input intervals are not sorted?
- **Return the number of merged intervals:** Instead of the list, return the count.

## Relevant Literature
- [LeetCode 57: Insert Interval](https://leetcode.com/problems/insert-interval/)
- [Interval Merging - GeeksforGeeks](https://www.geeksforgeeks.org/merging-intervals/)
- [CLRS, Chapter 16: Greedy Algorithms](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)

---
This explanation references the problem statement, canonical solution, and test cases, and follows the conventions in `ai_context/explanation_generation.md`. 
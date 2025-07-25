# Explanation: Interval List Intersections (LeetCode 986)

## Problem Recap
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order. Return the intersection of these two interval lists as a list of intervals.

## High-Level Approach
This problem is a classic two-pointer interval problem. The main challenge is to efficiently find all overlapping intervals between the two lists.

## Step-by-Step Breakdown
1. **Initialize two pointers:**
   - One for each interval list (let's call them `i` and `j`).
2. **Iterate through both lists:**
   - For each pair of intervals, check if they overlap.
   - If they overlap, add the intersection to the result.
   - Move the pointer that points to the interval with the smaller end value forward.
3. **Repeat until one list is exhausted.**

## Annotated Canonical Solution
```python
from typing import List

def canonical_intervals_intersection(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    i, j = 0, 0
    result = []
    while i < len(A) and j < len(B):
        start = max(A[i][0], B[j][0])
        end = min(A[i][1], B[j][1])
        if start <= end:
            result.append([start, end])
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return result
```
- **Why this works:**
  - By always advancing the pointer with the smaller end, we never miss a possible intersection and efficiently process both lists in O(m + n) time.

## Test Cases & Edge Cases
- `A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]` → `[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]`
- `A = [[1,3],[5,9]], B = []` → `[]`
- `A = [], B = [[4,8],[10,12]]` → `[]`
- `A = [[1,7]], B = [[3,10]]` → `[[3,7]]`
- `A = [[1,2],[3,4]], B = [[5,6],[7,8]]` → `[]`

## Common Pitfalls
- Not handling empty input lists.
- Off-by-one errors in the overlap check (`start <= end`).
- Not advancing the correct pointer, which can lead to missing intersections or infinite loops.

## Variations
- **Multiple interval lists:** How would you generalize to more than two lists?
- **Intervals not sorted:** What if the input intervals are not sorted?
- **Open intervals:** What if intervals are open (exclusive) instead of closed (inclusive)?

## Relevant Literature
- [LeetCode 986: Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)
- [Interval Problems - GeeksforGeeks](https://www.geeksforgeeks.org/intervals-in-data-structure/)
- [CLRS, Chapter 16: Greedy Algorithms](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)

---
This explanation references the problem statement, canonical solution, and test cases, and follows the conventions in `ai_context/explanation_generation.md`. 
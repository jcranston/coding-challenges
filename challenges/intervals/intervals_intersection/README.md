**LeetCode #986**  
**Tags:** intervals, two pointers, array

# Interval List Intersections

## Problem
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order. Return the intersection of these two interval lists as a list of intervals.

## Examples

### Example 1
```
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

### Example 2
```
Input: A = [[1,3],[5,9]], B = []
Output: []
```

## Constraints
- 0 <= A.length, B.length <= 1000
- 0 <= A[i][0] < A[i][1] <= 10^9
- 0 <= B[j][0] < B[j][1] <= 10^9
- A and B are both pairwise disjoint and in sorted order.

## Clarifications & Assumptions
- Intervals are closed (inclusive of endpoints).
- The output should be a list of all intersections, also as closed intervals.
- The input lists are already sorted and non-overlapping within themselves.

## Approach
- Use two pointers, one for each list.
- For each pair of intervals, check if they overlap.
- If they overlap, add the intersection to the result.
- Move the pointer that points to the interval with the smaller end value forward.
- Continue until one list is exhausted.

## Notes
- Edge cases: empty input lists, no overlap, one interval fully contained in another.
- This is a classic two-pointer interval problem. 
**LeetCode #56**  
**Tags:** array, sorting, intervals

# Merge Intervals

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

## Example

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

## Constraints
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^4

## Clarifications / Assumptions
- Each interval is represented as a list of two integers: [start, end].
- The input intervals may not be sorted.
- The output should be a list of non-overlapping intervals, sorted by their start value.
- If two intervals touch (e.g., [1,4] and [4,5]), they should be merged.
- Return the merged intervals as a list of lists. 
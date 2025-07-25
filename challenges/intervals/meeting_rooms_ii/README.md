**LeetCode #253**  
**Tags:** intervals, heap, sorting, greedy

# Meeting Rooms II

## Problem
Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required.

## Examples

### Example 1
```
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
```

### Example 2
```
Input: intervals = [[7,10],[2,4]]
Output: 1
```

## Constraints
- 1 <= intervals.length <= 10^4
- 0 <= start_i < end_i <= 10^6

## Clarifications & Assumptions
- Each meeting has a start and end time, and no two meetings can use the same room at the same time.
- Meetings may overlap.
- The answer is the minimum number of rooms required so that all meetings can take place.

## Approach
- Sort the intervals by start time.
- Use a min-heap to track the end times of ongoing meetings.
- For each meeting, if the earliest ending meeting is finished before the current meeting starts, reuse the room (pop from heap). Otherwise, allocate a new room (push to heap).
- The size of the heap at any time is the number of rooms needed.
- Time complexity: O(n log n), space complexity: O(n).

## Notes
- Edge cases: all meetings overlap, no overlap, single meeting, meetings with the same start or end time.
- This is a classic interview problem testing interval scheduling and heap usage. 
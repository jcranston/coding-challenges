# Explanation: Meeting Rooms II (LeetCode 253)

## Problem Recap
Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required so that all meetings can take place without overlap.

## High-Level Approach
This problem is a classic interval scheduling problem. The main challenge is to efficiently track overlapping meetings and determine the maximum number of concurrent meetings at any time. The optimal approach uses a min-heap to track the end times of ongoing meetings.

## Step-by-Step Breakdown
1. **Sort the Intervals:**
   - Sort the intervals by their start time. This allows us to process meetings in chronological order.
2. **Use a Min-Heap:**
   - Use a min-heap (priority queue) to keep track of the end times of meetings currently using a room.
3. **Process Each Meeting:**
   - For each meeting, check if the earliest ending meeting (top of the heap) has finished before the current meeting starts. If so, reuse the room (pop from heap). Otherwise, allocate a new room (push to heap).
   - Always push the current meeting's end time onto the heap.
4. **Result:**
   - The size of the heap at any time is the number of rooms needed. The maximum size reached is the answer.

## Annotated Canonical Solution
```python
from typing import List
import heapq

def canonical_min_meeting_rooms(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    heap = []  # stores end times
    for start, end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)  # Reuse room
        heapq.heappush(heap, end)
    return len(heap)
```
- **Why this works:** The heap always contains the end times of ongoing meetings. When a meeting ends before the next one starts, we reuse the room. The maximum number of rooms in use at any time is the answer.

## Test Cases & Edge Cases
- `[[0,30],[5,10],[15,20]]` → `2` (overlapping meetings)
- `[[7,10],[2,4]]` → `1` (no overlap)
- `[[1,5],[2,6],[3,7],[4,8]]` → `4` (all overlap)
- `[[1,2],[2,3],[3,4]]` → `1` (back-to-back meetings)
- `[[1,10],[2,3],[4,5],[6,7],[8,9]]` → `2` (nested meetings)
- `[[1,2]]` → `1` (single meeting)
- `[[1,5],[5,10],[10,15]]` → `1` (meetings touch but do not overlap)

## Common Pitfalls
- Not sorting the intervals by start time, which can lead to incorrect room allocation.
- Forgetting to pop from the heap when a meeting ends before the next one starts, leading to overcounting rooms.
- Not handling edge cases like a single meeting or all meetings overlapping.

## Variations
- **Return the actual room assignments:** Instead of just the count, return which meeting goes to which room.
- **Find the time(s) when the maximum number of rooms are used:** Useful for scheduling staff or resources.
- **Interval merging:** Related to problems like merging overlapping intervals.

## Relevant Literature
- [LeetCode 253: Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)
- [Interval Scheduling - CLRS, Chapter 16](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)
- [Heap Data Structure - GeeksforGeeks](https://www.geeksforgeeks.org/heap-data-structure/)

## Detailed Example Walkthrough
Let's walk through the main example step by step:

**Input:** `intervals = [[0,30],[5,10],[15,20]]`

1. **Sort intervals by start time:**
   - Sorted: `[[0,30],[5,10],[15,20]]`
2. **Initialize an empty min-heap.**
3. **Process each meeting:**
   - Add [0,30]: heap = [30]
   - Add [5,10]: 5 < 30, so need a new room. heap = [10, 30]
   - Add [15,20]: 15 >= 10, so pop 10 (room freed), then push 20. heap = [20, 30]
4. **Result:**
   - The maximum size of the heap is 2, so 2 rooms are required.

**Heap State at Each Step:**
| Step         | Heap (end times) |
|--------------|-----------------|
| Start        | []              |
| Add [0,30]   | [30]            |
| Add [5,10]   | [10, 30]        |
| Add [15,20]  | [20, 30]        |

**Important Note:**
- The correct answer is the **maximum size of the heap at any point during the iteration**, not just the length at the end. This is because the heap may shrink after the last meeting ends, but the peak size represents the maximum number of concurrent meetings (i.e., rooms needed).

**Updated Code Snippet (tracking max heap size):**
```python
import heapq
intervals = [[0,30],[5,10],[15,20]]
intervals.sort(key=lambda x: x[0])
heap = []
max_rooms = 0
for start, end in intervals:
    if heap and heap[0] <= start:
        print(f"Room freed (meeting ended at {heap[0]}) before {start}")
        heapq.heappop(heap)
    heapq.heappush(heap, end)
    max_rooms = max(max_rooms, len(heap))
    print(f"Meeting [{start},{end}] added, heap now: {heap}, max_rooms so far: {max_rooms}")
print(f"Minimum rooms required: {max_rooms}")
```
**Output:**
```
Meeting [0,30] added, heap now: [30], max_rooms so far: 1
Meeting [5,10] added, heap now: [10, 30], max_rooms so far: 2
Room freed (meeting ended at 10) before 15
Meeting [15,20] added, heap now: [20, 30], max_rooms so far: 2
Minimum rooms required: 2
```

**Note on Best Practice:**
- While returning `len(heap)` at the end works for the standard LeetCode 253 problem (since the heap contains all ongoing meetings after the last meeting is processed), it is best practice to track the maximum size of the heap during the loop. This approach is more robust, explicit, and future-proof, especially if the input or processing order changes, or if you want to visualize the peak number of concurrent meetings.

---
This explanation references the problem statement, canonical solution, and test cases, and follows the conventions in `ai_context/explanation_generation.md`. 
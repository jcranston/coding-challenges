# Explanation: Sliding Window Maximum

## Problem Recap
Given an array of integers `nums` and an integer `k`, return the maximum value in each sliding window of size `k` as it moves from left to right across the array.

## High-level Approach
A brute-force approach would check the maximum in every window, but this is inefficient for large arrays. The optimal solution uses a deque (double-ended queue) to keep track of indices of useful elements for each window, allowing us to find the maximum in O(1) time per window.

## Step-by-step Breakdown
1. **Deque Invariant:**
   - The deque stores indices of elements in decreasing order of their values (from front to back).
   - The front of the deque always contains the index of the maximum element for the current window.
2. **Processing Each Element:**
   - For each index `i`:
     - Remove indices from the back of the deque if their corresponding values are less than or equal to `nums[i]` (they can't be the max for this or any future window).
     - Remove the front index if it is out of the current window (`dq[0] <= i - k`).
     - Add the current index to the deque.
     - If the window has reached size `k` (`i >= k - 1`), append `nums[dq[0]]` to the result.

## Annotated Code
```python
from collections import deque

def sliding_window_maximum(nums, k):
    result = []
    dq = deque()  # stores indices
    for i, num in enumerate(nums):
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        if dq and dq[0] <= i - k:
            dq.popleft()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```
- The deque ensures that we always have access to the maximum for the current window in O(1) time.
- Time complexity is O(n), where n is the length of `nums`.

## Test Cases
- `nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3` → Output: `[3, 3, 5, 5, 6, 7]`
- `nums = [1], k = 1` → Output: `[1]`
- `nums = [9, 11], k = 2` → Output: `[11]`
- `nums = [4, 3, 2, 1], k = 2` → Output: `[4, 3, 2]`

## Common Pitfalls
- Not removing indices that are out of the current window.
- Not maintaining the decreasing order in the deque.
- Forgetting to append the result only after the first full window.

## Variations
- If you want the minimum in each window, adjust the deque to maintain increasing order.
- If `k == 1`, the output is just the original array.

## Relevant Literature
- [LeetCode #239: Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
- [Monotonic Queue Technique](https://cp-algorithms.com/data_structures/stack_queue_modification.html)
- CLRS, Section 10.1: Queues 
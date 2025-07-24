# Explanation: Find Median from Data Stream

## Problem Recap
You need to design a data structure that efficiently supports two operations:
- `add_num(num)`: Add a number from a data stream.
- `find_median()`: Return the median of all elements so far.

## Intuition
To find the median efficiently as numbers are added, we need a way to quickly access the middle value(s) of the current set of numbers. Keeping all numbers sorted would make insertion slow (O(n)), so we use two heaps to maintain the lower and upper halves of the data.

## The Two-Heap Solution
- **Max-heap (`low`)**: Stores the smaller half of the numbers (as negatives, since Python's `heapq` is a min-heap).
- **Min-heap (`high`)**: Stores the larger half of the numbers.

**Invariant:**
- All numbers in `low` are less than or equal to all numbers in `high`.
- The sizes of the heaps differ by at most 1.

## Algorithm
1. **Adding a Number**
    - Add the new number to `low` (max-heap, as negative).
    - Move the largest value from `low` to `high` to maintain order.
    - If `high` has more elements than `low`, move the smallest value from `high` back to `low`.

2. **Finding the Median**
    - If `low` has more elements, the median is the top of `low` (negated back to positive).
    - If both heaps are the same size, the median is the average of the tops of both heaps.

## Why Is This Efficient?
- **Insertion:** O(log n) per operation (heap push/pop).
- **Median Retrieval:** O(1) (peek at heap tops).
- This is optimal for streaming data where you need to frequently add numbers and find the median.

## Example
Suppose you add: 1, 2, 3

- Add 1:
    - `low = [-1]`, `high = []`
    - Median: 1
- Add 2:
    - `low = [-1]`, `high = [2]`
    - Median: (1 + 2) / 2 = 1.5
- Add 3:
    - `low = [-2, -1]`, `high = [3]`
    - Median: 2

## Summary
- The two-heap approach allows you to maintain the median in a dynamic data stream efficiently.
- This method is commonly asked in interviews and is the optimal solution for this problem. 
# Explanation: Kth Largest Element in an Array

## Problem Recap
Given an integer array `nums` and an integer `k`, return the k-th largest element in the array (not necessarily distinct).

## High-level Approach
There are several ways to solve this problem:
- **Sorting:** Sort the array and return the element at index `-k`.
- **Heap:** Use a min-heap of size `k` to keep track of the k largest elements seen so far.
- **Quickselect:** Use the Quickselect algorithm for average O(n) time.

The canonical solution here uses sorting for simplicity and reliability.

## Step-by-step Breakdown
1. **Sorting Approach:**
   - Sort the array in ascending order.
   - The k-th largest element is at index `-k` (counting from the end).
2. **Heap Approach (Alternative):**
   - Maintain a min-heap of size `k`.
   - For each element, push it onto the heap; if the heap exceeds size `k`, pop the smallest.
   - The root of the heap is the k-th largest element.
3. **Quickselect (Alternative):**
   - Partition the array as in quicksort, but only recurse into the side containing the k-th largest.
   - Average O(n) time, but worst-case O(n²).

## Annotated Code (Sorting Solution)
```python
from typing import List

def kth_largest_element(nums: List[int], k):
    nums.sort()
    return nums[-k]
```
- Sorting is O(n log n), where n is the length of `nums`.
- This approach is simple and works well for moderate input sizes.

## Test Cases
- `nums = [3,2,1,5,6,4], k = 2` → Output: 5
- `nums = [3,2,3,1,2,4,5,5,6], k = 4` → Output: 4

## Common Pitfalls
- Confusing the k-th largest with the k-th smallest (be careful with indices).
- Not handling duplicates correctly (the k-th largest is not necessarily unique).
- Not using 1-based indexing for k.

## Variations
- If you want the k-th smallest, use index `k-1` after sorting.
- For very large arrays, use a heap or quickselect for better performance.

## Relevant Literature
- [LeetCode #215: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [Heap Data Structure](https://en.wikipedia.org/wiki/Heap_(data_structure))
- [Quickselect Algorithm](https://en.wikipedia.org/wiki/Quickselect)
- CLRS, Section 9.2: Selection in Expected Linear Time 
# Median of Two Sorted Arrays — EXPLANATION

## Problem Recap
Given two sorted arrays `nums1` and `nums2`, return the median of the two sorted arrays. The overall run time complexity should be O(log(min(m, n))).

## High-Level Approach
Use binary search on the smaller array to partition both arrays such that the left and right halves have equal length and all elements on the left are less than or equal to those on the right. The median is then determined from the maximum of the left and the minimum of the right.

## Step-by-Step Solution
1. Ensure `nums1` is the smaller array (for efficiency).
2. Use binary search to partition `nums1` and `nums2` so that:
    - The total number of elements on the left equals the total on the right (or one more for odd total length).
    - The largest value on the left of both arrays is less than or equal to the smallest on the right.
3. If the partition is correct:
    - If the total length is odd, the median is the max of the left values.
    - If even, the median is the average of the max of the left and min of the right.
4. Adjust the binary search range based on comparisons at the partition.

## Annotated Code
```python
from typing import List

def median_of_two_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    while left <= right:
        i = (left + right) // 2
        j = (m + n + 1) // 2 - i
        a_left = nums1[i - 1] if i > 0 else float('-inf')
        a_right = nums1[i] if i < m else float('inf')
        b_left = nums2[j - 1] if j > 0 else float('-inf')
        b_right = nums2[j] if j < n else float('inf')
        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2 == 1:
                return max(a_left, b_left)
            else:
                return (max(a_left, b_left) + min(a_right, b_right)) / 2
        elif a_left > b_right:
            right = i - 1
        else:
            left = i + 1
```

## Example Test Cases
```python
assert median_of_two_sorted_arrays([1,3], [2]) == 2.0
assert median_of_two_sorted_arrays([1,2], [3,4]) == 2.5
```

## Common Pitfalls
- Not handling empty arrays correctly (one array may be empty).
- Not ensuring binary search is on the smaller array.
- Off-by-one errors in partitioning.

## Variations
- Find the kth smallest element in two sorted arrays.
- Merge k sorted arrays and find the median.

## References
- [LeetCode #4: Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)
- [Binary Search Partitioning](https://leetcode.com/problems/median-of-two-sorted-arrays/solutions/) 
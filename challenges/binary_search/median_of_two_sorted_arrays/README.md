# Median of Two Sorted Arrays

## Problem
Given two sorted arrays `nums1` and `nums2` of size m and n respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log(min(m, n))).

## Examples
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.0
Explanation: merged array = [1,2,3], median is 2.0

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.5
Explanation: merged array = [1,2,3,4], median is (2 + 3) / 2 = 2.5
```

## Constraints
- 0 <= m, n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6
- Both nums1 and nums2 are sorted in non-decreasing order.

## Clarifications & Assumptions
- The overall run time complexity should be O(log(min(m, n))).
- The arrays may be of different lengths.
- The median is the middle value if the total number of elements is odd, or the average of the two middle values if even.
- Both arrays may be empty, but not at the same time.

## Approach Hints
- Consider binary search on the smaller array.
- Think about partitioning the arrays so that the left and right halves have equal length.
- Handle edge cases where one array is empty. 
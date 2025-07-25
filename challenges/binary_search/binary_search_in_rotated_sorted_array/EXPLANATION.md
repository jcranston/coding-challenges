# Binary Search in Rotated Sorted Array — EXPLANATION

## Problem Recap
Given a rotated sorted array of distinct integers `nums` and an integer `target`, return the index of `target` if it is in `nums`, or -1 if it is not in `nums`. The array was originally sorted in ascending order and then rotated at some unknown pivot. Must run in O(log n) time.

## High-Level Approach
Use a modified binary search. At each step, determine which half of the array is sorted, and decide which half to search based on the target's value.

## Step-by-Step Solution
1. Initialize two pointers, `left` and `right`, at the start and end of the array.
2. While `left <= right`:
    - Compute `mid` as the average of `left` and `right`.
    - If `nums[mid]` is the target, return `mid`.
    - Determine which half is sorted:
        - If `nums[left] <= nums[mid]`, the left half is sorted.
            - If `nums[left] <= target < nums[mid]`, search left half (`right = mid - 1`).
            - Else, search right half (`left = mid + 1`).
        - Else, the right half is sorted.
            - If `nums[mid] < target <= nums[right]`, search right half (`left = mid + 1`).
            - Else, search left half (`right = mid - 1`).
3. If the loop ends, return -1 (target not found).

## Annotated Code
```python
def binary_search_in_rotated_sorted_array(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

## Example Test Cases
```python
assert binary_search_in_rotated_sorted_array([4,5,6,7,0,1,2], 0) == 4
assert binary_search_in_rotated_sorted_array([4,5,6,7,0,1,2], 3) == -1
assert binary_search_in_rotated_sorted_array([1], 0) == -1
```

## Common Pitfalls
- Not handling the case where the array is not rotated (fully sorted).
- Off-by-one errors in pointer updates.
- Not considering all edge cases (target at pivot, single-element array, negative numbers).

## Variations
- Array contains duplicates (requires extra logic).
- Find the minimum in a rotated sorted array.

## References
- [LeetCode #33: Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [Binary Search Pattern](https://leetcode.com/problems/search-in-rotated-sorted-array/solutions/) 
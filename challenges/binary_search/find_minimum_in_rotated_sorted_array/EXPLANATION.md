# Find Minimum in Rotated Sorted Array — EXPLANATION

## Problem Recap
Given a rotated sorted array `nums`, return the minimum element. The array is a rotated version of a sorted array, and all elements are unique.

## High-Level Approach
Use binary search to find the inflection point where the rotation occurs. The minimum element is the only element that is smaller than its previous element, or the leftmost element when the array is not rotated.

## Step-by-Step Solution
1. Initialize two pointers, `left` and `right`, at the start and end of the array.
2. While `left < right`:
    - Compute `mid` as the average of `left` and `right`.
    - If `nums[mid] > nums[right]`, the minimum is to the right of `mid` (`left = mid + 1`).
    - Otherwise, the minimum is at `mid` or to the left (`right = mid`).
3. When the loop ends, `left` points to the minimum element.

## Annotated Code
```python
from typing import List

def find_minimum_in_rotated_sorted_array(nums: List[int]) -> int:
    n = len(nums)
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
```

## Example Test Cases
```python
assert find_minimum_in_rotated_sorted_array([3,4,5,1,2]) == 1
assert find_minimum_in_rotated_sorted_array([4,5,6,7,0,1,2]) == 0
assert find_minimum_in_rotated_sorted_array([11,13,15,17]) == 11
```

## Common Pitfalls
- Not handling the case where the array is not rotated (minimum is the first element).
- Off-by-one errors in pointer updates.
- Assuming all elements are unique (problem constraint).

## Variations
- Array contains duplicates (requires extra logic).
- Find the maximum in a rotated sorted array.

## References
- [LeetCode #153: Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
- [Binary Search Pattern](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/) 
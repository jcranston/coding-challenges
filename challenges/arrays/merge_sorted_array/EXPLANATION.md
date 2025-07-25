# Merge Sorted Array — EXPLANATION

## Problem Recap
Given two sorted integer arrays `nums1` and `nums2`, merge `nums2` into `nums1` as one sorted array in-place. `nums1` has enough space to hold all elements.

## High-Level Approach
Use two pointers starting from the end of the initialized parts of `nums1` and `nums2`, and fill `nums1` from the back to avoid overwriting values.

## Step-by-Step Solution
1. Set three pointers:
    - `p1` at the end of the initialized part of `nums1` (m - 1)
    - `p2` at the end of `nums2` (n - 1)
    - `p` at the end of `nums1` (m + n - 1)
2. While both `p1` and `p2` are valid:
    - Compare `nums1[p1]` and `nums2[p2]`.
    - Place the larger at `nums1[p]` and move the corresponding pointer backward.
    - Move `p` backward.
3. If any elements remain in `nums2`, copy them into `nums1`.

## Annotated Code
```python
from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
```

## Example Test Cases
```python
nums1 = [1,2,3,0,0,0]; m = 3
nums2 = [2,5,6]; n = 3
merge(nums1, m, nums2, n)
assert nums1 == [1,2,2,3,5,6]
```

## Common Pitfalls
- Overwriting values in `nums1` by merging from the front.
- Not handling the case where `nums2` has remaining elements after `nums1` is exhausted.
- Not considering edge cases where one array is empty.

## Variations
- Merge k sorted arrays (generalization).
- Return a new array instead of modifying in-place.

## References
- [LeetCode #88: Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
- [Two Pointer Pattern](https://leetcode.com/problems/merge-sorted-array/solutions/) 
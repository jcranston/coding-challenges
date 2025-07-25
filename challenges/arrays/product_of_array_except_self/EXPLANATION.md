# Product of Array Except Self — EXPLANATION

## Problem Recap
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The solution must be done in O(n) time and without using division.

## High-Level Approach
The trick is to compute the product of all elements to the left and right of each index, then multiply them. This can be done in two passes: one forward (prefix products) and one backward (suffix products).

## Step-by-Step Solution
1. Initialize an output array of length n, filled with 1s.
2. Compute prefix products:
    - For each index i from left to right, set output[i] to the product of all elements to the left of i.
3. Compute suffix products:
    - For each index i from right to left, multiply output[i] by the product of all elements to the right of i.
4. Return the output array.

## Annotated Code
```python
def product_of_array_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    output = [1] * n
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]
    return output
```

## Example Test Cases
```python
assert product_of_array_except_self([1,2,3,4]) == [24,12,8,6]
assert product_of_array_except_self([-1,1,0,-3,3]) == [0,0,9,0,0]
```

## Common Pitfalls
- Using division (not allowed by the problem statement).
- Not handling zeros correctly (if there are multiple zeros, all outputs are zero).
- Forgetting to initialize prefix and suffix to 1.

## Variations
- What if you are allowed to use division?
- What if the array contains very large or very small numbers (overflow)?

## References
- [LeetCode #238: Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
- [Prefix Product Pattern](https://leetcode.com/problems/product-of-array-except-self/solutions/) 
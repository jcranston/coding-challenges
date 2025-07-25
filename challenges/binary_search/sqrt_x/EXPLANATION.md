# Explanation: Sqrt(x) (LeetCode 69)

## Problem Recap
Given a non-negative integer `x`, return the integer square root of `x` (the greatest integer `y` such that `y*y <= x`). Do not use built-in exponent functions.

## High-Level Approach
Use binary search to efficiently find the integer square root. For each mid, check if `mid*mid <= x < (mid+1)*(mid+1)`.

## Annotated Canonical Solution
```python
def canonical_sqrt_x(x: int) -> int:
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right
```
- This approach is O(log x) time and O(1) space.
- **Why return `right`?**
  - If `mid * mid == x` is never satisfied, the loop exits when `left > right`.
  - At this point, `right` is the largest integer such that `right * right <= x` (since `left` is the first value where `left * left > x`).
  - Returning `right` ensures we get the integer part of the square root, as required by the problem.

## Test Cases & Edge Cases
- `x = 0` → `0`
- `x = 1` → `1`
- `x = 4` → `2`
- `x = 8` → `2`
- `x = 2147395599` → `46339`

## Common Pitfalls
- Off-by-one errors in binary search.
- Not handling `x = 0` or `x = 1` correctly.
- Returning `left` instead of `right` (which would be incorrect if `mid * mid == x` is never hit).

## Relevant Literature
- [LeetCode 69: Sqrt(x)](https://leetcode.com/problems/sqrtx/)

---
This explanation is concise due to the simplicity of the problem, as recommended in `ai_context/explanation_generation.md`. 
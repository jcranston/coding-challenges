**LeetCode #69**  
**Tags:** math, binary search

# Sqrt(x)

Given a non-negative integer `x`, compute and return the integer square root of `x`. The integer square root is the greatest integer `y` such that `y*y <= x`.

## Example
```
Input: x = 4
Output: 2

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.828..., and since we want the integer part, the answer is 2.
```

## Constraints
- 0 <= x <= 2^31 - 1

## Clarifications & Assumptions
- The function should return the integer part of the square root (i.e., `floor(sqrt(x))`).
- Do not use any built-in exponent function or operator (e.g., `pow(x, 0.5)` or `x ** 0.5`).

## Approach
- Use binary search to find the integer square root efficiently.
- Start with `left = 0` and `right = x`. For each mid, check if `mid*mid <= x < (mid+1)*(mid+1)`.

## Notes
- Edge cases: x = 0, x = 1, very large x.
- Time complexity: O(log x).
- Space complexity: O(1). 
**LeetCode #202**  
**Tags:** math, hash set, cycle detection

# Happy Number

## Problem
Write an algorithm to determine if a number n is a happy number.

A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

## Examples

### Example 1
```
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```

### Example 2
```
Input: n = 2
Output: false
```

## Constraints
- 1 <= n <= 2^31 - 1

## Clarifications & Assumptions
- The process is repeated until n becomes 1 or a cycle is detected.
- The function should return a boolean indicating if n is happy.

## Approach
- Use a hash set to track numbers seen so far to detect cycles.
- Alternatively, use Floyd's cycle detection (tortoise and hare) for O(1) space.
- Time complexity: O(log n) per iteration, total iterations are bounded.

## Notes
- Edge cases: n = 1 (always happy), n = 0 (not happy), large n.
- This is a classic interview problem for cycle detection and digit manipulation. 
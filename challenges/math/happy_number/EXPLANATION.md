# Explanation: Happy Number (LeetCode 202)

## Problem Recap
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Return true if n is a happy number, and false if not.

## High-Level Approach
The main challenge is to detect if the process enters a cycle. The most common approach is to use a hash set to track numbers seen so far. If a number repeats, a cycle exists and n is not happy. Alternatively, Floyd's cycle detection algorithm (tortoise and hare) can be used for O(1) space.

## Step-by-Step Breakdown
1. **Initialize a set to track seen numbers.**
2. **Repeat the process:**
   - Replace n with the sum of the squares of its digits.
   - If n becomes 1, return True.
   - If n is already in the set, return False (cycle detected).
3. **Alternative:** Use two pointers (slow and fast) to detect a cycle without extra space.

## Annotated Canonical Solution
```python
def canonical_is_happy(n: int) -> bool:
    def get_next(x):
        return sum(int(d) ** 2 for d in str(x))
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1
```
- **Why this works:**
  - If n becomes 1, it is happy. If n repeats, a cycle exists and n is not happy.

## Alternative: Algorithmic Digit Extraction (Division/Modulo)
A more algorithmic approach (often preferred in interviews) extracts digits using division and modulo:

```python
def get_next(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** 2
        n //= 10
    return total
```
- This avoids string conversion and demonstrates understanding of number manipulation.
- Both approaches are valid, but the division/modulo method is more efficient and language-agnostic.

## Test Cases & Edge Cases
- `19`
# Palindrome Number — EXPLANATION

## Problem Recap
Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise. A palindrome reads the same backward as forward. Negative numbers are not palindromes.

## High-Level Approach
Reverse the digits of the number and compare to the original. For efficiency, only reverse half of the number and compare.

## Step-by-Step Solution
1. If `x` is negative or ends with 0 (but is not 0), return `False`.
2. Initialize `reversed_num` to 0.
3. While `x` is greater than `reversed_num`:
    - Add the last digit of `x` to `reversed_num`.
    - Remove the last digit from `x`.
4. For even-length numbers, check if `x == reversed_num`.
5. For odd-length numbers, check if `x == reversed_num // 10` (middle digit doesn't matter).

## Annotated Code
```python
def palindrome_number(x: int) -> bool:
    # Negative numbers and numbers ending in 0 (except 0 itself) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reversed_num = 0
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    # For even length: x == reversed_num
    # For odd length:  x == reversed_num // 10
    return x == reversed_num or x == reversed_num // 10
```

## Example Test Cases
```python
assert palindrome_number(121) == True
assert palindrome_number(-121) == False
assert palindrome_number(10) == False
assert palindrome_number(0) == True
```

## Common Pitfalls
- Not handling negative numbers or numbers ending in 0 (except 0 itself).
- Reversing the entire number (can cause overflow in some languages, but not in Python).
- Not considering odd vs. even length numbers.

## Variations
- Check if a string is a palindrome (ignoring non-alphanumeric characters).
- Find the largest palindromic number less than a given number.

## References
- [LeetCode #9: Palindrome Number](https://leetcode.com/problems/palindrome-number/)
- [Digit Manipulation](https://leetcode.com/problems/palindrome-number/solutions/) 
# Explanation: Valid Palindrome (LeetCode 125)

## Problem Recap
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

## Approach
- Use two pointers (left and right) to scan the string from both ends.
- Move the left pointer forward until it points to an alphanumeric character.
- Move the right pointer backward until it points to an alphanumeric character.
- Compare the characters at the two pointers (case-insensitive).
- If they differ, return False. If they match, move both pointers inward and continue.
- If the pointers cross, the string is a palindrome.

## Code Reasoning
- The two-pointer approach efficiently checks for palindromes in O(n) time.
- Skipping non-alphanumeric characters ensures only relevant characters are compared.
- Lowercasing ensures case-insensitive comparison.

## Edge Cases
- Empty string: considered a palindrome.
- String with only non-alphanumeric characters: considered a palindrome.
- Mixed case: handled by lowercasing.

## Why Use Two Pointers?
- Efficiently compares characters from both ends.
- Avoids extra space for filtered strings.

## Related Literature
- Two-pointer palindrome checking is a classic algorithm (see CLRS, Chapter 2).
- LeetCode Discuss: [Valid Palindrome - Two Pointers](https://leetcode.com/problems/valid-palindrome/solutions/31247/python-in-place-2-pointer-solution/)

## Invariants
- At each step, the pointers reference the next alphanumeric characters to compare.
- The function returns as soon as a mismatch is found.

## Code Example
```python
def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
``` 
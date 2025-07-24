# Explanation: Reverse Vowels of a String (LeetCode 345)

## Problem Recap
Given a string s, reverse only all the vowels in the string and return it. The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases.

## Approach
- Use two pointers (left and right) to scan the string from both ends.
- Move the left pointer forward until it finds a vowel.
- Move the right pointer backward until it finds a vowel.
- Swap the vowels at the two pointers.
- Continue until the pointers meet.

## Code Reasoning
- The two-pointer approach is efficient for in-place reversal.
- Vowel checking is case-insensitive.
- The algorithm only swaps vowels, leaving other characters in place.

## Edge Cases
- No vowels: string remains unchanged.
- All vowels: string is fully reversed.
- Mixed case: both 'A' and 'a' are considered vowels.

## Why Use Two Pointers?
- Efficiently reverses only the vowels in a single pass.
- Avoids extra space for non-vowel characters.

## Related Literature
- Two-pointer techniques are common for in-place string/array manipulation (see CLRS, Chapter 2).
- LeetCode Discuss: [Reverse Vowels of a String - Two Pointers](https://leetcode.com/problems/reverse-vowels-of-a-string/solutions/81164/clear-python-solution/)

## Invariants
- All non-vowel characters remain in their original positions.
- The order of vowels is reversed.

## Code Example
```python
def reverse_vowels(s):
    vowels = set('aeiouAEIOU')
    s = list(s)
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and s[l] not in vowels:
            l += 1
        while l < r and s[r] not in vowels:
            r -= 1
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return ''.join(s)
``` 
# Longest Palindromic Substring — EXPLANATION

## Problem Recap
Given a string `s`, return the longest palindromic substring in `s`. A palindrome is a string that reads the same forward and backward. If multiple answers exist, return any one.

## High-Level Approach
The most efficient approach is to expand around each possible center of a palindrome. For each character (and each gap between characters), expand outward as long as the substring remains a palindrome, tracking the longest found.

## Step-by-Step Solution
1. For each index in the string, treat it as the center of a potential palindrome.
2. Expand around the center for both odd-length and even-length palindromes.
3. For each expansion, if the resulting palindrome is longer than the current longest, update the result.
4. Return the longest palindrome found.

## Annotated Code
```python
def longest_palindromic_substring(s: str) -> str:
    """
    Finds the longest palindromic substring in s using the expand around center approach.
    """
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    longest = ""
    for i in range(len(s)):
        # Odd length
        p1 = expand_around_center(i, i)
        # Even length
        p2 = expand_around_center(i, i + 1)
        if len(p1) > len(longest):
            longest = p1
        if len(p2) > len(longest):
            longest = p2
    return longest
```

## Example Test Cases
```python
assert longest_palindromic_substring("babad") in ("bab", "aba")
assert longest_palindromic_substring("cbbd") == "bb"
assert longest_palindromic_substring("a") == "a"
assert longest_palindromic_substring("ac") in ("a", "c")
```

## Common Pitfalls
- Not checking both odd and even length centers.
- Not handling single-character or empty strings.
- Returning the first palindrome found instead of the longest.

## Variations
- Return all longest palindromic substrings if there are multiple.
- Find the longest palindromic subsequence (not necessarily contiguous).

## References
- [LeetCode #5: Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- [Expand Around Center Approach](https://leetcode.com/problems/longest-palindromic-substring/solutions/2972/) 
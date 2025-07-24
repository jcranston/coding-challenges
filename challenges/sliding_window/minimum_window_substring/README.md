**LeetCode #76**  
**Tags:** strings, sliding window, hash table, two pointers

# Minimum Window Substring

## Problem
Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

## Examples
- Input: `s = "ADOBECODEBANC"`, `t = "ABC"`
  Output: `"BANC"`
- Input: `s = "a"`, `t = "a"`
  Output: `"a"`
- Input: `s = "a"`, `t = "aa"`
  Output: `""`

## Constraints
- 1 <= s.length, t.length <= 10^5
- s and t consist of English letters.

## Clarifications
- The answer is unique if it exists.
- If t's characters are not all present in s, return `""`.
- The search is case-sensitive.
- All assumptions are clarified above. 
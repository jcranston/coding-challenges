**LeetCode #424**  
**Tags:** strings, sliding window, hash table

# Longest Repeating Character Replacement

## Problem
Given a string `s` and an integer `k`, return the length of the longest substring containing the same letter you can get after performing at most `k` character replacements.

## Example
```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' to form "AABBBBA".
```

## Constraints
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.
- 0 <= k <= s.length

## Clarifications & Assumptions
- You can replace any character in the string with any uppercase English letter.
- The substring must be contiguous.
- If k = 0, you cannot make any replacements.

## Approach
Describe your approach and thought process after attempting the problem. Consider using a sliding window and hash map for optimal performance.

## Notes
- Edge cases: k = 0, all characters the same, k >= s.length, multiple optimal substrings, empty string (not allowed by constraints). 
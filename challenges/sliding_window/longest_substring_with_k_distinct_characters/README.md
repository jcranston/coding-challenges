**LeetCode #340**
**LeetCode Problem: Longest Substring with At Most K Distinct Characters**

**Tags:** string, sliding window, hash table, two pointers

# Longest Substring with K Distinct Characters

## Problem

Given a string `s` and an integer `k`, return the length of the longest substring of `s` that contains at most `k` distinct characters.

## Examples

**Example 1:**
```
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
```

**Example 2:**
```
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
```

**Example 3:**
```
Input: s = "eceba", k = 1
Output: 1
Explanation: Any single character substring has length 1.
```

## Constraints

- `1 <= s.length <= 5 * 10^4`
- `0 <= k <= 50`
- `s` consists of only lowercase English letters.

## Clarifications & Assumptions

- The substring must be contiguous (not just any subsequence).
- If `k = 0`, the result should be 0 (no valid substring).
- If `k` is greater than or equal to the number of unique characters in the string, the result is the length of the entire string.
- The problem asks for "at most k distinct characters", so a substring with fewer than k distinct characters is also valid.
- The input string can be empty, in which case the result is 0.

## Notes

- This is a classic problem that appears frequently in coding interviews.
- Think about how to efficiently track the characters in a substring.
- Consider what happens when you need to expand or contract your search window. 
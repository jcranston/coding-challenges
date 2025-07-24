**LeetCode #727**  
**Tags:** two pointers, dynamic programming, string

# Minimum Window Subsequence

## Problem
Given two strings `s1` and `s2`, return the minimum window in `s1` which will contain all the characters in `s2` in order (as a subsequence). If there is no such window in `s1` that covers all characters in `s2`, return the empty string `""`.

## Example
```
Input: s1 = "abcdebdde", s2 = "bde"
Output: "bcde"
Explanation: "bcde" is the shortest substring of "abcdebdde"
where "bde" appears as a subsequence.

Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
Output: ""
```

## Constraints
- 1 <= s1.length, s2.length <= 2000
- s1 and s2 consist of lowercase English letters.

## Clarifications & Assumptions
- The window must contain all characters of s2 in order (as a subsequence, not necessarily contiguous).
- If multiple such windows exist, return the one with the left-most starting index.
- If no such window exists, return the empty string.

## Approach
Describe your approach and thought process after attempting the problem. Consider two pointers and dynamic programming for optimal performance.

## Notes
- Edge cases: s2 longer than s1, s2 not a subsequence of s1, multiple minimum windows, s2 is empty. 
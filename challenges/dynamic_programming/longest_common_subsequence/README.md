LeetCode #1143
LeetCode Problem: Longest Common Subsequence

# Longest Common Subsequence

**Tags:** dynamic programming, string, memoization, tabulation

## Problem

Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

## Examples

**Example 1:**
```
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
```

**Example 2:**
```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

**Example 3:**
```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

## Constraints

- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist only of lowercase English characters.

## Clarifications & Assumptions

- A subsequence does not need to be contiguous.
- The order of characters must be preserved from the original string.
- If either string is empty, the LCS length is 0.
- The problem asks for the length of the LCS, not the actual subsequence itself.
- Both strings contain only lowercase English letters.

## Approach

This problem can be solved using dynamic programming with two main approaches:

1. **Top-down (Memoization):** Use recursion with memoization to avoid redundant calculations
2. **Bottom-up (Tabulation):** Build the solution iteratively from smaller subproblems

Both approaches use the same recurrence relation:
- If characters match: `dp[i][j] = 1 + dp[i+1][j+1]`
- If characters don't match: `dp[i][j] = max(dp[i+1][j], dp[i][j+1])`

## Notes

- The top-down approach is more intuitive but may have stack overflow for very large strings
- The bottom-up approach is more space-efficient and avoids recursion overhead
- Time complexity: O(m*n) where m and n are the lengths of the strings
- Space complexity: O(m*n) for the DP table
- This is a classic dynamic programming problem that appears frequently in interviews 
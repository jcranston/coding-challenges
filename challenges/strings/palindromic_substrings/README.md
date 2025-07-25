**LeetCode #647**  
**Tags:** string, dynamic programming, expand around center

# Palindromic Substrings

## Problem
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

## Examples

### Example 1
```
Input: s = "abc"
Output: 3
Explanation: Three palindromic substrings: "a", "b", "c".
```

### Example 2
```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic substrings: "a", "a", "a", "aa", "aa", "aaa".
```

## Constraints
- 1 <= s.length <= 1000
- s consists of lowercase English letters.

## Clarifications & Assumptions
- Each single character is a palindrome.
- Substrings can overlap.
- The function should return the total count of palindromic substrings.

## Approach
- Use dynamic programming or expand around center to count all palindromic substrings.
- For each center (single character or between two characters), expand as long as the substring is a palindrome.
- Time complexity: O(n^2), space complexity: O(1) for expand around center, O(n^2) for DP.

## Notes
- Edge cases: all unique characters, all same characters, single character string.
- This is a classic string and palindrome problem. 
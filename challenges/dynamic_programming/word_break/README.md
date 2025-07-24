**LeetCode #139**  
**Tags:** dynamic programming, string, hash table, trie, memoization

# Word Break

## Problem
Given a string `s` and a dictionary of strings `wordDict`, return `True` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

## Examples
```
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: True
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: True
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: False
```

## Constraints
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters.
- All the strings in wordDict are unique.

## Clarifications & Assumptions
- The same word in the dictionary may be reused multiple times in the segmentation.
- The dictionary is a list of unique words.

## Approach Hints
- Consider using dynamic programming with a boolean array dp where dp[i] is True if s[:i] can be segmented.
- Use a set for fast word lookup. 
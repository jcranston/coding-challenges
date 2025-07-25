# Explanation: Word Break

## Problem Recap
Given a string `s` and a dictionary of strings `wordDict`, return `True` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

## High-level Approach
This is a classic dynamic programming problem. The main idea is to use a boolean DP array where `dp[i]` is `True` if the substring `s[:i]` can be segmented into words from the dictionary.

## Step-by-step Breakdown
1. **DP Table Definition:**
   - Let `dp[i]` be `True` if `s[:i]` can be segmented into words from `wordDict`.
2. **Initialization:**
   - `dp[0] = True` (empty string can always be segmented).
3. **DP Transition:**
   - For each `i` from 1 to `len(s)`, check all `j < i`:
     - If `dp[j]` is `True` and `s[j:i]` is in `wordDict`, set `dp[i] = True`.
   - Use a set for `wordDict` for O(1) lookups.
4. **Result:**
   - The answer is `dp[len(s)]`.

## Annotated Code (Canonical Solution)
```python
from typing import List

def word_break(s: str, wordDict: List[str]) -> bool:
    word_set = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[n]
```
- The outer loop considers all possible end positions, and the inner loop checks all possible start positions for a valid word.
- Time complexity is O(n² * k), where n is the length of `s` and k is the average word length.

## Test Cases
- `s = "leetcode", wordDict = ["leet", "code"]` → Output: `True`
- `s = "applepenapple", wordDict = ["apple", "pen"]` → Output: `True`
- `s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]` → Output: `False`

## Common Pitfalls
- Not initializing `dp[0]` to `True`.
- Not using a set for fast word lookups.
- Forgetting that words can be reused multiple times.

## Variations
- If you want to return the actual segmentation, you can keep track of the splits.
- If you want to count the number of ways to segment, use a count DP instead of boolean.

## Relevant Literature
- [LeetCode #139: Word Break](https://leetcode.com/problems/word-break/)
- [Dynamic Programming for String Segmentation](https://leetcode.com/tag/dynamic-programming/)
- CLRS, Section 15.3: Dynamic Programming 
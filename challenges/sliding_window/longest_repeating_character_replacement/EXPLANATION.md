# Explanation: Longest Repeating Character Replacement

## Problem Recap
Given a string `s` and an integer `k`, return the length of the longest substring containing the same letter you can get after performing at most `k` character replacements.

## High-level Approach
A brute-force approach would check all substrings, but this is inefficient for large strings. The optimal solution uses a sliding window and a hash map to efficiently track the counts of characters in the current window.

## Step-by-step Breakdown
1. **Sliding Window:**
   - Use two pointers (`left` and `right`) to represent the current window.
   - Expand the window by moving `right` and updating the count of the current character.
2. **Track Most Frequent Character:**
   - Keep track of the count of the most frequent character in the current window (`max_count`).
   - The minimum number of replacements needed to make all characters in the window the same is `(window size) - max_count`.
3. **Shrink Window if Needed:**
   - If the number of replacements needed exceeds `k`, move `left` to shrink the window until it is valid again.
4. **Result:**
   - The answer is the maximum window size found during the process.

## Annotated Code
```python
from collections import defaultdict

def longest_repeating_character_replacement(s, k):
    count = defaultdict(int)
    max_count = 0
    left = 0
    result = 0
    for right in range(len(s)):
        count[s[right]] += 1
        max_count = max(max_count, count[s[right]])
        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1
        result = max(result, right - left + 1)
    return result
```
- The window is expanded and contracted to always maintain the maximum valid window.
- Time complexity is O(n), where n is the length of `s`.

## Test Cases
- `s = "ABAB", k = 2` → Output: 4
- `s = "AABABBA", k = 1` → Output: 4
- `s = "AAAA", k = 2` → Output: 4
- `s = "ABCD", k = 0` → Output: 1
- `s = "AABACCAABBAA", k = 3` → Output: 8

## Common Pitfalls
- Not updating `max_count` correctly as the window moves.
- Forgetting to shrink the window when replacements exceed `k`.
- Not handling edge cases like `k = 0` or all characters the same.

## Variations
- If you want to return the actual substring, keep track of the window indices.
- If the string contains lowercase letters, adjust the hash map accordingly.

## Relevant Literature
- [LeetCode #424: Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
- [Sliding Window Technique](https://leetcode.com/tag/sliding-window/)
- CLRS, Section 32.2: String Matching 
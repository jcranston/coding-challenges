# Explanation: Minimum Window Substring

## Problem Recap
Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

## High-level Approach
A brute-force approach would check all substrings, but this is inefficient for large strings. The optimal solution uses a sliding window with two pointers and hash maps to efficiently track the required characters and their counts.

## Step-by-step Breakdown
1. **Character Counts:**
   - Use a hash map (Counter) to store the required counts of each character in `t`.
   - Use another hash map to track the counts of characters in the current window of `s`.
2. **Sliding Window:**
   - Expand the window by moving the right pointer and updating the window counts.
   - When the window contains all required characters (with correct counts), try to shrink the window from the left to find the minimum.
   - Update the result whenever a smaller valid window is found.
3. **Result:**
   - If a valid window is found, return the substring. Otherwise, return `""`.

## Annotated Code
```python
from collections import Counter, defaultdict

def min_window_substring(s, t):
    if not t or not s:
        return ""
    need = Counter(t)
    window = defaultdict(int)
    have, required = 0, len(need)
    res = (float("inf"), None, None)
    left = 0
    for right, char in enumerate(s):
        window[char] += 1
        if char in need and window[char] == need[char]:
            have += 1
        while have == required:
            if (right - left + 1) < res[0]:
                res = (right - left + 1, left, right)
            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1
            left += 1
    _, l, r = res
    if l is not None and r is not None:
        return s[l : r + 1]
    else:
        return ""
```
- The window is expanded and contracted to always maintain the minimum valid window.
- Time complexity is O(|s| + |t|), where |s| and |t| are the lengths of the strings.

## Test Cases
- `s = "ADOBECODEBANC", t = "ABC"` → Output: `"BANC"`
- `s = "a", t = "a"` → Output: `"a"`
- `s = "a", t = "aa"` → Output: `""`
- `s = "abc", t = "d"` → Output: `""`
- `s = "abdecfab", t = "abc"` → Output: `"cfab"`

## Common Pitfalls
- Not handling duplicate characters in `t` correctly.
- Forgetting to shrink the window from the left after finding a valid window.
- Not updating the result when a smaller valid window is found.

## Variations
- If you want the maximum window containing all characters, adjust the shrinking logic.
- If the answer is not unique, return any valid minimum window.

## Relevant Literature
- [LeetCode #76: Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [Sliding Window Technique](https://leetcode.com/tag/sliding-window/)
- CLRS, Section 32.2: String Matching 
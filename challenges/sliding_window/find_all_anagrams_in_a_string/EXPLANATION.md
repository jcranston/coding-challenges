# Explanation: Find All Anagrams in a String

## Problem Recap
Given two strings `s` and `p`, return a list of all the start indices of `p`'s anagrams in `s`. An anagram is a permutation of all the characters in `p`.

## High-level Approach
A brute-force approach would check every substring of length `len(p)` in `s` to see if it is an anagram of `p`, but this is inefficient. The optimal solution uses a sliding window and character counts to efficiently check for anagrams in O(n) time.

## Step-by-step Breakdown
1. **Character Counts:**
   - Use a hash map or fixed-size array to store the counts of each character in `p`.
   - Maintain a window of length `len(p)` in `s` and track the counts of characters in the current window.
2. **Sliding Window:**
   - Slide the window one character at a time, updating the counts as you go.
   - If the counts in the window match the counts in `p`, record the starting index.
3. **Result:**
   - Return the list of all starting indices where an anagram of `p` begins in `s`.

## Annotated Code (Canonical Solution)
```python
from typing import List

def find_all_anagrams(s: str, p: str) -> List[int]:
    if len(p) > len(s):
        return []
    res = []
    p_count = [0] * 26
    s_count = [0] * 26
    a_ord = ord("a")
    for c in p:
        p_count[ord(c) - a_ord] += 1
    for i in range(len(p)):
        s_count[ord(s[i]) - a_ord] += 1
    if s_count == p_count:
        res.append(0)
    for i in range(len(p), len(s)):
        s_count[ord(s[i]) - a_ord] += 1
        s_count[ord(s[i - len(p)]) - a_ord] -= 1
        if s_count == p_count:
            res.append(i - len(p) + 1)
    return res
```
- The window is updated in O(1) time per step, and the counts are compared for equality.
- Time complexity is O(n), where n is the length of `s`.

## Test Cases
- `s = "cbaebabacd", p = "abc"` → Output: `[0, 6]`
- `s = "abab", p = "ab"` → Output: `[0, 1, 2]`
- `s = "a", p = "a"` → Output: `[0]`
- `s = "a", p = "b"` → Output: `[]`
- `s = "baa", p = "aa"` → Output: `[1]`

## Common Pitfalls
- Not updating the window counts correctly when sliding.
- Not handling the case where `p` is longer than `s`.
- Forgetting to check the first window before sliding.

## Variations
- If the string contains uppercase letters, increase the size of the count arrays.
- If you want to return the actual substrings, store them instead of indices.

## Relevant Literature
- [LeetCode #438: Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
- [Sliding Window Technique](https://leetcode.com/tag/sliding-window/)
- CLRS, Section 32.2: String Matching 
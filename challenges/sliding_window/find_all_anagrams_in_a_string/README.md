**LeetCode #438**  
**Tags:** strings, sliding window, hash table

# Find All Anagrams in a String

## Problem
Given two strings `s` and `p`, return a list of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples
- Input: s = "cbaebabacd", p = "abc"
  Output: [0, 6]
  Explanation: The substring with start index = 0 is "cba", which is an anagram of "abc". The substring with start index = 6 is "bac", which is an anagram of "abc".

- Input: s = "abab", p = "ab"
  Output: [0, 1, 2]
  Explanation: The substring with start index = 0 is "ab", which is an anagram of "ab". The substring with start index = 1 is "ba", which is an anagram of "ab". The substring with start index = 2 is "ab", which is an anagram of "ab".

## Constraints
- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters.

## Clarifications
- The returned list should contain all starting indices of substrings in `s` that are anagrams of `p`.
- If there are no anagrams, return an empty list.
- All values in the returned list should be unique and in any order. 
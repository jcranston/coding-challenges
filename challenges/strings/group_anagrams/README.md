**LeetCode #49**  
**Tags:** strings, hash table, sorting

# Group Anagrams

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

## Example

```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
```

## Constraints
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

## Clarifications / Assumptions
- Each string consists of lowercase English letters only (a-z).
- The output should be a list of lists, where each sublist contains anagrams grouped together.
- The order of groups and the order of strings within each group does not matter.
- An anagram is a word formed by rearranging the letters of another word. 
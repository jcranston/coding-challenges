# Group Anagrams — EXPLANATION

## Problem Recap
Given an array of strings, group the anagrams together. An anagram is a word formed by rearranging the letters of another word. The order of groups and the order of strings within each group does not matter.

## High-Level Approach
The key insight is that all anagrams, when sorted alphabetically, yield the same string. We can use this property to group words efficiently using a hash table.

## Step-by-Step Solution
1. Initialize a hash table (dictionary) where the key is the sorted version of a string, and the value is a list of all strings that, when sorted, match that key.
2. Iterate through each string in the input list:
    - Sort the string alphabetically.
    - Use the sorted string as a key and append the original string to the corresponding list in the hash table.
3. Return the values of the hash table as the grouped anagrams.

## Annotated Code
```python
from collections import defaultdict
from typing import List

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups anagrams together from a list of strings.
    """
    sorted_to_anagrams = defaultdict(list)
    for s in strs:
        # Sort the string to get the key
        key = "".join(sorted(s))
        sorted_to_anagrams[key].append(s)
    return list(sorted_to_anagrams.values())
```

## Example Test Cases
```python
assert sorted([sorted(g) for g in group_anagrams(["eat","tea","tan","ate","nat","bat"])]) == sorted([sorted(["eat","tea","ate"]), sorted(["tan","nat"]), ["bat"]])
assert group_anagrams([""]) == [[""]]
assert group_anagrams(["a"]) == [["a"]]
```

## Common Pitfalls
- Not sorting the string before using it as a key (will not group anagrams correctly).
- Forgetting that the order of groups and the order within groups does not matter.
- Not handling empty strings or single-character strings.

## Variations
- Return the groups in a specific order (e.g., lexicographically sorted groups).
- Grouping anagrams for very large datasets (may require more memory-efficient approaches).

## References
- [LeetCode #49: Group Anagrams](https://leetcode.com/problems/group-anagrams/)
- Python documentation: [collections.defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict) 
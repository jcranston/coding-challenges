# Find the First Unique Character in a String — EXPLANATION

## Problem Recap
Given a string `s`, return the index of the first non-repeating character in it. If there is no such character, return `-1`.

## High-Level Approach
Use a hash table (Counter) to count the frequency of each character, then scan the string to find the first character with a count of 1.

## Step-by-Step Solution
1. Count the frequency of each character in the string using `collections.Counter`.
2. Iterate through the string by index:
    - For each character, check if its count is 1.
    - If so, return the index.
3. If no unique character is found, return -1.

## Annotated Code
```python
from collections import Counter

def find_first_unique_character(s: str) -> int:
    """
    Given a string s, return the index of the first non-repeating character in it. If there is no such character, return -1.
    """
    hist = Counter(s)
    for idx, c in enumerate(s):
        if hist[c] == 1:
            return idx
    return -1
```

## Example Test Cases
```python
assert find_first_unique_character("adobe") == 0  # 'a' is unique
assert find_first_unique_character("leetcode") == 0  # 'l' is unique
assert find_first_unique_character("aabb") == -1  # no unique character
```

## Common Pitfalls
- Not handling the case where there is no unique character (should return -1).
- Not considering all characters (should check every index).
- Assuming the string only contains lowercase letters (as per constraints).

## Variations
- Return the unique character itself instead of its index.
- Find the last unique character instead of the first.
- Handle Unicode or mixed-case strings.

## References
- [LeetCode #387: First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)
- Python documentation: [collections.Counter](https://docs.python.org/3/library/collections.html#collections.Counter) 
# Valid Anagram

Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.

## Example

```
Input: s = "anagram", t = "nagaram"
Output: True

Input: s = "rat", t = "car"
Output: False
```

## Constraints
- 1 <= s.length, t.length <= 5 * 10^4
- `s` and `t` consist of lowercase English letters.

## Clarifications / Assumptions
- Both strings contain only lowercase English letters (a-z).
- The order of characters in the strings does not matter for anagrams.
- The function should be case-sensitive (i.e., 'A' and 'a' are different if present).
- Return a boolean value: `True` if `t` is an anagram of `s`, otherwise `False`. 
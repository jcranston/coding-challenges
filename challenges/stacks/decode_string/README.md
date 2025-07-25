**LeetCode #394**  
**Tags:** stack, string, decoding

# Decode String

## Problem
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; no extra white spaces, square brackets are well-formed, etc.

## Examples

### Example 1
```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```

### Example 2
```
Input: s = "3[a2[c]]"
Output: "accaccacc"
```

### Example 3
```
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

## Constraints
- 1 <= s.length <= 30
- s consists of only lowercase English letters, digits, and square brackets '[]'.
- s is guaranteed to be a valid input.
- All the integers in s are in the range [1, 300].

## Clarifications & Assumptions
- The input string is always valid and well-formed.
- Nested encodings are possible.

## Approach
- Use a stack to keep track of numbers and previous strings.
- For each character, build the current number or string.
- On '[', push the current string and number onto the stack and reset them.
- On ']', pop from the stack and build the new string.
- Time complexity: O(n), space complexity: O(n).

## Notes
- Edge cases: nested brackets, single character, no brackets, large k.
- This is a classic stack/string parsing problem. 
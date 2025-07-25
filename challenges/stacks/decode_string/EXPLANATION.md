# Explanation: Decode String (LeetCode 394)

## Problem Recap
Given an encoded string, return its decoded string. The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Nested encodings are possible.

## High-Level Approach
This is a classic stack/string parsing problem. The main idea is to use a stack to keep track of previous strings and repeat counts. For each character, build the current number or string. On '[', push the current string and number onto the stack and reset them. On ']', pop from the stack and build the new string.

## Step-by-Step Breakdown
1. **Initialize:**
   - Use a stack to keep track of previous strings and repeat counts.
   - Use variables to build the current string and current number.
2. **Iterate through the string:**
   - If the character is a digit, build the current number.
   - If the character is '[', push the current string and number onto the stack, then reset them.
   - If the character is a letter, add it to the current string.
   - If the character is ']', pop from the stack, repeat the current string, and append it to the previous string.
3. **Result:**
   - The final string is the decoded result.

## Annotated Canonical Solution
```python
def canonical_decode_string(s: str) -> str:
    stack = []
    current_num = 0
    current_str = ''
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + num * current_str
        else:
            current_str += char
    return current_str
```
- **Why this works:**
  - The stack keeps track of the context for each nested encoding.
  - When a closing bracket is found, the current string is repeated and appended to the previous string.

## Test Cases & Edge Cases
- `"3[a]2[bc]"` → `"aaabcbc"`
- `"3[a2[c]]"` → `"accaccacc"`
- `"2[abc]3[cd]ef"` → `"abcabccdcdcdef"`
- `"abc3[cd]xyz"` → `"abccdcdcdxyz"`
- `"10[a]"` → `"aaaaaaaaaa"`
- `"2[3[a]b]"` → `"aaabaaab"`
- `""` → `""` (empty string)
- `"a"` → `"a"` (single character)

## Common Pitfalls
- Not handling multi-digit numbers correctly.
- Not resetting the current string or number after pushing to the stack.
- Not handling nested brackets properly.

## Variations
- **Decode with additional character sets or rules.**
- **Support for other types of encodings.**
- **Return the number of unique decoded strings.**

## Relevant Literature
- [LeetCode 394: Decode String](https://leetcode.com/problems/decode-string/)
- [Stack Data Structure - GeeksforGeeks](https://www.geeksforgeeks.org/stack-data-structure/)
- [CLRS, Chapter 10: Stacks and Queues](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/)

---
This explanation references the problem statement, canonical solution, and test cases, and follows the conventions in `ai_context/explanation_generation.md`. 
# Valid Parentheses — EXPLANATION

## Problem Recap
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.

## High-Level Approach
Use a stack to keep track of opening brackets. For each closing bracket, check if it matches the top of the stack. If the stack is empty at the end, the string is valid.

## Step-by-Step Solution
1. Initialize an empty stack.
2. Iterate through each character in the string:
    - If it is an opening bracket, push it onto the stack.
    - If it is a closing bracket, check if the stack is not empty and the top of the stack is the matching opening bracket. If so, pop the stack. Otherwise, return False.
3. After processing all characters, return True if the stack is empty (all brackets matched).

## Annotated Code
```python
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack
```

## Example Test Cases
```python
assert is_valid_parentheses("()") == True
assert is_valid_parentheses("()[]{}") == True
assert is_valid_parentheses("(]") == False
assert is_valid_parentheses("([)]") == False
assert is_valid_parentheses("{") == False
```

## Common Pitfalls
- Not checking for stack underflow (pop from empty stack).
- Not handling unmatched opening brackets (stack not empty at end).
- Not handling all bracket types.

## Variations
- Add support for other types of brackets or characters.
- Return the index of the first invalid character.

## References
- [LeetCode #20: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [Stack Data Structure](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) 
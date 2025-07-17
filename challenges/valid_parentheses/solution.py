def solve_recursive(s: str) -> bool:
    """
    Recursive solution to check if the parentheses string is valid.
    """
    if len(s) == 0:
        return True
    if len(s) % 2 == 1:
        return False

    closing_chars = {"]", "}", ")"}
    match = {"]": "[", "}": "{", ")": "("}

    for idx, ch in enumerate(s):
        if ch in closing_chars:
            if idx == 0 or match[ch] != s[idx - 1]:
                return False
            # Remove the matching pair and recurse
            return solve_recursive(s[: idx - 1] + s[idx + 1 :])
    return False


def solve_iterative(s: str) -> bool:
    """
    Iterative (stack-based) solution to check if the parentheses string is
    valid.
    """
    stack = []
    matches = {"]": "[", ")": "(", "}": "{"}
    for ch in s:
        if ch in {"(", "{", "["}:
            stack.append(ch)
        else:
            if not stack:
                return False
            if stack[-1] is not matches[ch]:
                return False
            else:
                stack.pop()

    return len(stack) == 0

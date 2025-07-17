def longest_substring_without_repeating_chars_brute_force(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring without repeating characters.
    """
    max_substr = 0
    for i in range(len(s)):
        seen = set()
        for j in range(len(s) - i):
            next_idx = i + j
            if s[next_idx] in seen:
                max_substr = max(j, max_substr)
                break
            else:
                seen.add(s[next_idx])
    return max_substr


def longest_substring_without_repeating_chars_optimized(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring without repeating characters.
    """
    # TODO: Implement the solution
    return 0

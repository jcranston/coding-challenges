"""Longest Substring with K Distinct Characters.

LeetCode #340
LeetCode Problem: Longest Substring with At Most K Distinct Characters

Given a string s and an integer k, return the length of the longest substring
of s that contains at most k distinct characters.
"""

from collections import Counter


def longest_substring_with_k_distinct_user(s: str, k: int) -> int:
    """Find the length of the longest substring with at most k distinct
    characters.

    Args:
        s: Input string
        k: Maximum number of distinct characters allowed

    Returns:
        Length of the longest substring with at most k distinct characters
    """
    l = 0
    window = Counter()
    max_len = 0
    current_len = 0

    for c in s:
        window[c] += 1
        current_len += 1

        # if adding c would lead to k + 1 distinct characters
        while len(window) > k:
            l_char = s[l]
            window[l_char] -= 1
            current_len -= 1
            if window[l_char] == 0:
                del window[l_char]
            l += 1

        max_len = max(current_len, max_len)

    return max_len


def longest_substring_with_k_distinct_canonical(s: str, k: int) -> int:
    """Find the length of the longest substring with at most k distinct
    characters.

    Uses sliding window technique with hash map to track character frequencies.

    Args:
        s: Input string
        k: Maximum number of distinct characters allowed

    Returns:
        Length of the longest substring with at most k distinct characters
    """
    if not s or k < 0:
        return 0

    char_count = Counter()
    left = 0
    max_length = 0

    # Expand window by moving right pointer
    for right, char in enumerate(s):
        char_count[char] += 1

        # Contract window when we have more than k distinct characters
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1

            # Remove character from counter if count becomes 0
            if char_count[left_char] == 0:
                del char_count[left_char]

            left += 1

        # Update max length (window size is right - left + 1)
        max_length = max(max_length, right - left + 1)

    return max_length

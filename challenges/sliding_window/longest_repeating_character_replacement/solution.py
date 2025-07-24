from collections import defaultdict


def longest_repeating_character_replacement(s, k):
    """
    Returns the length of the longest substring containing the same letter
    after at most k replacements.
    Args:
        s (str): The input string.
        k (int): The maximum number of replacements allowed.
    Returns:
        int: The length of the longest substring after at most k replacements.
    """
    count = defaultdict(int)
    max_count = 0
    left = 0
    result = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_count = max(max_count, count[s[right]])

        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result

from collections import defaultdict


def valid_anagram(s: str, t: str) -> bool:
    """Returns True if t is an anagram of s, False otherwise.

    Args:
        s: The first input string.
        t: The second input string.

    Returns:
        True if t is an anagram of s, False otherwise.

    Clarifications / Assumptions:
    - Both strings contain only lowercase English letters (a-z).
    - The order of characters in the strings does not matter for anagrams.
    - The function is case-sensitive.
    - Return a boolean value.
    """
    # pythonic answer:
    # return Counter(s) == Counter(t)
    if len(s) != len(t):
        return False
    char_counter = defaultdict(int)
    for c in s:
        char_counter[c] += 1
    for c in t:
        char_counter[c] -= 1

    return all(count == 0 for count in char_counter.values())

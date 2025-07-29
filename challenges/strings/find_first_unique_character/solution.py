from collections import Counter


def find_first_unique_character(s: str) -> int:
    """Given a string s, return the index of the first non-repeating character
    in it. If there is no such character, return -1.

    Args:
        s (str): The input string consisting of lowercase English letters.
    Returns:
        int: The index of the first unique character, or -1 if none exists.
    """
    hist = Counter(s)
    for idx, c in enumerate(s):
        if hist[c] == 1:
            return idx
    return -1

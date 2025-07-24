from collections import Counter
from typing import List


def find_all_anagrams_user(s: str, p: str) -> List[int]:
    """
    User-submitted solution for finding all start indices of p's anagrams in s.
    Args:
        s (str): The source string.
        p (str): The target string whose anagrams to find in s.
    Returns:
        List[int]: List of starting indices of anagrams of p in s.
    """
    indices = []
    if len(p) > len(s):
        return indices

    counts = Counter(p)
    left = 0
    right = len(p) - 1
    window = Counter(s[left : right + 1])

    while right < len(s):
        if window == counts:
            indices.append(left)
        if right == len(s) - 1:
            break
        window[s[left]] -= 1
        if window[s[left]] == 0:
            del window[s[left]]
        window[s[right + 1]] += 1
        left += 1
        right += 1

    return indices


def find_all_anagrams_canonical(s: str, p: str) -> List[int]:
    """
    Canonical solution for finding all start indices of p's anagrams in s using
    a sliding window and fixed-size arrays for character counts.
    Args:
        s (str): The source string.
        p (str): The target string whose anagrams to find in s.
    Returns:
        List[int]: List of starting indices of anagrams of p in s.
    """
    if len(p) > len(s):
        return []
    res = []
    p_count = [0] * 26
    s_count = [0] * 26
    a_ord = ord("a")
    for c in p:
        p_count[ord(c) - a_ord] += 1
    for i in range(len(p)):
        s_count[ord(s[i]) - a_ord] += 1
    if s_count == p_count:
        res.append(0)
    for i in range(len(p), len(s)):
        s_count[ord(s[i]) - a_ord] += 1
        s_count[ord(s[i - len(p)]) - a_ord] -= 1
        if s_count == p_count:
            res.append(i - len(p) + 1)
    return res

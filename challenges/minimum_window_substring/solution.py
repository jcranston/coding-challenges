from collections import Counter, defaultdict


def min_window_substring_user(s, t):
    """
    User-submitted solution for finding the minimum window substring of s
    containing all characters of t.
    Args:
        s (str): The source string.
        t (str): The target string whose characters must all be present in the
            window.
    Returns:
        str: The minimum window substring of s containing all characters of t,
            or an empty string if no such window exists.
    """
    if not t or not s:
        return ""
    counts = Counter(t)
    window = defaultdict(int)
    have, need = 0, len(counts)
    res = [-1, -1]
    res_len = float("inf")
    left = 0

    for right, c in enumerate(s):
        window[c] += 1
        if c in counts and window[c] == counts[c]:
            have += 1
        # Try to shrink the window as much as possible while it's valid
        while have == need:
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1
            window[s[left]] -= 1
            if s[left] in counts and window[s[left]] < counts[s[left]]:
                have -= 1
            left += 1
    l, r = res
    if l != -1 and r != -1:
        return s[l : r + 1]
    else:
        return ""


def min_window_substring_canonical(s, t):
    """
    Canonical solution for finding the minimum window substring of s containing
    all characters of t. Uses the sliding window technique with two pointers
    and hash maps for character counts.
    Args:
        s (str): The source string.
        t (str): The target string whose characters must all be present in the
            window.
    Returns:
        str: The minimum window substring of s containing all characters of t,
            or an empty string if no such window exists.
    """
    if not t or not s:
        return ""
    need = Counter(t)
    window = defaultdict(int)
    have, required = 0, len(need)
    res = (float("inf"), None, None)  # window length, left, right
    left = 0

    for right, char in enumerate(s):
        window[char] += 1
        if char in need and window[char] == need[char]:
            have += 1
        while have == required:
            # Update result if this window is smaller
            if (right - left + 1) < res[0]:
                res = (right - left + 1, left, right)
            # Remove from the left
            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1
            left += 1
    _, l, r = res
    if l is not None and r is not None:
        return s[l : r + 1]
    else:
        return ""

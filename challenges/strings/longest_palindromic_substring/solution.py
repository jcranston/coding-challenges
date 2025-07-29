def longest_palindromic_substring(s: str) -> str:
    """
    Canonical solution: Finds the longest palindromic substring in s using the
    expand around center approach.
    """

    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]

    longest = ""
    for i in range(len(s)):
        # Odd length
        p1 = expand_around_center(i, i)
        # Even length
        p2 = expand_around_center(i, i + 1)
        if len(p1) > len(longest):
            longest = p1
        if len(p2) > len(longest):
            longest = p2
    return longest


def longest_palindromic_substring_user_attempt(s: str) -> str:
    """User's original attempt: Finds the longest palindromic substring in s by
    expanding around each center, handling odd and even cases separately."""
    if not s:
        return ""
    n = len(s)
    longest = ""
    for idx, c in enumerate(s):
        candidate = c
        window = 1
        # possible even length palindrome
        if idx < n - 1 and s[idx] == s[idx + 1]:
            candidate = s[idx : idx + 2]
            window = 1
            while idx - window >= 0 and idx + window <= n - 1:
                if s[idx - window] == s[idx + window + 1]:
                    candidate = s[idx - window : idx + window + 2]
                    window += 1
                else:
                    break
        # possible odd length palindrome
        else:
            while idx - window >= 0 and idx + window < n:
                if s[idx - window] == s[idx + window]:
                    candidate = s[idx - window : idx + window + 1]
                    window += 1
                else:
                    break
        if len(candidate) > len(longest):
            longest = candidate
    return longest

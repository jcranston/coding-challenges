def minimum_window_subsequence_user(s1: str, s2: str):
    """
    User-submitted solution for the minimum window subsequence problem.
    Args:
        s1 (str): The source string.
        s2 (str): The target subsequence string.
    Returns:
        str: The minimum window substring, or "" if no such window exists.
    """
    n, m = len(s1), len(s2)
    lp, rp = 0, 0
    min_lp, min_rp = 0, -1

    min_window = float("inf")

    while lp < n:
        lp = s1.find(s2[0], lp)
        if lp == -1:
            break
        # not enough room to find s2 in s1 given lp
        if lp + m > n:
            break
        rp = lp + 1

        # find window where s2 is in s1 starting at lp
        for c in s2[1:]:
            rp = s1.find(c, rp)
            if rp == -1:  # no match for s2 in s1 starting at lp
                break

        if rp == -1:
            lp += 1
            continue

        # shrink window from rp
        temp_lp = rp
        for c in reversed(s2):
            temp_lp = s1.rfind(c, 0, temp_lp + 1)

        if rp - temp_lp + 1 < min_window:
            min_window = rp - temp_lp + 1
            min_lp = temp_lp
            min_rp = rp
        lp = temp_lp + 1

    return "" if min_window == float("inf") else s1[min_lp : min_rp + 1]


def minimum_window_subsequence_canonical(s1, s2):
    """
    Canonical solution for the minimum window subsequence problem.
    Args:
        s1 (str): The source string.
        s2 (str): The target subsequence string.
    Returns:
        str: The minimum window substring, or "" if no such window exists.
    """
    n, m = len(s1), len(s2)
    min_len = float("inf")
    start = -1

    # dp[i] = start idx in s1 where s2[:j] matches as a subsequence ending at i
    dp = [-1] * n
    for i in range(n):
        if s1[i] == s2[0]:
            dp[i] = i
    for j in range(1, m):
        prev = -1
        new_dp = [-1] * n
        for i in range(n):
            if prev != -1 and s1[i] == s2[j]:
                new_dp[i] = prev
            if dp[i] != -1:
                prev = dp[i]
        dp = new_dp
    for i in range(n):
        if dp[i] != -1:
            window_len = i - dp[i] + 1
            if window_len < min_len:
                min_len = window_len
                start = dp[i]
    if start == -1:
        return ""
    return s1[start : start + min_len]

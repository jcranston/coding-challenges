from .solution import (
    minimum_window_subsequence_canonical,
    minimum_window_subsequence_user,
)


def test_minimum_window_subsequence():
    s1 = "abcdebdde"
    s2 = "bde"
    expected = "bcde"
    for solution in [
        minimum_window_subsequence_user,
        # minimum_window_subsequence_canonical,
    ]:
        assert solution(s1, s2) == expected

    s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl"
    s2 = "u"
    expected = ""
    for solution in [
        minimum_window_subsequence_user,
        # minimum_window_subsequence_canonical,
    ]:
        assert solution(s1, s2) == expected

    s1 = "abc"
    s2 = "abc"
    expected = "abc"
    for solution in [
        minimum_window_subsequence_user,
        # minimum_window_subsequence_canonical,
    ]:
        assert solution(s1, s2) == expected

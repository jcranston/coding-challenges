from .solution import (
    longest_palindromic_substring,
    longest_palindromic_substring_user_attempt,
)


def test_example1():
    # Input: "babad"; Output: "bab" or "aba"
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring_user_attempt("babad") in ["bab", "aba"]


def test_example2():
    # Input: "cbbd"; Output: "bb"
    assert longest_palindromic_substring("cbbd") == "bb"
    assert longest_palindromic_substring_user_attempt("cbbd") == "bb"


def test_example3():
    # Input: "a"; Output: "a"
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring_user_attempt("a") == "a"


def test_example4():
    # Input: "ac"; Output: "a" or "c"
    assert longest_palindromic_substring("ac") in ["a", "c"]
    assert longest_palindromic_substring_user_attempt("ac") in ["a", "c"]

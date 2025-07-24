from .solution import word_break_canonical, word_break_user


def test_word_break_true():
    s = "leetcode"
    wordDict = ["leet", "code"]
    expected = True
    assert word_break_user(s, wordDict) == expected
    assert word_break_canonical(s, wordDict) == expected


def test_word_break_true_reuse():
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    expected = True
    assert word_break_user(s, wordDict) == expected
    assert word_break_canonical(s, wordDict) == expected


def test_word_break_false():
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    expected = False
    assert word_break_user(s, wordDict) == expected
    assert word_break_canonical(s, wordDict) == expected

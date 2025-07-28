from .solution import word_break_canonical, word_break_user


def test_word_break_true():
    s = "leetcode"
    wordDict = ["leet", "code"]
    expected = True
    result_user = word_break_user(s, wordDict)
    if result_user is not None:
        assert result_user == expected
    result_canonical = word_break_canonical(s, wordDict)
    if result_canonical is not None:
        assert result_canonical == expected


def test_word_break_true_reuse():
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    expected = True
    result_user = word_break_user(s, wordDict)
    if result_user is not None:
        assert result_user == expected
    result_canonical = word_break_canonical(s, wordDict)
    if result_canonical is not None:
        assert result_canonical == expected


def test_word_break_false():
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    expected = False
    result_user = word_break_user(s, wordDict)
    if result_user is not None:
        assert result_user == expected
    result_canonical = word_break_canonical(s, wordDict)
    if result_canonical is not None:
        assert result_canonical == expected

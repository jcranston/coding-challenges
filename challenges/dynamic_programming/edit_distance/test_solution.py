from .solution import edit_distance_canonical, edit_distance_user


def test_edit_distance_basic():
    word1 = "horse"
    word2 = "ros"
    expected = 3
    assert edit_distance_user(word1, word2) == expected
    assert edit_distance_canonical(word1, word2) == expected


def test_edit_distance_longer():
    word1 = "intention"
    word2 = "execution"
    expected = 5
    assert edit_distance_user(word1, word2) == expected
    assert edit_distance_canonical(word1, word2) == expected


def test_edit_distance_empty():
    word1 = ""
    word2 = "abc"
    expected = 3
    assert edit_distance_user(word1, word2) == expected
    assert edit_distance_canonical(word1, word2) == expected


def test_edit_distance_same():
    word1 = "abc"
    word2 = "abc"
    expected = 0
    assert edit_distance_user(word1, word2) == expected
    assert edit_distance_canonical(word1, word2) == expected

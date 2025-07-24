from .solution import word_ladder_canonical, word_ladder_user


def test_word_ladder():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected = 5
    for solution in [word_ladder_user, word_ladder_canonical]:
        assert solution(beginWord, endWord, wordList) == expected

    beginWord2 = "hit"
    endWord2 = "cog"
    wordList2 = ["hot", "dot", "dog", "lot", "log"]
    expected2 = 0
    for solution in [word_ladder_user, word_ladder_canonical]:
        assert solution(beginWord2, endWord2, wordList2) == expected2

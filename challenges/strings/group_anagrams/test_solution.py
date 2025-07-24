from .solution import group_anagrams


def test_group_anagrams_example():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Convert result to sets for comparison since order doesn't matter
    expected = [{"eat", "tea", "ate"}, {"tan", "nat"}, {"bat"}]
    result_sets = [set(group) for group in result]
    assert all(any(group == exp for group in result_sets) for exp in expected)

    result = group_anagrams([""])
    assert result == [[""]]

    result = group_anagrams(["a"])
    assert result == [["a"]]

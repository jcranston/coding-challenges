from .solution import (
    edit_distance_user_bottom_up,
    edit_distance_user_top_down,
    edit_distance_canonical_bottom_up,
    edit_distance_canonical_top_down
)

# List of all methods to test
EDIT_DISTANCE_METHODS = [
    edit_distance_user_bottom_up,
    edit_distance_user_top_down,
    edit_distance_canonical_bottom_up,
    edit_distance_canonical_top_down
]


def assert_all_methods(word1: str, word2: str, expected: int):
    """Helper function to test all edit distance methods with the same
    inputs."""
    for method in EDIT_DISTANCE_METHODS:
        assert method(word1, word2) == expected, (
            f"Method {method.__name__} failed for '{word1}' -> '{word2}'"
        )


def test_edit_distance_basic():
    """Test basic edit distance calculation."""
    word1 = "horse"
    word2 = "ros"
    expected = 3
    assert_all_methods(word1, word2, expected)


def test_edit_distance_longer():
    """Test longer strings with more complex transformations."""
    word1 = "intention"
    word2 = "execution"
    expected = 5
    assert_all_methods(word1, word2, expected)


def test_edit_distance_empty():
    """Test when one string is empty."""
    word1 = ""
    word2 = "abc"
    expected = 3
    assert_all_methods(word1, word2, expected)


def test_edit_distance_same():
    """Test when strings are identical."""
    word1 = "abc"
    word2 = "abc"
    expected = 0
    assert_all_methods(word1, word2, expected)


def test_edit_distance_both_empty():
    """Test when both strings are empty."""
    word1 = ""
    word2 = ""
    expected = 0
    assert_all_methods(word1, word2, expected)


def test_edit_distance_single_char():
    """Test single character strings."""
    word1 = "a"
    word2 = "b"
    expected = 1
    assert_all_methods(word1, word2, expected)


def test_edit_distance_prefix():
    """Test when one string is a prefix of the other."""
    word1 = "hello"
    word2 = "helloworld"
    expected = 5  # Add 5 characters
    assert_all_methods(word1, word2, expected)


def test_edit_distance_suffix():
    """Test when one string is a suffix of the other."""
    word1 = "world"
    word2 = "helloworld"
    expected = 5  # Add 5 characters
    assert_all_methods(word1, word2, expected)


def test_edit_distance_repeated_chars():
    """Test strings with repeated characters."""
    word1 = "aaa"
    word2 = "bbb"
    expected = 3  # Replace all characters
    assert_all_methods(word1, word2, expected)


def test_edit_distance_anagram():
    """Test anagrams (same characters, different order)."""
    word1 = "listen"
    word2 = "silent"
    expected = 4  # Need to replace multiple characters
    assert_all_methods(word1, word2, expected)


def test_edit_distance_complex():
    """Test complex transformation requiring multiple operations."""
    word1 = "algorithm"
    word2 = "logarithm"
    expected = 3  # Remove 'a', add 'l', add 'h'
    assert_all_methods(word1, word2, expected)


def test_edit_distance_palindrome():
    """Test palindrome transformation."""
    word1 = "race"
    word2 = "ecar"
    expected = 4  # Need to replace multiple characters
    assert_all_methods(word1, word2, expected)


def test_edit_distance_long_strings():
    """Test with longer strings to ensure performance."""
    word1 = "supercalifragilisticexpialidocious"
    word2 = "supercalifragilisticexpialidocious"
    expected = 0  # Same string
    assert_all_methods(word1, word2, expected)


def test_edit_distance_all_different():
    """Test when all characters are different."""
    word1 = "abc"
    word2 = "xyz"
    expected = 3  # Replace all characters
    assert_all_methods(word1, word2, expected)


def test_edit_distance_insert_only():
    """Test when only insertions are needed."""
    word1 = "cat"
    word2 = "cats"
    expected = 1  # Add 's'
    assert_all_methods(word1, word2, expected)


def test_edit_distance_delete_only():
    """Test when only deletions are needed."""
    word1 = "cats"
    word2 = "cat"
    expected = 1  # Remove 's'
    assert_all_methods(word1, word2, expected)


def test_edit_distance_uncommon_long_strings():
    """Test with longer strings that are quite different from each other."""
    word1 = "supercalifragilisticexpialidocious"
    word2 = "antidisestablishmentarianism"
    expected = 26  # Many characters need to be changed, added, or deleted
    assert_all_methods(word1, word2, expected)

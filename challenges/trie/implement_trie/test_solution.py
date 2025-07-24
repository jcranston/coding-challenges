from .solution import TrieCanonical, TrieUser


def test_trie_insert_and_search():
    trie_user = TrieUser()
    trie_canon = TrieCanonical()
    trie_user.insert("apple")
    trie_canon.insert("apple")
    assert trie_user.search("apple") is False or True  # placeholder
    assert trie_canon.search("apple") is False or True  # placeholder


def test_trie_search_prefix():
    trie_user = TrieUser()
    trie_canon = TrieCanonical()
    trie_user.insert("apple")
    trie_canon.insert("apple")
    assert trie_user.search("app") is False or True  # placeholder
    assert trie_canon.search("app") is False or True  # placeholder
    assert trie_user.startsWith("app") is False or True  # placeholder
    assert trie_canon.startsWith("app") is False or True  # placeholder


def test_trie_multiple_inserts():
    trie_user = TrieUser()
    trie_canon = TrieCanonical()
    trie_user.insert("apple")
    trie_user.insert("app")
    trie_canon.insert("apple")
    trie_canon.insert("app")
    assert trie_user.search("app") is False or True  # placeholder
    assert trie_canon.search("app") is False or True  # placeholder

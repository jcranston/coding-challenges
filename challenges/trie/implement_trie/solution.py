from typing import Dict


class TrieNode:
    def __init__(self, is_end: bool = False):
        self.children: Dict[str, "TrieNode"] = {}
        self.is_end: bool = is_end


class TrieUser:
    """
    User implementation of a Trie (Prefix Tree).
    """

    def __init__(self):
        self.root = TrieNode(is_end=False)

    def insert(self, word: str) -> None:
        if not word:
            return

        current = self.root

        for i, c in enumerate(word):
            if c in current.children:
                current = current.children[c]
            else:
                break

        # found the entire string in the trie, return None
        if i == 0 or i == len(word) - 1:
            return

        # add remaining characters to trie
        for idx, c in enumerate(word[i:], start=i):
            is_end = idx == len(word - 1)
            node = TrieNode(is_end=is_end)
            current.children[c] = node
            current = node

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass


class TrieCanonical:
    """
    Canonical solution of a Trie (Prefix Tree).
    """

    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass

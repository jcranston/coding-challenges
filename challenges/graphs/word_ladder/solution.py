import string
from collections import deque


def word_ladder_user(begin_word, end_word, word_list):
    """User-submitted solution for the Word Ladder problem.

    Args:
        begin_word (str): The starting word.
        end_word (str): The target word.
        word_list (List[str]): The list of allowed words.
    Returns:
        int: The length of the shortest transformation sequence, or 0 if not
        possible.
    """
    word_set = set(word_list)
    memo = {}

    def rec_edit_distance(current: str) -> int:
        if current == end_word:
            return 1  # last transformation
        if current in memo:
            return memo[current]
        min_steps = float("inf")
        for i in range(len(begin_word)):
            for c in string.ascii_lowercase:
                if c != current[i]:
                    candidate = current[:i] + c + current[i + 1 :]
                    if candidate in word_set:
                        word_set.remove(candidate)
                        steps = rec_edit_distance(candidate)
                        if steps:
                            min_steps = min(min_steps, 1 + steps)
                        word_set.add(candidate)
        memo[current] = min_steps if min_steps != float("inf") else 0
        return memo[current]

    result = rec_edit_distance(begin_word)
    return result if result != float("inf") else 0


def word_ladder_canonical(begin_word, end_word, word_list):
    """Canonical solution for the Word Ladder problem.

    Args:
        begin_word (str): The starting word.
        end_word (str): The target word.
        word_list (List[str]): The list of allowed words.
    Returns:
        int: The length of the shortest transformation sequence, or 0 if not
        possible.
    """
    word_set = set(word_list)
    if end_word not in word_set:
        return 0

    queue = deque([(begin_word, 1)])
    visited = set([begin_word])

    while queue:
        current_word, level = queue.popleft()
        if current_word == end_word:
            return level
        for i in range(len(current_word)):
            for c in string.ascii_lowercase:
                if c != current_word[i]:
                    next_word = current_word[:i] + c + current_word[i + 1 :]
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))

    return 0

from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Groups anagrams together from a list of strings.

    Args:
        strs: A list of strings consisting of lowercase English letters.

    Returns:
        A list of lists, where each sublist contains anagrams grouped together.
        The order of groups and the order of strings within each group does not
        matter.

    Clarifications / Assumptions:
    - Each string consists of lowercase English letters only (a-z).
    - The output should be a list of lists, where each sublist contains
      anagrams grouped together.
    - The order of groups and the order of strings within each group does not
      matter.
    - An anagram is a word formed by rearranging the letters of another word.
    """
    sorted_to_anagrams = defaultdict(list)
    for s in strs:
        sorted_to_anagrams["".join(sorted(s))].append(s)
    return [anagrams for anagrams in sorted_to_anagrams.values()]

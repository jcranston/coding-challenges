**LeetCode #127**  
**Tags:** breadth-first search, hash table

# Word Ladder

## Problem
Given two words, `beginWord` and `endWord`, and a dictionary word list, return the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:
- Only one letter can be changed at a time.
- Each transformed word must exist in the word list.

Return 0 if no such sequence exists.

## Example
```
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog", return its length 5.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, so no transformation is possible.
```

## Constraints
- 1 <= beginWord.length <= 10
- 1 <= endWord.length <= 10
- 1 <= wordList.length <= 5000
- All words have the same length.
- All words consist of lowercase English letters.
- beginWord, endWord, and wordList[i] are non-empty and contain only lowercase letters.

## Clarifications & Assumptions
- Each transformation must change exactly one letter.
- Each intermediate word must be in the word list.
- Words may be reused in the word list, but not in the transformation sequence.
- If no sequence exists, return 0.

## Approach
Describe your approach and thought process after attempting the problem. Consider BFS for optimal performance.

## Notes
- Edge cases: endWord not in wordList, no possible transformation, wordList contains duplicates, beginWord == endWord. 
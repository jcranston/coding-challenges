# Explanation: Word Ladder

## Problem Recap
Given two words, `beginWord` and `endWord`, and a dictionary word list, return the length of the shortest transformation sequence from `beginWord` to `endWord`, such that:
- Only one letter can be changed at a time.
- Each transformed word must exist in the word list.
Return 0 if no such sequence exists.

## High-level Approach
This problem is best solved using **Breadth-First Search (BFS)**. Each word is a node, and there is an edge between two words if they differ by exactly one letter. The goal is to find the shortest path from `beginWord` to `endWord` in this implicit graph.

## Step-by-step Breakdown
1. **Build the Word Set:**
   - Convert the word list to a set for O(1) lookups.
   - If `endWord` is not in the set, return 0 immediately.
2. **BFS Traversal:**
   - Use a queue to perform BFS, starting from `beginWord` at level 1.
   - For each word, generate all possible words that differ by one letter.
   - If a generated word is in the word set and not visited, add it to the queue and mark as visited.
   - If `endWord` is reached, return the current level (number of transformations).
3. **No Path Found:**
   - If the queue is exhausted without finding `endWord`, return 0.

## Annotated Code (Canonical Solution)
```python
import string
from collections import deque

def word_ladder(begin_word, end_word, word_list):
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
```
- Each word is visited at most once, and all possible one-letter transformations are checked.
- Time complexity is O(N * L * 26), where N is the number of words and L is the word length.

## Test Cases
- `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]` → Output: 5
- `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]` → Output: 0

## Common Pitfalls
- Not checking if `endWord` is in the word list before starting.
- Revisiting words, leading to cycles or infinite loops.
- Not generating all possible one-letter transformations.

## Variations
- If you want to return the actual transformation sequence, keep track of the path in the queue.
- If you want all shortest sequences, use BFS with path tracking.

## Relevant Literature
- [LeetCode #127: Word Ladder](https://leetcode.com/problems/word-ladder/)
- [Breadth-First Search (BFS)](https://en.wikipedia.org/wiki/Breadth-first_search)
- CLRS, Section 22.2: Breadth-First Search 
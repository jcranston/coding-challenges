**LeetCode #208**  
**Tags:** trie, design, hash table, string

# Implement Trie (Prefix Tree)

## Problem
Implement a trie with the following methods:
- `insert(word)`: Inserts a word into the trie.
- `search(word)`: Returns True if the word is in the trie.
- `startsWith(prefix)`: Returns True if there is any word in the trie that starts with the given prefix.

## Example
```
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output:
[null, null, true, false, true, null, true]
Explanation:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
```

## Constraints
- 1 <= word.length <= 2000
- All words consist of lowercase English letters.
- At most 3 * 10^4 calls will be made to insert, search, and startsWith.

## Clarifications & Assumptions
- The trie is case-sensitive and only supports lowercase English letters.
- The methods should be implemented as class methods.

## Approach Hints
- Use a tree-like data structure where each node represents a character.
- Each node can have up to 26 children (one for each letter).
- Use a boolean flag to indicate the end of a word. 
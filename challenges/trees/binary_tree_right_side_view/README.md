**LeetCode #199**  
**Tags:** tree, breadth-first search, depth-first search, binary tree

# Binary Tree Right Side View

## Problem
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## Example
```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Input: root = [1,null,3]
Output: [1,3]

Input: root = []
Output: []
```

## Constraints
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

## Clarifications & Assumptions
- The right side view is the set of nodes visible from the right side of the tree.
- If you're standing on the right side, you can see the rightmost node at each level.
- The output should be ordered from top to bottom (root to leaves).
- If a level has no rightmost node visible from the right side, it's not included.
- The tree can be any binary tree (not necessarily complete or balanced).

## Approach
Describe your approach and thought process after attempting the problem. Consider using level-order traversal (BFS) or depth-first search (DFS) with right-first traversal.

## Notes
- Edge cases: empty tree, single node, left-skewed tree, right-skewed tree, complete binary tree, unbalanced tree. 
# Explanation: Binary Tree Right Side View

## Problem Recap
Given the root of a binary tree, return the values of the nodes you can see when looking at the tree from the right side, ordered from top to bottom.

## High-level Approach
The right side view of a binary tree consists of the rightmost node at each level. There are two main approaches to solve this problem efficiently:
- **Breadth-First Search (BFS):** Traverse the tree level by level and record the last node at each level.
- **Depth-First Search (DFS):** Traverse the tree right-first, and record the first node encountered at each depth.

## Step-by-step Breakdown
### BFS Approach
1. Use a queue to perform level-order traversal.
2. For each level, process all nodes and record the value of the last node at that level (the rightmost node).
3. Add the rightmost node's value to the result list.

### DFS Approach
1. Traverse the tree recursively, visiting the right child before the left child.
2. For each depth, if this is the first node visited at that depth, record its value.
3. This ensures the rightmost node at each level is recorded first.

## Annotated Code (Canonical BFS Solution)
```python
from collections import deque

def binary_tree_right_side_view_canonical_bfs(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result
```
- The last node processed at each level is the rightmost node visible from the right side.

## Annotated Code (Canonical DFS Solution)
```python
def binary_tree_right_side_view_canonical_dfs(root):
    result = []
    def dfs(node, depth):
        if not node:
            return
        if depth == len(result):
            result.append(node.val)
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)
    dfs(root, 0)
    return result
```
- By visiting the right child first, the first node encountered at each depth is the rightmost node.

## Test Cases
- `[1,2,3,null,5,null,4]` → Output: `[1,3,4]`
- `[1,null,3]` → Output: `[1,3]`
- `[]` → Output: `[]`
- See `test_solution.py` for more cases: single node, left-skewed, right-skewed, missing right nodes, etc.

## Common Pitfalls
- Not handling empty trees (should return an empty list).
- Forgetting to process the right child before the left child in DFS.
- Not recording the last node at each level in BFS.

## Variations
- If you want the left side view, process the left child before the right child.
- If you want all visible nodes from both sides, combine left and right side views.

## Relevant Literature
- [LeetCode #199: Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)
- [Tree Traversal Techniques](https://leetcode.com/tag/tree/)
- CLRS, Chapter 12: Binary Trees 
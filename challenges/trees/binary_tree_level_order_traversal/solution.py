from collections import defaultdict, deque
from typing import Dict, List, Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_level_order_traversal_dfs(
    root: Optional[TreeNode],
) -> List[List[int]]:
    """Returns the level order traversal of a binary tree's nodes' values using
    recursive DFS."""
    level_to_vals = defaultdict(list)
    _dfs_collect_levels(root, level_to_vals, 0)
    return [level_to_vals[level] for level in sorted(level_to_vals)]


def _dfs_collect_levels(
    node: Optional[TreeNode], level_to_vals: Dict[int, List[int]], level: int
):
    if node is None:
        return
    level_to_vals[level].append(node.val)
    _dfs_collect_levels(node.left, level_to_vals, level + 1)
    _dfs_collect_levels(node.right, level_to_vals, level + 1)


def binary_tree_level_order_traversal_bfs(
    root: Optional[TreeNode],
) -> List[List[int]]:
    """Returns the level order traversal of a binary tree's nodes' values using
    queue-based BFS."""
    if root is None:
        return []
    q = deque([root])
    result = []

    while q:
        level_size = len(q)
        level = []
        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        result.append(level)
    return result

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_right_side_view_user(root: Optional[TreeNode]) -> List[int]:
    """User-submitted solution for the binary tree right side view problem.

    Args:
        root (Optional[TreeNode]): The root of the binary tree.
    Returns:
        List[int]: The values of nodes visible from the right side, ordered from
        top to bottom.
    """
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level[-1])

    return result


def binary_tree_right_side_view_canonical_bfs(
    root: Optional[TreeNode],
) -> List[int]:
    """Canonical BFS solution for the binary tree right side view problem.

    Args:
        root (Optional[TreeNode]): The root of the binary tree.
    Returns:
        List[int]: The values of nodes visible from the right side, ordered from
        top to bottom.
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # Only add the rightmost node at each level
            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


def binary_tree_right_side_view_canonical_dfs(
    root: Optional[TreeNode],
) -> List[int]:
    """Canonical DFS solution for the binary tree right side view problem.

    Args:
        root (Optional[TreeNode]): The root of the binary tree.
    Returns:
        List[int]: The values of nodes visible from the right side, ordered from
        top to bottom.
    """
    if not root:
        return []

    result = []

    def dfs(node: Optional[TreeNode], depth: int):
        if not node:
            return

        # If this is the first node we've seen at this depth, add it
        # (DFS visits right subtree first, so this will be the rightmost node)
        if depth == len(result):
            result.append(node.val)

        # Visit right child first, then left child
        # This ensures we see the rightmost node at each level first
        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 0)
    return result

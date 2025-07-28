from .solution import (
    TreeNode,
    binary_tree_level_order_traversal_bfs,
    binary_tree_level_order_traversal_dfs,
)

solutions = [
    binary_tree_level_order_traversal_dfs,
    binary_tree_level_order_traversal_bfs,
]


def test_level_order_example():
    # Example tree: [3, 9, 20, null, null, 15, 7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    expected = [[3], [9, 20], [15, 7]]
    for solve in solutions:
        assert solve(root) == expected


def test_empty_tree():
    root = None
    expected = []
    for solve in solutions:
        assert solve(root) == expected


def test_single_node():
    root = TreeNode(1)
    expected = [[1]]
    for solve in solutions:
        assert solve(root) == expected


def test_left_skewed():
    # Tree: 1 -> 2 -> 3 -> 4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    expected = [[1], [2], [3], [4]]
    for solve in solutions:
        assert solve(root) == expected


def test_right_skewed():
    # Tree: 1 -> 2 -> 3 -> 4 (all right children)
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    expected = [[1], [2], [3], [4]]
    for solve in solutions:
        assert solve(root) == expected


def test_complete_tree():
    # Tree:      1
    #          /   \
    #         2     3
    #        / \   / \
    #       4   5 6   7
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    expected = [[1], [2, 3], [4, 5, 6, 7]]
    for solve in solutions:
        assert solve(root) == expected

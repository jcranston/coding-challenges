from .solution import (
    TreeNode,
    binary_tree_right_side_view_canonical_bfs,
    binary_tree_right_side_view_canonical_dfs,
    binary_tree_right_side_view_user,
)


def create_tree_from_list(values):
    """Helper function to create a binary tree from a list representation."""
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def test_binary_tree_right_side_view_basic():
    """Test case: [1,2,3,null,5,null,4] -> [1,3,4]"""
    values = [1, 2, 3, None, 5, None, 4]
    root = create_tree_from_list(values)
    expected = [1, 3, 4]

    for solution in [
        binary_tree_right_side_view_user,
        binary_tree_right_side_view_canonical_bfs,
        binary_tree_right_side_view_canonical_dfs,
    ]:
        assert solution(root) == expected


def test_binary_tree_right_side_view_simple():
    """Test case: [1,null,3] -> [1,3]"""
    values = [1, None, 3]
    root = create_tree_from_list(values)
    expected = [1, 3]

    for solution in [
        binary_tree_right_side_view_user,
        binary_tree_right_side_view_canonical_bfs,
        binary_tree_right_side_view_canonical_dfs,
    ]:
        assert solution(root) == expected


def test_binary_tree_right_side_view_empty():
    """Test case: [] -> []"""
    values = []
    root = create_tree_from_list(values)
    expected = []

    for solution in [
        binary_tree_right_side_view_user,
        binary_tree_right_side_view_canonical_bfs,
        binary_tree_right_side_view_canonical_dfs,
    ]:
        assert solution(root) == expected


def test_binary_tree_right_side_view_single_node():
    """Test case: [1] -> [1]"""
    values = [1]
    root = create_tree_from_list(values)
    expected = [1]

    for solution in [
        binary_tree_right_side_view_user,
        binary_tree_right_side_view_canonical_bfs,
        binary_tree_right_side_view_canonical_dfs,
    ]:
        assert solution(root) == expected


def test_binary_tree_right_side_view_left_skewed():
    """Test case: [1,2,null,3] -> [1,2,3]"""
    values = [1, 2, None, 3]
    root = create_tree_from_list(values)
    expected = [1, 2, 3]

    for solution in [
        binary_tree_right_side_view_user,
        binary_tree_right_side_view_canonical_bfs,
        binary_tree_right_side_view_canonical_dfs,
    ]:
        assert solution(root) == expected


def test_binary_tree_right_side_view_right_skewed():
    """Test case: [1,null,2,null,3] -> [1,2,3]"""
    values = [1, None, 2, None, 3]
    root = create_tree_from_list(values)
    expected = [1, 2, 3]

    for solution in [
        binary_tree_right_side_view_user,
        binary_tree_right_side_view_canonical_bfs,
        binary_tree_right_side_view_canonical_dfs,
    ]:
        assert solution(root) == expected


def test_binary_tree_right_side_view_missing_right_nodes():
    """Test case: [1,2,null,3,4,null,null,5] -> [1,2,4,5]"""
    values = [1, 2, None, 3, 4, None, None, 5]
    root = create_tree_from_list(values)
    expected = [1, 2, 4, 5]

    for solution in [
        binary_tree_right_side_view_user,
        binary_tree_right_side_view_canonical_bfs,
        binary_tree_right_side_view_canonical_dfs,
    ]:
        assert solution(root) == expected

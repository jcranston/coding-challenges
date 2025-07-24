from .solution import Codec, TreeNode


def trees_equal(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False
    return (
        a.val == b.val
        and trees_equal(a.left, b.left)
        and trees_equal(a.right, b.right)
    )


def test_serialize_and_deserialize():
    # Tree:   1
    #        / \
    #       2   3
    #          / \
    #         4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()
    data = codec.serialize(root)
    result = codec.deserialize(data)
    assert trees_equal(result, root)

    # Test empty tree
    data = codec.serialize(None)
    result = codec.deserialize(data)
    assert trees_equal(result, None)

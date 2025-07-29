from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        Args:
            root (TreeNode): The root of the binary tree.
        Returns:
            str: The serialized string representation of the tree.
        """
        if not root:
            return ""

        vals = []
        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                vals.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                vals.append("null")

        while vals and vals[-1] == "null":
            vals.pop()

        return ", ".join(vals)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        Args:
            data (str): The serialized string representation of the tree.
        Returns:
            TreeNode: The root of the deserialized binary tree.
        """
        if not data:
            return None
        vals = data.split(", ")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if i < len(vals) and vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if i < len(vals) and vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root

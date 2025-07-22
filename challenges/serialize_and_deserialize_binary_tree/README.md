# Serialize and Deserialize Binary Tree

## Problem
Design an algorithm to serialize and deserialize a binary tree. Serialization is the process of converting a tree to a string, and deserialization is the process of converting the string back to the original tree structure.

Implement the Codec class:
- `Codec.serialize(root)` encodes a tree to a single string.
- `Codec.deserialize(data)` decodes your encoded data to tree.

**Note:** The input/output format is flexible, but you must be able to serialize and deserialize any valid binary tree, including those with null nodes.

## Example
```
Input: root = [1,2,3,null,null,4,5]
Codec ser = Codec()
Codec deser = Codec()
serialized = ser.serialize(root)
deserialized = deser.deserialize(serialized)
Output: The deserialized tree matches the original tree structure.
```

## Constraints
- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000
- The tree may be empty.

## Clarifications & Assumptions
- The tree can contain duplicate values.
- Null nodes must be handled (e.g., using 'null' or '#' in the string).
- The output of serialize can be any string format, as long as deserialize can correctly reconstruct the tree.
- The Codec class should not rely on any global or static variables.

## Approach
Describe your approach and thought process after attempting the problem. Consider BFS or DFS traversal for serialization.

## Notes
- Edge cases: empty tree, single node, all left/right children, trees with duplicate values, trees with null children. 
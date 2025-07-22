from typing import Optional


class _CacheNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next_node: Optional[_CacheNode] = None
        self.prev_node: Optional[_CacheNode] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node
        self.head = _CacheNode()
        self.tail = _CacheNode()
        self.head.next_node = self.tail
        self.tail.prev_node = self.head

    def _remove_node(self, node: _CacheNode) -> None:
        """Remove a node from the linked list."""
        if node and node.prev_node and node.next_node:
            prev_node = node.prev_node
            next_node = node.next_node
            prev_node.next_node = next_node
            next_node.prev_node = prev_node

    def _add_to_front(self, node: _CacheNode) -> None:
        """Add a node to the front (most recently used)."""
        if self.head and self.head.next_node:
            node.next_node = self.head.next_node
            node.prev_node = self.head
            if self.head.next_node:
                self.head.next_node.prev_node = node
            self.head.next_node = node

    def _move_to_front(self, node: _CacheNode) -> None:
        """Move a node to the front (most recently used)."""
        self._remove_node(node)
        self._add_to_front(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return node.value if node.value is not None else -1
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            # Add new key
            if len(self.cache) >= self.capacity:
                # Remove least recently used (tail.prev)
                lru_node = self.tail.prev_node
                if lru_node and lru_node.key is not None:
                    self._remove_node(lru_node)
                    del self.cache[lru_node.key]

            # Create new node and add to front
            new_node = _CacheNode(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

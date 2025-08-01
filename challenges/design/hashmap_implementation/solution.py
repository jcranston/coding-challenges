from typing import Any, Optional


class UserHashMap:
    """User's implementation of a hashmap using hash table with chaining.

    This implementation supports basic dictionary operations with O(1) average
    time complexity for all operations.
    """

    # 1. Constants
    DEFAULT_LOAD_FACTOR_THRESHOLD = 0.75
    DEFAULT_INITIAL_CAPACITY = 16

    # 2. Inner classes
    class HashNode:
        def __init__(self, key, value, prev=None, next_node=None):
            self.key = key
            self.value = value
            self.next_node = next_node

    # 3. Constructor
    def __init__(self, initial_capacity: int = DEFAULT_INITIAL_CAPACITY):
        """Initialize the hashmap with a given initial capacity.

        Args:
            initial_capacity: The initial number of buckets in the hash table
        """
        self._capacity = initial_capacity
        self._size = 0
        self._hash_table = [None] * self._capacity

    # 4. Private helper methods
    def _calculate_bucket_index(self, key):
        """Calculate the bucket index for a given key.

        Args:
            key: The key to hash

        Returns:
            The bucket index (0 to capacity-1)
        """
        return hash(key) % self._capacity

    def _calculate_load_factor(self):
        """Calculate the current load factor of the hashmap.

        Returns:
            The load factor (size / capacity)
        """
        return self._size / self._capacity

    def _rehash(self):
        """Rehash the hashmap by doubling the capacity and redistributing all
        entries."""
        new_capacity = self._capacity * 2
        new_table = [None] * new_capacity

        def add_to_new_table(bucket: int, node: "UserHashMap.HashNode"):
            current = new_table[bucket]

            # if new hash table at the bucket is empty
            if not current:
                new_table[bucket] = node

            # otherwise, traverse chain and add at end
            else:
                prev = None
                while current:
                    prev = current
                    current = current.next_node
                prev.next_node = node

        # traverse old hash table
        for node in self._hash_table:
            # if bucket in old table is non-empty, move the nodes
            if node:
                current = node

                # traverse chain
                while current:
                    next_node_node = current.next_node
                    new_bucket = hash(current.key) % new_capacity
                    # Disconnect the node from the old chain before moving it
                    current.next_node = None
                    add_to_new_table(new_bucket, current)
                    current = next_node_node

        self._capacity = new_capacity
        self._hash_table = new_table

    # 5. Public interface methods (alphabetical order)
    def clear(self):
        """Remove all key-value pairs from the hashmap.

        Returns:
            None
        """
        self._hash_table = [None] * self._capacity
        self._size = 0

    def contains(self, key: Any) -> bool:
        """Check if a key exists in the hashmap.

        Args:
            key: The key to check

        Returns:
            True if the key exists, False otherwise
        """
        bucket = self._calculate_bucket_index(key)
        current = self._hash_table[bucket]

        # traverse chain looking for key
        while current:
            if current.key == key:
                return True
            current = current.next_node

        # key not found
        return False

    def get(self, key: Any) -> Optional[Any]:
        """Retrieve the value associated with a key.

        Args:
            key: The key to look up

        Returns:
            The value associated with the key, or None if key doesn't exist
        """
        bucket = self._calculate_bucket_index(key)
        node = self._hash_table[bucket]

        # traverse chain looking for key
        current = node
        while current:
            if current.key == key:
                return current.value
            current = current.next_node

        # key was not found
        return None

    def put(self, key: Any, value: Any) -> None:
        """Insert or update a key-value pair in the hashmap.

        Args:
            key: The key to insert (must be hashable)
            value: The value to associate with the key

        Returns:
            None
        """
        bucket = self._calculate_bucket_index(key)
        current = self._hash_table[bucket]

        # if bucket is empty, create new node directly
        if not current:
            self._hash_table[bucket] = self.HashNode(key, value)
            self._size += 1
            if (
                self._calculate_load_factor()
                > self.DEFAULT_LOAD_FACTOR_THRESHOLD
            ):
                self._rehash()
            return

        # otherwise, traverse the chain
        prev = None
        while current:
            if current.key == key:
                current.value = value
                return
            prev = current
            current = current.next_node

        # add new node at end of chain for new keys
        prev.next_node = self.HashNode(key, value)
        self._size += 1
        if self._calculate_load_factor() > self.DEFAULT_LOAD_FACTOR_THRESHOLD:
            self._rehash()

    def remove(self, key: Any) -> None:
        """Remove a key-value pair from the hashmap.

        Args:
            key: The key to remove

        Returns:
            None (does nothing if key doesn't exist)
        """
        bucket = self._calculate_bucket_index(key)
        current = self._hash_table[bucket]
        prev = None

        while current:
            if current.key == key:
                # removing the first node in the bucket
                if prev is None:
                    self._hash_table[bucket] = current.next_node

                # removing a node in the middle/end
                else:
                    prev.next_node = current.next_node

                self._size -= 1
                return

            # continue traversing the list
            prev = current
            current = current.next_node

        # key not found - do nothing

    def size(self) -> int:
        """Return the number of key-value pairs in the hashmap.

        Returns:
            The number of entries in the hashmap
        """
        return self._size


class CanonicalHashMap:
    """Canonical implementation of a hashmap using hash table with chaining.

    This implementation supports basic dictionary operations with O(1) average
    time complexity for all operations.
    """

    def __init__(self, initial_capacity: int = 16):
        """Initialize the hashmap with a given initial capacity.

        Args:
            initial_capacity: The initial number of buckets in the hash table
        """
        self.capacity = initial_capacity
        self._size = 0
        self.table = [None] * self.capacity
        self.load_factor_threshold = 0.75

    def _hash(self, key):
        """Calculate hash value for a key.

        Args:
            key: The key to hash

        Returns:
            Hash value for the key
        """
        return hash(key) % self.capacity

    def _resize(self):
        """Resize the hashmap when load factor exceeds threshold."""
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self._size = 0

        # Rehash all existing entries
        for bucket in old_table:
            current = bucket
            while current:
                next_node = current.next
                current.next = None  # Disconnect from old chain
                self._insert_node(current)
                current = next_node

    def _insert_node(self, node):
        """Insert a node into the hashmap.

        Args:
            node: The HashNode to insert
        """
        bucket = self._hash(node.key)

        if self.table[bucket] is None:
            self.table[bucket] = node
        else:
            # Handle collision by chaining
            current = self.table[bucket]
            while current.next:
                if current.key == node.key:
                    current.value = node.value
                    return
                current = current.next

            if current.key == node.key:
                current.value = node.value
            else:
                current.next = node

        self._size += 1

    def put(self, key, value):
        """Insert or update a key-value pair in the hashmap.

        Args:
            key: The key to insert (must be hashable)
            value: The value to associate with the key

        Returns:
            None
        """
        # Check if resize is needed
        if (self._size + 1) / self.capacity > self.load_factor_threshold:
            self._resize()

        bucket = self._hash(key)

        # If bucket is empty, create new node
        if self.table[bucket] is None:
            self.table[bucket] = HashNode(key, value)
            self._size += 1
            return

        # Search for existing key in chain
        current = self.table[bucket]
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        # Key not found, add new node at end of chain
        current = self.table[bucket]
        while current.next:
            current = current.next
        current.next = HashNode(key, value)
        self._size += 1

    def get(self, key):
        """Retrieve the value associated with a key.

        Args:
            key: The key to look up

        Returns:
            The value associated with the key, or None if key doesn't exist
        """
        bucket = self._hash(key)
        current = self.table[bucket]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def remove(self, key):
        """Remove a key-value pair from the hashmap.

        Args:
            key: The key to remove

        Returns:
            None (does nothing if key doesn't exist)
        """
        bucket = self._hash(key)
        current = self.table[bucket]
        prev = None

        while current:
            if current.key == key:
                if prev is None:
                    # Removing first node in bucket
                    self.table[bucket] = current.next
                else:
                    # Removing node in middle or end
                    prev.next = current.next
                self._size -= 1
                return
            prev = current
            current = current.next

    def contains(self, key):
        """Check if a key exists in the hashmap.

        Args:
            key: The key to check

        Returns:
            True if the key exists, False otherwise
        """
        return self.get(key) is not None

    def size(self):
        """Return the number of key-value pairs in the hashmap.

        Returns:
            The number of entries in the hashmap
        """
        return self._size

    def clear(self):
        """Remove all key-value pairs from the hashmap.

        Returns:
            None
        """
        self.table = [None] * self.capacity
        self._size = 0


class HashNode:
    """Node class for hashmap chaining."""

    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


def user_solution():
    """User-submitted solution for the hashmap implementation challenge.

    Returns:
        A UserHashMap instance with the user's implementation
    """
    return UserHashMap()


def canonical_solution():
    """Canonical solution for the hashmap implementation challenge.

    Returns:
        A CanonicalHashMap instance with the reference implementation
    """
    return CanonicalHashMap()

# Hashmap Implementation - Detailed Explanation

## Problem Recap

This problem asks us to implement a hashmap (dictionary) data structure from scratch. A hashmap provides O(1) average time complexity for insert, delete, and search operations by using a hash function to map keys to array indices. The key challenge is handling hash collisions, which occur when multiple keys hash to the same index.

## High-level Approach

The solution uses a **hash table with chaining** for collision resolution. The core idea is:
1. Use a hash function to map keys to bucket indices
2. Store key-value pairs in nodes within each bucket
3. Handle collisions by chaining nodes together in linked lists
4. Resize the table when load factor exceeds threshold to maintain O(1) performance

## Step-by-step Breakdown

### 1. Data Structure Design

```python
class HashNode:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next
```

Each node stores a key-value pair and a pointer to the next node in the chain.

### 2. Hash Function

```python
def _hash(self, key):
    return hash(key) % self.capacity
```

The hash function converts any hashable key into an integer index within the table's capacity. Using Python's built-in `hash()` function provides good distribution for most data types.

### 3. Put Operation Algorithm

```python
def put(self, key, value):
    # Check if resize is needed
    if (self.size + 1) / self.capacity > self.load_factor_threshold:
        self._resize()
    
    bucket = self._hash(key)
    
    # If bucket is empty, create new node
    if self.table[bucket] is None:
        self.table[bucket] = HashNode(key, value)
        self.size += 1
        return
    
    # Search for existing key in chain
    current = self.table[bucket]
    while current:
        if current.key == key:
            current.value = value  # Update existing key
            return
        current = current.next
    
    # Key not found, add new node at end of chain
    current = self.table[bucket]
    while current.next:
        current = current.next
    current.next = HashNode(key, value)
    self.size += 1
```

**Key Steps:**
1. **Load Factor Check**: Calculate if resize is needed before insertion
2. **Bucket Calculation**: Use hash function to find target bucket
3. **Empty Bucket**: If bucket is empty, create first node
4. **Key Search**: Traverse chain looking for existing key
5. **Update or Insert**: Either update existing value or append new node

### 4. Get Operation Algorithm

```python
def get(self, key):
    bucket = self._hash(key)
    current = self.table[bucket]
    
    while current:
        if current.key == key:
            return current.value
        current = current.next
    
    return None  # Key not found
```

**Key Steps:**
1. **Hash to Bucket**: Calculate bucket index
2. **Chain Traversal**: Search through linked list
3. **Key Comparison**: Return value if key matches
4. **Not Found**: Return None if key doesn't exist

### 5. Remove Operation Algorithm

```python
def remove(self, key):
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
            self.size -= 1
            return
        prev = current
        current = current.next
```

**Key Steps:**
1. **Find Node**: Traverse chain with previous pointer
2. **First Node Removal**: Update bucket pointer directly
3. **Middle/End Removal**: Update previous node's next pointer
4. **Size Update**: Decrement size counter

### 6. Rehashing Algorithm

```python
def _resize(self):
    old_table = self.table
    self.capacity *= 2
    self.table = [None] * self.capacity
    self.size = 0
    
    # Rehash all existing entries
    for bucket in old_table:
        current = bucket
        while current:
            next_node = current.next
            current.next = None  # Disconnect from old chain
            self._insert_node(current)
            current = next_node
```

**Key Steps:**
1. **Save Old Table**: Store reference to current table
2. **Double Capacity**: Create new table with doubled size
3. **Reset Size**: Start with zero entries
4. **Rehash All**: Process every node in old table
5. **Disconnect Nodes**: Prevent circular references
6. **Reinsert**: Add each node to new table

## Annotated Code Analysis

### Critical Implementation Details

**1. Load Factor Management**
```python
if (self.size + 1) / self.capacity > self.load_factor_threshold:
```
This check prevents the table from becoming too full, which would degrade performance to O(n). The threshold of 0.75 balances space and time efficiency.

**2. Node Disconnection During Rehashing**
```python
current.next = None  # Disconnect from old chain
```
This is crucial! Without disconnecting nodes, circular references can cause infinite loops during rehashing.

**3. Size Tracking**
```python
self.size += 1  # Only increment for new insertions
```
Size should only increase when adding new keys, not when updating existing ones.

**4. Empty Bucket Handling**
```python
if self.table[bucket] is None:
    self.table[bucket] = HashNode(key, value)
```
This prevents AttributeError when trying to access `.next` on None.

## Test Cases Analysis

The provided test cases cover:

1. **Basic Operations**: Verify put, get, contains, size work correctly
2. **Collision Handling**: Test with 100 entries to ensure chaining works
3. **Edge Cases**: Empty hashmap, non-existent keys, duplicate keys
4. **Different Types**: String, int, tuple, boolean keys and various value types
5. **Remove Operations**: First node, middle node, non-existent key removal
6. **Clear Functionality**: Reset to empty state
7. **Initial Capacity**: Verify custom capacity handling

## Common Pitfalls

### 1. Forgetting Node Disconnection
```python
# WRONG - causes infinite loops
current.next = next_node
self._insert_node(current)

# CORRECT - disconnect first
current.next = None
self._insert_node(current)
```

### 2. Incorrect Size Tracking
```python
# WRONG - increments size on updates
self.size += 1

# CORRECT - only increment for new keys
if key_exists:
    update_value()
else:
    self.size += 1
```

### 3. Not Handling Empty Buckets
```python
# WRONG - AttributeError on None
current = self.table[bucket]
current.next = new_node

# CORRECT - check for empty bucket
if self.table[bucket] is None:
    self.table[bucket] = new_node
```

### 4. Memory Leaks in Remove
```python
# WRONG - doesn't update pointers properly
del current

# CORRECT - update previous node's pointer
prev.next = current.next
```

## Time Complexity Analysis

| Operation | Average Case | Worst Case | Explanation |
|-----------|--------------|------------|-------------|
| put       | O(1)        | O(n)       | Hash + chain traversal |
| get       | O(1)        | O(n)       | Hash + chain traversal |
| remove    | O(1)        | O(n)       | Hash + chain traversal |
| contains  | O(1)        | O(n)       | Uses get() internally |
| size      | O(1)        | O(1)       | Stored counter |
| clear     | O(n)        | O(n)       | Must process all nodes |

**Average Case**: When hash function distributes keys evenly and load factor is maintained
**Worst Case**: When all keys hash to the same bucket, creating a single long chain

## Space Complexity

- **Average**: O(n) where n is the number of entries
- **Worst**: O(n) when all keys hash to the same bucket
- **Overhead**: Each node stores key, value, and next pointer

## Variations and Extensions

### 1. Open Addressing
Instead of chaining, use probing strategies:
- **Linear Probing**: Try next bucket sequentially
- **Quadratic Probing**: Try buckets with quadratic spacing
- **Double Hashing**: Use second hash function for probe sequence

### 2. Different Growth Strategies
- **Linear Growth**: Simpler but can lead to frequent resizing
- **Exponential Growth**: Better amortized cost but more memory

### 3. Custom Hash Functions
- **String-specific**: Optimize for string keys
- **Cryptographic**: Better distribution but slower
- **Perfect Hashing**: No collisions but complex setup

## Relevant Literature

1. **Introduction to Algorithms (CLRS)**: Chapter 11 covers hash tables in detail
2. **Java HashMap Implementation**: OpenJDK's implementation uses similar chaining approach
3. **Python Dictionary Implementation**: CPython uses open addressing with probing
4. **Hash Table Wikipedia**: Comprehensive overview of different collision resolution strategies

## Performance Considerations

### Memory Usage
- Each node: key + value + next pointer overhead
- Table array: capacity × pointer size
- Total: O(n) space for n entries

### Cache Performance
- **Chaining**: Sequential access within chains is cache-friendly
- **Random Access**: Bucket access may cause cache misses
- **Optimization**: Consider using arrays instead of linked lists for small chains

### Thread Safety
- This implementation is not thread-safe
- Would need locks or atomic operations for concurrent access
- Consider using `concurrent.futures.ThreadPoolExecutor` for parallel operations 
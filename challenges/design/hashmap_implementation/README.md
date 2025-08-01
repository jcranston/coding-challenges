# Hashmap Implementation

## Problem

Implement a hashmap (dictionary) data structure from scratch using a hash table with chaining for collision resolution. Your implementation should support the following operations:

- `put(key, value)`: Insert or update a key-value pair
- `get(key)`: Retrieve the value associated with a key
- `remove(key)`: Remove a key-value pair
- `contains(key)`: Check if a key exists in the hashmap
- `size()`: Return the number of key-value pairs
- `clear()`: Remove all key-value pairs

The hashmap should handle collisions using chaining (linked lists) and should resize when the load factor exceeds a threshold.

## Examples

```python
# Create a new hashmap
hashmap = HashMap()

# Basic operations
hashmap.put("apple", 1)
hashmap.put("banana", 2)
hashmap.put("cherry", 3)

print(hashmap.get("apple"))    # Output: 1
print(hashmap.get("banana"))   # Output: 2
print(hashmap.contains("cherry"))  # Output: True
print(hashmap.size())          # Output: 3

# Update existing key
hashmap.put("apple", 10)
print(hashmap.get("apple"))    # Output: 10

# Remove key
hashmap.remove("banana")
print(hashmap.contains("banana"))  # Output: False
print(hashmap.size())          # Output: 2

# Handle non-existent key
print(hashmap.get("grape"))    # Output: None
```

## Constraints

- Keys can be any hashable type (strings, integers, etc.)
- Values can be any type
- The hashmap should handle collisions using chaining
- Implement dynamic resizing when load factor > 0.75
- All operations should have O(1) average time complexity
- The initial capacity should be 16 buckets

## Clarifications & Assumptions

- Use a simple hash function (e.g., `hash(key) % capacity`) for this implementation
- When resizing, rehash all existing key-value pairs into the new larger table
- The load factor is calculated as `number_of_entries / capacity`
- If a key doesn't exist, `get()` should return `None`
- `remove()` should do nothing if the key doesn't exist
- The hashmap should work with any hashable key type

## Notes

- Think about how to efficiently handle collisions using linked lists
- Consider the trade-offs between space and time complexity
- Pay attention to the resizing strategy and when to trigger it
- Remember to handle edge cases like null keys or duplicate keys
- Consider how to maintain O(1) average time complexity for all operations 
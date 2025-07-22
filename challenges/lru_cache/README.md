# LRU Cache

## Problem
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:
- `get(key)`: Return the value of the key if the key exists in the cache, otherwise return -1.
- `put(key, value)`: Update or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

Implement the LRUCache class:
- `LRUCache(int capacity)` initializes the cache with positive size capacity.
- `int get(int key)` returns the value of the key if the key exists, otherwise -1.
- `void put(int key, int value)` updates or inserts the value.

## Example
```
Input:
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
Output:
[null,null,null,1,null,-1,null,-1,3,4]
Explanation:
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // returns 1
lRUCache.put(3, 3); // evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // returns -1 (not found)
lRUCache.get(3);    // returns 3
lRUCache.get(4);    // returns 4
```

## Constraints
- 1 <= capacity <= 3000
- 0 <= key, value <= 10^4
- At most 3 * 10^4 calls will be made to get and put.

## Clarifications & Assumptions
- All operations must run in O(1) average time complexity.
- The cache must evict the least recently used item when full.
- Keys and values are integers.
- The cache is initially empty.

## Approach
Describe your approach and thought process after attempting the problem. Consider using a hash map and a doubly linked list for O(1) operations.

## Notes
- Edge cases: repeated puts, gets for missing keys, capacity 1, updating existing keys, all keys unique, all keys the same. 
from .solution import LRUCache


def test_lru_cache_basic():
    cache = LRUCache(2)
    cache.put(1, 1)  # cache is {1=1}
    cache.put(2, 2)  # cache is {1=1, 2=2}
    assert cache.get(1) == 1  # returns 1
    cache.put(3, 3)  # evicts key 2, cache is {1=1, 3=3}
    assert cache.get(2) == -1  # returns -1 (not found)
    cache.put(4, 4)  # evicts key 1, cache is {4=4, 3=3}
    assert cache.get(1) == -1  # returns -1 (not found)
    assert cache.get(3) == 3  # returns 3
    assert cache.get(4) == 4  # returns 4


def test_lru_cache_update():
    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(2, 2)
    assert cache.get(2) == 2  # returns 2
    cache.put(1, 1)
    cache.put(4, 1)  # evicts key 2
    assert cache.get(2) == -1  # returns -1 (not found)


def test_lru_cache_capacity_one():
    cache = LRUCache(1)
    cache.put(1, 1)
    assert cache.get(1) == 1
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2

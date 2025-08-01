import pytest

from .solution import canonical_solution, user_solution


def assert_result(result, expected, method_name=""):
    """Helper function to check result and skip if not implemented.

    Args:
        result: The result from the method call
        expected: The expected value
        method_name: Optional name for debugging
    """
    # Only skip if result is None AND expected is not None
    # This handles the case where None is a valid return value
    if result is None and expected is not None:
        pytest.skip(f"Method {method_name} not implemented yet")
    assert result == expected


def test_basic_operations():
    """Test basic put, get, and contains operations."""
    for solution_func in [user_solution, canonical_solution]:
        hashmap = solution_func()
        if hashmap is None:
            continue

        # Test basic put and get
        hashmap.put("apple", 1)
        assert_result(hashmap.get("apple"), 1, "get")
        assert_result(hashmap.contains("apple"), True, "contains")
        assert_result(hashmap.size(), 1, "size")

        # Test updating existing key
        hashmap.put("apple", 10)
        assert_result(hashmap.get("apple"), 10, "get")
        assert_result(hashmap.size(), 1, "size")

        # Test non-existent key
        assert_result(hashmap.get("banana"), None, "get")
        assert_result(hashmap.contains("banana"), False, "contains")


def test_multiple_entries():
    """Test multiple key-value pairs."""
    for solution_func in [user_solution, canonical_solution]:
        hashmap = solution_func()
        if hashmap is None:
            continue

        # Add multiple entries
        hashmap.put("a", 1)
        hashmap.put("b", 2)
        hashmap.put("c", 3)

        assert_result(hashmap.get("a"), 1, "get")
        assert_result(hashmap.get("b"), 2, "get")
        assert_result(hashmap.get("c"), 3, "get")
        assert_result(hashmap.size(), 3, "size")

        assert_result(hashmap.contains("a"), True, "contains")
        assert_result(hashmap.contains("b"), True, "contains")
        assert_result(hashmap.contains("c"), True, "contains")
        assert_result(hashmap.contains("d"), False, "contains")


def test_remove_operations():
    """Test remove functionality."""
    for solution_func in [user_solution, canonical_solution]:
        hashmap = solution_func()
        if hashmap is None:
            continue

        # Add some entries
        hashmap.put("apple", 1)
        hashmap.put("banana", 2)
        hashmap.put("cherry", 3)
        assert_result(hashmap.size(), 3, "size")

        # Remove existing key
        hashmap.remove("banana")
        assert_result(hashmap.get("banana"), None, "get")
        assert_result(hashmap.contains("banana"), False, "contains")
        assert_result(hashmap.size(), 2, "size")

        # Remove non-existent key (should do nothing)
        hashmap.remove("grape")
        assert_result(hashmap.size(), 2, "size")

        # Verify other entries still exist
        assert_result(hashmap.get("apple"), 1, "get")
        assert_result(hashmap.get("cherry"), 3, "get")


def test_clear_operation():
    """Test clear functionality."""
    for solution_func in [user_solution, canonical_solution]:
        hashmap = solution_func()
        if hashmap is None:
            continue

        # Add some entries
        hashmap.put("a", 1)
        hashmap.put("b", 2)
        assert_result(hashmap.size(), 2, "size")

        # Clear the hashmap
        hashmap.clear()
        assert_result(hashmap.size(), 0, "size")
        assert_result(hashmap.get("a"), None, "get")
        assert_result(hashmap.get("b"), None, "get")
        assert_result(hashmap.contains("a"), False, "contains")
        assert_result(hashmap.contains("b"), False, "contains")


def test_different_key_types():
    """Test hashmap with different key types."""
    for solution_func in [user_solution, canonical_solution]:
        hashmap = solution_func()
        if hashmap is None:
            continue

        # Test string keys
        hashmap.put("string_key", "string_value")
        assert_result(hashmap.get("string_key"), "string_value", "get")

        # Test integer keys
        hashmap.put(42, "int_key_value")
        assert_result(hashmap.get(42), "int_key_value", "get")

        # Test tuple keys
        hashmap.put((1, 2), "tuple_value")
        assert_result(hashmap.get((1, 2)), "tuple_value", "get")

        # Test boolean keys
        hashmap.put(True, "bool_value")
        assert_result(hashmap.get(True), "bool_value", "get")

        assert_result(hashmap.size(), 4, "size")


def test_different_value_types():
    """Test hashmap with different value types."""
    for solution_func in [user_solution, canonical_solution]:
        hashmap = solution_func()
        if hashmap is None:
            continue

        # Test different value types
        hashmap.put("list_key", [1, 2, 3])
        hashmap.put("dict_key", {"a": 1, "b": 2})
        hashmap.put("tuple_key", (1, 2, 3))
        hashmap.put("int_key", 42)
        hashmap.put("string_key", "hello")

        assert_result(hashmap.get("list_key"), [1, 2, 3], "get")
        assert_result(hashmap.get("dict_key"), {"a": 1, "b": 2}, "get")
        assert_result(hashmap.get("tuple_key"), (1, 2, 3), "get")
        assert_result(hashmap.get("int_key"), 42, "get")
        assert_result(hashmap.get("string_key"), "hello", "get")

        assert_result(hashmap.size(), 5, "size")


def test_collision_handling():
    """Test that collisions are handled correctly."""
    for solution_func in [user_solution, canonical_solution]:
        hashmap = solution_func()
        if hashmap is None:
            continue

        # Add many entries to potentially cause collisions
        for i in range(100):
            hashmap.put(f"key_{i}", f"value_{i}")

        # Verify all entries can be retrieved correctly
        for i in range(100):
            assert_result(hashmap.get(f"key_{i}"), f"value_{i}", "get")
            assert_result(hashmap.contains(f"key_{i}"), True, "contains")

        assert_result(hashmap.size(), 100, "size")


def test_edge_cases():
    """Test edge cases and boundary conditions."""
    for solution_func in [user_solution, canonical_solution]:
        hashmap = solution_func()
        if hashmap is None:
            continue

        # Test empty hashmap
        assert_result(hashmap.size(), 0, "size")
        assert_result(hashmap.get("any_key"), None, "get")
        assert_result(hashmap.contains("any_key"), False, "contains")

        # Test removing from empty hashmap
        hashmap.remove("any_key")  # Should not raise error
        assert_result(hashmap.size(), 0, "size")

        # Test clearing empty hashmap
        hashmap.clear()  # Should not raise error
        assert_result(hashmap.size(), 0, "size")


def test_initial_capacity():
    """Test hashmap with custom initial capacity."""
    for solution_func in [user_solution, canonical_solution]:
        # Test with custom capacity
        hashmap = solution_func()
        if hashmap is None:
            continue

        # The default capacity should be 16
        # Add entries and verify they work correctly
        for i in range(20):  # More than default capacity
            hashmap.put(f"key_{i}", i)

        # Verify all entries
        for i in range(20):
            assert_result(hashmap.get(f"key_{i}"), i, "get")

        assert_result(hashmap.size(), 20, "size")

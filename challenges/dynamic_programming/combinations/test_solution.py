import pytest

from .solution import (
    combinations_canonical_bottom_up,
    combinations_canonical_top_down,
    combinations_user_bottom_up,
    combinations_user_top_down,
)

# List of all methods to test
ALL_METHODS = [
    combinations_user_top_down,
    combinations_user_bottom_up,
    combinations_canonical_top_down,
    combinations_canonical_bottom_up,
]


def assert_all_methods(n: int, k: int, expected: int):
    """Helper function to test all methods with the same inputs."""
    for method in ALL_METHODS:
        result = method(n, k)
        if result is None:
            continue  # Not implemented yet
        assert result == expected, f"Method {method.__name__} failed"


@pytest.mark.parametrize(
    "n, k, expected",
    [
        (5, 2, 10),  # C(5,2) = 10
        (5, 3, 10),  # C(5,3) = 10
        (4, 2, 6),  # C(4,2) = 6
        (6, 3, 20),  # C(6,3) = 20
        (7, 4, 35),  # C(7,4) = 35
        (8, 5, 56),  # C(8,5) = 56
    ],
)
def test_combinations(n: int, k: int, expected: int):
    """Test all combinations methods with various input combinations."""
    assert_all_methods(n, k, expected)


def test_edge_cases():
    """Test edge cases for all methods."""
    # Base cases
    assert_all_methods(5, 0, 1)  # C(n,0) = 1
    assert_all_methods(5, 5, 1)  # C(n,n) = 1
    assert_all_methods(0, 0, 1)  # C(0,0) = 1

    # Invalid cases (k > n)
    assert_all_methods(3, 5, 0)  # C(3,5) = 0
    assert_all_methods(2, 3, 0)  # C(2,3) = 0


def test_small_values():
    """Test small values for all methods."""
    # Small n values
    assert_all_methods(1, 0, 1)  # C(1,0) = 1
    assert_all_methods(1, 1, 1)  # C(1,1) = 1
    assert_all_methods(2, 0, 1)  # C(2,0) = 1
    assert_all_methods(2, 1, 2)  # C(2,1) = 2
    assert_all_methods(2, 2, 1)  # C(2,2) = 1
    assert_all_methods(3, 1, 3)  # C(3,1) = 3
    assert_all_methods(3, 2, 3)  # C(3,2) = 3


def test_pascal_triangle_values():
    """Test values that correspond to Pascal's triangle."""
    # Row 4: [1, 4, 6, 4, 1]
    assert_all_methods(4, 0, 1)  # C(4,0) = 1
    assert_all_methods(4, 1, 4)  # C(4,1) = 4
    assert_all_methods(4, 2, 6)  # C(4,2) = 6
    assert_all_methods(4, 3, 4)  # C(4,3) = 4
    assert_all_methods(4, 4, 1)  # C(4,4) = 1

    # Row 5: [1, 5, 10, 10, 5, 1]
    assert_all_methods(5, 0, 1)  # C(5,0) = 1
    assert_all_methods(5, 1, 5)  # C(5,1) = 5
    assert_all_methods(5, 2, 10)  # C(5,2) = 10
    assert_all_methods(5, 3, 10)  # C(5,3) = 10
    assert_all_methods(5, 4, 5)  # C(5,4) = 5
    assert_all_methods(5, 5, 1)  # C(5,5) = 1

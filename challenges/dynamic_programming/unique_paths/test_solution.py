import pytest

from .solution import canonical_unique_paths, user_unique_paths


def assert_result(result, expected, method_name=""):
    """Helper function to check result and skip if not implemented.

    Args:
        result: The result from the method call
        expected: The expected value
        method_name: Optional name for debugging
    """
    if result is None:
        pytest.skip(f"Method {method_name} not implemented yet")
    assert result == expected


def test_unique_paths_basic():
    """Test basic cases for unique paths."""
    test_cases = [
        (1, 1, 1),  # Single cell
        (1, 2, 1),  # Single row
        (2, 1, 1),  # Single column
        (2, 2, 2),  # 2x2 grid
        (2, 3, 3),  # 2x3 grid
        (3, 2, 3),  # 3x2 grid
    ]

    for func in [user_unique_paths, canonical_unique_paths]:
        for m, n, expected in test_cases:
            result = func(m, n)
            assert_result(result, expected, f"unique_paths({m}, {n})")


def test_unique_paths_medium():
    """Test medium-sized grids."""
    test_cases = [
        (3, 3, 6),  # 3x3 grid
        (3, 7, 28),  # 3x7 grid
        (7, 3, 28),  # 7x3 grid
        (4, 4, 20),  # 4x4 grid
    ]

    for func in [user_unique_paths, canonical_unique_paths]:
        for m, n, expected in test_cases:
            result = func(m, n)
            assert_result(result, expected, f"unique_paths({m}, {n})")


def test_unique_paths_large():
    """Test larger grids."""
    test_cases = [
        (5, 5, 70),  # 5x5 grid
        (6, 6, 252),  # 6x6 grid
        (7, 7, 924),  # 7x7 grid
        (10, 10, 48620),  # 10x10 grid
    ]

    for func in [user_unique_paths, canonical_unique_paths]:
        for m, n, expected in test_cases:
            result = func(m, n)
            assert_result(result, expected, f"unique_paths({m}, {n})")


def test_unique_paths_rectangular():
    """Test rectangular grids."""
    test_cases = [
        (2, 5, 5),  # 2x5 grid
        (5, 2, 5),  # 5x2 grid
        (3, 8, 36),  # 3x8 grid
        (8, 3, 36),  # 8x3 grid
        (4, 6, 56),  # 4x6 grid
        (6, 4, 56),  # 6x4 grid
    ]

    for func in [user_unique_paths, canonical_unique_paths]:
        for m, n, expected in test_cases:
            result = func(m, n)
            assert_result(result, expected, f"unique_paths({m}, {n})")


def test_unique_paths_edge_cases():
    """Test edge cases and boundary conditions."""
    test_cases = [
        (1, 100, 1),  # Single row, many columns
        (100, 1, 1),  # Many rows, single column
        (2, 100, 100),  # 2 rows, many columns
        (100, 2, 100),  # Many rows, 2 columns
    ]

    for func in [user_unique_paths, canonical_unique_paths]:
        for m, n, expected in test_cases:
            result = func(m, n)
            assert_result(result, expected, f"unique_paths({m}, {n})")

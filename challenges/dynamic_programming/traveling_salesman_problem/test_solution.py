from typing import List

import pytest

from .solution import (
    solve_tsp_canonical_backtrack,
    solve_tsp_canonical_dp,
    solve_tsp_user,
    solve_tsp_user_backtrack,
)

# List of all methods to test
ALL_METHODS = [
    solve_tsp_user,
    solve_tsp_user_backtrack,
    solve_tsp_canonical_dp,
    solve_tsp_canonical_backtrack,
]


def assert_all_methods(distances: List[List[int]], expected: int):
    """Helper function to test all methods with the same inputs."""
    for method in ALL_METHODS:
        result = method(distances)
        if result is None:
            continue  # Not implemented yet
        assert result == expected, f"Method {method.__name__} failed"


@pytest.mark.parametrize(
    "distances, expected",
    [
        (
            [
                [0, 10, 15, 20],
                [10, 0, 35, 25],
                [15, 35, 0, 30],
                [20, 25, 30, 0],
            ],
            80,
        ),
        (
            [
                [0, 20, 42, 35],
                [20, 0, 30, 34],
                [42, 30, 0, 12],
                [35, 34, 12, 0],
            ],
            97,
        ),
        ([[0, 1, 2], [1, 0, 3], [2, 3, 0]], 6),
        ([[0, 5, 8, 6], [5, 0, 9, 7], [8, 9, 0, 4], [6, 7, 4, 0]], 24),
        # Larger instance (5 cities)
        (
            [
                [0, 12, 10, 19, 8],
                [12, 0, 3, 7, 2],
                [10, 3, 0, 6, 20],
                [19, 7, 6, 0, 4],
                [8, 2, 20, 4, 0],
            ],
            34,  # Optimal: 0 -> 1 -> 4 -> 3 -> 2 -> 0 (12 + 2 + 4 + 6 + 10)
        ),
        # All equal distances (except diagonal)
        (
            [
                [0, 5, 5, 5],
                [5, 0, 5, 5],
                [5, 5, 0, 5],
                [5, 5, 5, 0],
            ],
            15,  # Any tour has same cost: 5 * 3 = 15
        ),
        # Asymmetric distances - demonstrates directionality matters
        (
            [
                [0, 10, 15, 20],
                [5, 0, 35, 25],  # Different from [1][0] = 10
                [15, 35, 0, 30],
                [20, 25, 30, 0],
            ],
            75,  # Optimal: 0 -> 2 -> 3 -> 1 -> 0 (15 + 30 + 25 + 5)
        ),
    ],
)
def test_traveling_salesman_problem(distances, expected):
    """Test all TSP methods with various distance matrices."""
    assert_all_methods(distances, expected)


def test_edge_case_two_cities():
    """Test the simplest case with only 2 cities."""
    distances = [[0, 5], [5, 0]]
    expected = 10  # Must go 0 -> 1 -> 0
    assert_all_methods(distances, expected)


def test_edge_case_three_cities():
    """Test case with 3 cities to verify basic logic."""
    distances = [[0, 1, 2], [1, 0, 3], [2, 3, 0]]
    expected = 6  # Optimal tour: 0 -> 1 -> 2 -> 0 (1 + 3 + 2)
    assert_all_methods(distances, expected)


def test_edge_case_large_distances():
    """Test with very large distance values."""
    distances = [
        [0, 1000, 2000, 3000],
        [1000, 0, 1500, 2500],
        [2000, 1500, 0, 1000],
        [3000, 2500, 1000, 0],
    ]
    expected = 3500  # Optimal: 0 -> 1 -> 2 -> 3 -> 0 (1000 + 1500 + 1000)
    assert_all_methods(distances, expected)


def test_edge_case_small_distances():
    """Test with very small distance values."""
    distances = [
        [0, 1, 2, 3],
        [1, 0, 1, 2],
        [2, 1, 0, 1],
        [3, 2, 1, 0],
    ]
    expected = 4  # Optimal: 0 -> 1 -> 2 -> 3 -> 0 (1 + 1 + 1 + 1)
    assert_all_methods(distances, expected)


def test_asymmetric_edge_cases():
    """Test asymmetric distance scenarios."""
    # Case 1: Very asymmetric - one direction much cheaper
    distances = [
        [0, 1, 100, 100],
        [100, 0, 1, 100],
        [100, 100, 0, 1],
        [1, 100, 100, 0],
    ]
    expected = 4  # Optimal: 0 -> 1 -> 2 -> 3 -> 0 (1 + 1 + 1 + 1)
    assert_all_methods(distances, expected)

    # Case 2: Asymmetric with different optimal tours
    distances = [
        [0, 10, 20, 30],
        [5, 0, 15, 25],  # Much cheaper return path
        [25, 15, 0, 10],
        [35, 25, 5, 0],  # Very cheap return path
    ]
    expected = 35  # Optimal: 0 -> 1 -> 2 -> 3 -> 0 (10 + 15 + 10 + 0)
    assert_all_methods(distances, expected)

    # Case 3: 5-city asymmetric - larger instance
    distances = [
        [0, 10, 20, 30, 40],
        [5, 0, 15, 25, 35],  # Much cheaper return paths
        [25, 15, 0, 10, 20],
        [35, 25, 5, 0, 15],
        [45, 35, 25, 5, 0],  # Very cheap return paths
    ]
    expected = 45  # Optimal: 0 -> 1 -> 2 -> 3 -> 4 -> 0 (10 + 15 + 10 + 5 + 5)
    assert_all_methods(distances, expected)

    # Case 4: Extreme asymmetry - one direction blocked
    distances = [
        [0, 1, 999, 999],
        [999, 0, 1, 999],
        [999, 999, 0, 1],
        [1, 999, 999, 0],
    ]
    expected = 4  # Must follow the "cheap" path: 0 -> 1 -> 2 -> 3 -> 0
    assert_all_methods(distances, expected)

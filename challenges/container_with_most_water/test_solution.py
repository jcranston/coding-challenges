import pytest

from .solution import find_max_water_container_area


class TestContainerWithMostWater:
    """Test cases for the Container With Most Water problem."""

    def test_example_1(self):
        """Test the first example from the problem description."""
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        assert find_max_water_container_area(height) == expected

    def test_example_2(self):
        """Test the second example from the problem description."""
        height = [1, 1]
        expected = 1
        assert find_max_water_container_area(height) == expected

    def test_minimum_size(self):
        """Test with minimum array size (2 elements)."""
        height = [2, 3]
        expected = 2
        assert find_max_water_container_area(height) == expected

    def test_all_equal_heights(self):
        """Test with all heights being equal."""
        height = [5, 5, 5, 5, 5]
        expected = 20  # width=4, height=5
        assert find_max_water_container_area(height) == expected

    def test_increasing_heights(self):
        """Test with strictly increasing heights."""
        height = [1, 2, 3, 4, 5]
        expected = 6  # width=3, height=2 (between indices 1 and 4)
        assert find_max_water_container_area(height) == expected

    def test_decreasing_heights(self):
        """Test with strictly decreasing heights."""
        height = [5, 4, 3, 2, 1]
        expected = 6  # width=3, height=2 (between indices 0 and 3)
        assert find_max_water_container_area(height) == expected

    def test_zero_heights(self):
        """Test with some zero heights."""
        height = [0, 2, 0, 3, 0]
        expected = 4  # width=2, height=2 (between indices 1 and 3)
        assert find_max_water_container_area(height) == expected

    def test_single_peak(self):
        """Test with a single peak in the middle."""
        height = [1, 2, 3, 4, 3, 2, 1]
        expected = 8  # width=4, height=2 (between indices 1 and 5)
        assert find_max_water_container_area(height) == expected

    def test_two_peaks(self):
        """Test with two peaks of equal height."""
        height = [1, 3, 1, 3, 1]
        expected = 6  # width=2, height=3 (between indices 1 and 3)
        assert find_max_water_container_area(height) == expected

    def test_large_numbers(self):
        """Test with large height values."""
        height = [10000, 5000, 10000]
        expected = 20000  # width=2, height=10000 (between indices 0 and 2)
        assert find_max_water_container_area(height) == expected

    def test_alternating_heights(self):
        """Test with alternating high and low heights."""
        height = [10, 1, 10, 1, 10]
        expected = 40  # width=4, height=10 (between indices 0 and 4)
        assert find_max_water_container_area(height) == expected

    def test_edge_case_maximum_width(self):
        """Test case where maximum area is achieved with maximum width."""
        height = [1, 2, 1]
        expected = 2  # width=2, height=1 (between indices 0 and 2)
        assert find_max_water_container_area(height) == expected

    def test_edge_case_minimum_width(self):
        """Test case where maximum area is achieved with minimum width."""
        height = [5, 5]
        expected = 5  # width=1, height=5
        assert find_max_water_container_area(height) == expected

    def test_complex_case(self):
        """Test a more complex case with multiple local maxima."""
        height = [2, 3, 4, 5, 18, 17, 6]
        expected = 17  # width=1, height=17 (between indices 4 and 5)
        assert find_max_water_container_area(height) == expected


if __name__ == "__main__":
    pytest.main([__file__])

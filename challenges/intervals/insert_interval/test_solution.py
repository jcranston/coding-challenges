from .solution import canonical_solution, user_solution


def test_example():
    # Replace with actual test cases and expected output
    input_data = None
    expected = None
    for solution in [user_solution, canonical_solution]:
        assert solution(input_data) == expected

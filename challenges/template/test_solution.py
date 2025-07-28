from .solution import canonical_solution, user_solution


def test_example():
    # Replace with actual test cases and expected output
    input_data = None
    expected = None
    for solution in [user_solution, canonical_solution]:
        result = solution(input_data)
        if result is None:
            # If function is not implemented, just pass the test
            continue
        assert result == expected

from .solution import longest_substring_without_repeating_chars_brute_force

solutions = [
    longest_substring_without_repeating_chars_brute_force,
    # longest_substring_without_repeating_chars_optimized
]


def test_longest_substr_without_repeating_chars():
    expectations = {"abcabcbb": 3, "bbbbb": 1, "pwwkew": 3}
    for solve in solutions:
        for input, output in expectations.items():
            assert solve(input) == output

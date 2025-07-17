from .solution import solve_iterative, solve_recursive

solutions = [solve_recursive, solve_iterative]


def test_valid_parentheses_positive_cases():
    valid_cases = [
        "()",
        "()[]{}",
        "{[]}",
        "((()))",
        "(([])())",
        "",
        "([{}])",
        "(()())",
    ]
    for solve in solutions:
        for s in valid_cases:
            assert solve(s) is True, f"Failed for {solve.__name__}({s!r})"


def test_valid_parentheses_negative_cases():
    invalid_cases = ["(]", "([)]", "(", "([{})]", ")(", "([)"]
    for solve in solutions:
        for s in invalid_cases:
            assert solve(s) is False, f"Failed for {solve.__name__}({s!r})"

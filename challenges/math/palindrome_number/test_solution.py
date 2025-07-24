from .solution import palindrome_number


def test_palindrome_number_example():
    assert palindrome_number(12321) is True
    assert palindrome_number(121) is True
    assert palindrome_number(-121) is False
    assert palindrome_number(10) is False

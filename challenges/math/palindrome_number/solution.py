def palindrome_number(x: int) -> bool:
    """Returns True if x is a palindrome, False otherwise.

    Args:
        x: The input integer.

    Returns:
        True if x is a palindrome, False otherwise.

    Clarifications / Assumptions:
    - A palindrome is a number that reads the same backward as forward.
    - Negative numbers are not palindromes.
    - The function should return a boolean value.
    - Input will always be an integer.
    """
    # Negative numbers and numbers ending in 0 (except 0 itself) are not
    # palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_num = 0
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10

    # For even length: x == reversed_num
    # For odd length:  x == reversed_num // 10
    return x == reversed_num or x == reversed_num // 10

def is_happy(number):
    """
    Determines whether a number is happy or not.

    A happy number is defined by the following process:
    - Starting with any positive integer, replace the number by the sum of the squares of its digits.
    - Repeat the process until the number equals 1, or it loops endlessly in a cycle which does not include 1.
    - If the number equals 1, it is considered a happy number. Otherwise, it is not.

    Parameters:
    - number (int): The number to check for happiness.

    Returns:
    - bool: True if the number is happy, False otherwise.

    Example:
    >>> is_happy(19)
    True
    """
    set_number = set()
    while (number != 1) and (number not in set_number):
        set_number.add(number)
        number = sum([int(num) ** 2 for num in str(number)])
    return number == 1

if __name__ == "__main__":
    assert is_happy(7) is True
    assert is_happy(44) is True

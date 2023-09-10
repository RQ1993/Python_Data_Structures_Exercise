def number_compare(a, b):
    """Compare two numbers and return a string indicating the result.

    Args:
        a (float or int): The first number.
        b (float or int): The second number.

    Returns:
        str: A string indicating the comparison result:
             - 'Numbers are equal' if a and b are equal.
             - 'First is greater' if a is greater than b.
             - 'Second is greater' if b is greater than a.
    """
    if a == b:
        return 'Numbers are equal'
    elif a > b:
        return 'First is greater'
    else:
        return 'Second is greater'

# Test cases
print(number_compare(1, 1))   # Output: 'Numbers are equal'
print(number_compare(-1, 1))  # Output: 'Second is greater'
print(number_compare(1, -2))  # Output: 'First is greater'

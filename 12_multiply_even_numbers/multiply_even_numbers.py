def multiply_even_numbers(nums):
    """Multiply the even numbers in the list.

    Args:
        nums (list): The input list of numbers.

    Returns:
        int: The product of all even numbers in the list, or 1 if there are no even numbers.
    """
    product = 1

    for num in nums:
        if num % 2 == 0:
            # Multiply the even number by the current product
            product *= num

    return product if product != 1 else 1

# Test cases
print(multiply_even_numbers([2, 3, 4, 5, 6]))  # Output: 48
print(multiply_even_numbers([3, 4, 5]))        # Output: 4
print(multiply_even_numbers([1, 3, 5]))        # Output: 1

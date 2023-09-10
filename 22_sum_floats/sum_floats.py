def sum_floats(nums):
    """
    Return the sum of floating point numbers in nums.

    Args:
        nums (list): List of numbers (including floats and non-floats).

    Returns:
        float: The sum of floating point numbers in the list.
    """
    return sum(num for num in nums if isinstance(num, float))

# Example usage and test cases
print(sum_floats([1.5, 2.4, 'awesome', [], 1]))
# Output: 3.9

print(sum_floats([1, 2, 3]))
# Output: 0

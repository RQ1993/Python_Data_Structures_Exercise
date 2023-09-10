def triple_and_filter(nums):
    """
    Return a new list of tripled numbers for those numbers divisible by 4.

    Args:
        nums (list of int): List of numbers.

    Returns:
        list of int: New list containing tripled numbers for those divisible by 4.
    """
    return [num * 3 for num in nums if num % 4 == 0]

# Example usage and test cases
print(triple_and_filter([1, 2, 3, 4]))  # Output: [12] (4 is divisible by 4, and tripled)
print(triple_and_filter([6, 8, 10, 12]))  # Output: [24, 36] (8 and 12 are divisible by 4, and tripled)
print(triple_and_filter([1, 2]))  # Output: [] (No numbers divisible by 4)

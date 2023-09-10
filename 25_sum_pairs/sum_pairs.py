def sum_pairs(nums, goal):
    """
    Return the tuple of the first pair of numbers from nums that sum to the goal.

    Args:
        nums (list): List of numbers.
        goal (int): The target sum.

    Returns:
        tuple: A tuple containing the pair of numbers that sum to the goal.
    """
    seen = {}  # A dictionary to store seen numbers and their indices

    for num in nums:
        complement = goal - num  # Find the complement of the current number
        if complement in seen:
            # If the complement has been seen before, return the pair
            return (complement, num)
        seen[num] = True  # Mark the current number as seen

    # If no pair is found, return an empty tuple
    return ()

# Test cases
print(sum_pairs([1, 2, 2, 10], 4))  # Output: (2, 2)
print(sum_pairs([4, 2, 10, 5, 1], 6))  # Output: (4, 2)
print(sum_pairs([5, 1, 4, 8, 3, 2], 7))  # Output: (4, 3)
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))  # Output: ()

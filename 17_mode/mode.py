def mode(nums):
    """Return the most common number in the list.

    Args:
        nums (list): The input list of numbers.

    Returns:
        int: The most common number in the list.
    """
    # Create a dictionary to count the occurrences of each number
    num_counts = {}
    
    # Iterate through the list and count the occurrences of each number
    for num in nums:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
    
    # Find the number with the highest count (mode)
    most_common_num = max(num_counts, key=num_counts.get)
    
    return most_common_num

# Test cases
print(mode([1, 2, 1]))               # Output: 1
print(mode([2, 2, 3, 3, 2]))         # Output: 2

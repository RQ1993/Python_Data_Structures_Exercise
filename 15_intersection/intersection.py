def intersection(l1, l2):
    """Return a new list containing the intersection of two input lists.

    Args:
        l1 (list): The first input list.
        l2 (list): The second input list.

    Returns:
        list: A new list containing the common elements of l1 and l2.
    """
    return [item for item in l1 if item in l2]

# Test cases
print(intersection([1, 2, 3], [2, 3, 4]))       # Output: [2, 3]
print(intersection([1, 2, 3], [1, 2, 3, 4]))    # Output: [1, 2, 3]
print(intersection([1, 2, 3], [3, 4]))          # Output: [3]
print(intersection([1, 2, 3], [4, 5, 6]))       # Output: []

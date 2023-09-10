def frequency(lst, search_term):
    """Count the frequency of a term in a list.

    Args:
        lst (list): The input list.
        search_term: The term to search for in the list.

    Returns:
        int: The frequency of the search term in the list.
    """
    return lst.count(search_term)

# Test cases
print(frequency([1, 4, 3, 4, 4], 4))  # Output: 3
print(frequency([1, 4, 3], 7))        # Output: 0

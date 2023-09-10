def list_check(lst):
    """
    Check if all items in lst are lists.

    Args:
        lst (list): List of items.

    Returns:
        bool: True if all items in lst are lists, False otherwise.
    """
    return all(isinstance(item, list) for item in lst)

# Example usage and test cases
print(list_check([[1], [2, 3]]))
# Output: True

print(list_check([[1], "nope"]))
# Output: False

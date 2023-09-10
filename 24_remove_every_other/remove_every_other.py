def remove_every_other(lst):
    """
    Return a new list containing every other item from the original list.

    Args:
        lst (list): The original list.

    Returns:
        list: A new list containing every other item.
    """
    return lst[::2]

# Example usage and test case
lst = [1, 2, 3, 4, 5]
new_lst = remove_every_other(lst)
print(new_lst)
# Output: [1, 3, 5]

# The original list should not be mutated
print(lst)
# Output: [1, 2, 3, 4, 5]

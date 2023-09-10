def compact(lst):
    """Return a new list with non-true elements removed.

    Args:
        lst (list): The input list.

    Returns:
        list: A new list with non-true elements removed.
    """
    return [item for item in lst if item]

# Test case
print(compact([0, 1, 2, '', [], False, (), None, 'All done']))
# Output: [1, 2, 'All done']

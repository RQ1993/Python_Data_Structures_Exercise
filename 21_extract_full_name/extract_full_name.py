def extract_full_names(people):
    """
    Return a list of full names extracted from dictionaries containing 'first' and 'last' keys.

    Args:
        people (list of dict): List of dictionaries with 'first' and 'last' keys for first and last names.

    Returns:
        list of str: List of space-separated full names.
    """
    return [f"{person['first']} {person['last']}" for person in people]

# Example usage and test cases
names = [
    {'first': 'Ada', 'last': 'Lovelace'},
    {'first': 'Grace', 'last': 'Hopper'},
]

print(extract_full_names(names))
# Output: ['Ada Lovelace', 'Grace Hopper']

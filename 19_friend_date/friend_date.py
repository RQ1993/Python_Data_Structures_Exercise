def friend_date(a, b):
    """
    Given two friends, determine if they have any hobbies in common.

    Args:
        a (tuple): Friend #1, a tuple of (name, age, list-of-hobbies).
        b (tuple): Friend #2, same structure as 'a'.

    Returns:
        bool: True if they have any hobbies in common, False if not.
    """
    # Extract the list of hobbies for each friend
    hobbies_a = set(a[2])
    hobbies_b = set(b[2])

    # Check if there is any common hobby by taking the intersection of their hobby sets
    common_hobbies = hobbies_a.intersection(hobbies_b)

    # If the intersection set is not empty, they have at least one common hobby
    if common_hobbies:
        return True
    else:
        return False

# Example usage and test cases
elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

print(friend_date(elmo, sauron))  # Output: False (No common hobbies)
print(friend_date(sauron, gandalf))  # Output: True (They share the 'chess' hobby)

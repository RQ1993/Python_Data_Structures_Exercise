def capitalize(phrase):
    """Capitalize the first letter of the first word in a phrase.

    Args:
        phrase (str): The input phrase.

    Returns:
        str: The phrase with the first letter of the first word capitalized.
    """
    # Check if the phrase is not empty
    if phrase:
        # Capitalize the first letter of the first word
        return phrase[0].upper() + phrase[1:]
    else:
        return phrase

# Test cases
print(capitalize('python'))           # Output: 'Python'
print(capitalize('only first word'))   # Output: 'Only first word'
print(capitalize(''))                 # Output: '' (empty string remains empty)

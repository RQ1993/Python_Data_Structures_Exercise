def flip_case(phrase, to_swap):
    """Flip the case of each occurrence of to_swap in the phrase.

    Args:
        phrase (str): The input phrase.
        to_swap (str): The character to swap the case for.

    Returns:
        str: The modified phrase with case-swapped characters.
    """
    result = ""

    for char in phrase:
        if char.lower() == to_swap.lower():
            # Swap the case of the character
            result += char.swapcase()
        else:
            result += char

    return result

# Test cases
print(flip_case('Aaaahhh', 'a'))  # Output: 'aAAAhhh'
print(flip_case('Aaaahhh', 'A'))  # Output: 'aAAAhhh'
print(flip_case('Aaaahhh', 'h'))  # Output: 'AaaaHHH'

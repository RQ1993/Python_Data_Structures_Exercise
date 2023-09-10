def multiple_letter_count(phrase):
    """Count the frequency of each letter in a phrase and return a dictionary.

    Args:
        phrase (str): The input phrase.

    Returns:
        dict: A dictionary where keys are letters and values are their frequencies.
    """
    # Initialize an empty dictionary to store the letter frequencies
    letter_count = {}

    # Iterate through each character in the phrase
    for letter in phrase:
        # Check if the character is a letter (ignore non-letter characters)
        if letter.isalpha():
            # Convert the letter to lowercase for case-insensitive counting
            letter = letter.lower()
            
            # Update the letter count in the dictionary
            letter_count[letter] = letter_count.get(letter, 0) + 1

    return letter_count

# Test cases
print(multiple_letter_count('yay'))  # Output: {'y': 2, 'a': 1}
print(multiple_letter_count('Yay'))  # Output: {'y': 1, 'a': 1}

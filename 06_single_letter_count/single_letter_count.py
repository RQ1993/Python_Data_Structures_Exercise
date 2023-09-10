def single_letter_count(word, letter):
    """Count the number of times a letter appears in a word (case-insensitively).

    Args:
        word (str): The input word.
        letter (str): The letter to count (case-insensitive).

    Returns:
        int: The count of the specified letter in the word.
    """
    # Convert both the word and letter to lowercase for case-insensitive comparison
    word = word.lower()
    letter = letter.lower()

    # Use the count method to count occurrences of the letter in the word
    return word.count(letter)

# Test cases
print(single_letter_count('Hello World', 'h'))  # Output: 1
print(single_letter_count('Hello World', 'z'))  # Output: 0
print(single_letter_count("Hello World", 'l'))  # Output: 3

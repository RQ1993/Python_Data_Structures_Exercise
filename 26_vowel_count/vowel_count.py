def vowel_count(phrase):
    """
    Return a frequency map of vowels in the given phrase (case-insensitive).

    Args:
        phrase (str): The input phrase.

    Returns:
        dict: A dictionary containing the frequency of each vowel.
    """
    # Initialize a dictionary to store the vowel frequencies
    vowel_freq = {}
    
    # Define a set of vowels (both lowercase and uppercase)
    vowels = set("aeiouAEIOU")
    
    # Iterate through the characters in the phrase
    for char in phrase:
        # Check if the character is a vowel
        if char in vowels:
            # Convert the character to lowercase to make it case-insensitive
            char = char.lower()
            
            # Update the frequency count in the dictionary
            if char in vowel_freq:
                vowel_freq[char] += 1
            else:
                vowel_freq[char] = 1
    
    return vowel_freq

# Test cases
print(vowel_count('rithm school'))  # Output: {'i': 1, 'o': 2}
print(vowel_count('HOW ARE YOU? i am great!'))  # Output: {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}

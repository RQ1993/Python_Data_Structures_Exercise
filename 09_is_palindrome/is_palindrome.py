def is_palindrome(phrase):
    """Check if a phrase is a palindrome.

    Args:
        phrase (str): The input phrase to check.

    Returns:
        bool: True if the phrase is a palindrome, False otherwise.
    """
    # Remove spaces and convert the phrase to lowercase
    phrase = phrase.replace(" ", "").lower()
    
    # Check if the phrase is equal to its reverse
    return phrase == phrase[::-1]

# Test cases
print(is_palindrome('tacocat'))  # Output: True
print(is_palindrome('noon'))     # Output: True
print(is_palindrome('robert'))   # Output: False
print(is_palindrome('taco cat')) # Output: True
print(is_palindrome('Noon'))     # Output: True

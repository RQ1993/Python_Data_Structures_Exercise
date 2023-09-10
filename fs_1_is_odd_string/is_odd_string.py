def is_odd_string(word):
    # Initialize a variable to store the sum of character positions
    sum_of_positions = 0

    # Iterate through each character in the word
    for char in word:
        # Convert the character to lowercase and find its position
        char_position = ord(char.lower()) - ord('a') + 1
        sum_of_positions += char_position

    # Check if the sum of character positions is odd
    return sum_of_positions % 2 != 0

# Test cases
print(is_odd_string('a'))  # Output: True
print(is_odd_string('A'))  # Output: True
print(is_odd_string('aaaa'))  # Output: False
print(is_odd_string('AAaa'))  # Output: False
print(is_odd_string('amazing'))  # Output: True

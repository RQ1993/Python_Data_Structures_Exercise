def same_frequency(num1, num2):
    # Convert the numbers to strings to easily work with their digits
    str_num1 = str(num1)
    str_num2 = str(num2)
    
    # Check if the lengths of the two strings are different
    if len(str_num1) != len(str_num2):
        return False
    
    # Create dictionaries to store the frequency of each digit in both numbers
    freq1 = {}
    freq2 = {}
    
    # Count the frequency of each digit in num1
    for digit in str_num1:
        freq1[digit] = freq1.get(digit, 0) + 1
    
    # Count the frequency of each digit in num2
    for digit in str_num2:
        freq2[digit] = freq2.get(digit, 0) + 1
    
    # Compare the dictionaries to check if they have the same frequencies
    return freq1 == freq2

# Test cases
print(same_frequency(551122, 221515))   # True
print(same_frequency(321142, 3212215))  # False
print(same_frequency(1212, 2211))       # True

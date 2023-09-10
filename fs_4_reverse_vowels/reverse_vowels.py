def reverse_vowels(s):
    # Convert the string to a list to make it mutable
    s_list = list(s)
    
    # Define a set of vowels
    vowels = set("aeiouAEIOU")
    
    # Initialize pointers
    left, right = 0, len(s_list) - 1
    
    while left < right:
        # Move the left pointer to the right until it points to a vowel
        while left < right and s_list[left] not in vowels:
            left += 1
        
        # Move the right pointer to the left until it points to a vowel
        while left < right and s_list[right] not in vowels:
            right -= 1
        
        # Swap the vowels
        s_list[left], s_list[right] = s_list[right], s_list[left]
        
        # Move the pointers towards each other
        left += 1
        right -= 1

    # Convert the list back to a string
    return ''.join(s_list)

# Test cases
print(reverse_vowels("Hello!"))  # Output: 'Holle!'
print(reverse_vowels("Tomatoes"))  # Output: 'Temotaos'
print(reverse_vowels("Reverse Vowels In A String"))  # Output: 'RivArsI Vewols en e Streng'
print(reverse_vowels("aeiou"))  # Output: 'uoiea'
print(reverse_vowels("why try, shy fly?"))  # Output: 'why try, shy fly?'

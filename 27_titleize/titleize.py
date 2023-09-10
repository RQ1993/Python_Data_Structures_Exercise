def titleize(phrase):
    # Split the phrase into words
    words = phrase.split()
    
    # Capitalize the first letter of each word and join them back together
    titleized_words = [word.capitalize() for word in words]
    
    # Join the titleized words into a single string
    return ' '.join(titleized_words)

# Test cases
print(titleize('this is awesome'))  # Output: 'This Is Awesome'
print(titleize('oNLy cAPITALIZe fIRSt'))  # Output: 'Only Capitalize First'

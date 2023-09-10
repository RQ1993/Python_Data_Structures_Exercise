def truncate(phrase, n):
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    elif len(phrase) <= n:
        return phrase
    else:
        return phrase[:n - 3] + '...'

# Test cases
print(truncate("Hello World", 6))  # 'Hel...'
print(truncate("Problem solving is the best!", 10))  # 'Problem...'
print(truncate("Yo", 100))  # 'Yo'
print(truncate('Cool', 1))  # 'Truncation must be at least 3 characters.'
print(truncate("Woah", 4))  # 'W...'
print(truncate("Woah", 3))  # '...'

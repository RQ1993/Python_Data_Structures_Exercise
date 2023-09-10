def repeat(phrase, num):
    if not isinstance(num, int) or num < 0:
        return None
    else:
        return phrase * num

# Test cases
print(repeat('*', 3))  # '***'
print(repeat('abc', 2))  # 'abcabc'
print(repeat('abc', 0))  # ''
print(repeat('abc', -1) is None)  # True
print(repeat('abc', 'nope') is None)  # True

def min_max_keys(d):
    # Use the min and max functions to find the minimum and maximum keys
    min_key = min(d.keys())
    max_key = max(d.keys())
    
    # Return a tuple containing the minimum and maximum keys
    return (min_key, max_key)

# Test cases
d1 = {2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}
print(min_max_keys(d1))  # Output: (1, 10)

d2 = {"apple": "red", "cherry": "red", "berry": "blue"}
print(min_max_keys(d2))  # Output: ('apple', 'cherry')

def two_list_dictionary(keys, values):
    # Create an empty dictionary to store the result
    result = {}
    
    # Iterate over the keys and values simultaneously using zip
    for key, value in zip(keys, values):
        result[key] = value
    
    # If there are more keys than values, fill the remaining keys with None
    if len(keys) > len(values):
        remaining_keys = keys[len(values):]
        for key in remaining_keys:
            result[key] = None
    
    return result

# Test cases
print(two_list_dictionary(['x', 'y', 'z'], [9, 8, 7]))  # {'x': 9, 'y': 8, 'z': 7}
print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))  # {'a': 1, 'b': 2, 'c': 3, 'd': None}
print(two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]))  # {'a': 1, 'b': 2, 'c': 3}
def two_list_dictionary(keys, values):
    # Create an empty dictionary to store the result
    result = {}
    
    # Iterate over the keys and values simultaneously using zip
    for key, value in zip(keys, values):
        result[key] = value
    
    # If there are more keys than values, fill the remaining keys with None
    if len(keys) > len(values):
        remaining_keys = keys[len(values):]
        for key in remaining_keys:
            result[key] = None
    
    return result

# Test cases
print(two_list_dictionary(['x', 'y', 'z'], [9, 8, 7]))  # {'x': 9, 'y': 8, 'z': 7}
print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))  # {'a': 1, 'b': 2, 'c': 3, 'd': None}
print(two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]))  # {'a': 1, 'b': 2, 'c': 3}

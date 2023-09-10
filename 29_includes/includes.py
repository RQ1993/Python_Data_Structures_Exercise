def includes(collection, sought, start=None):
    if isinstance(collection, (list, str, tuple)):
        if start is None:
            start = 0
        if sought in collection[start:]:
            return True
    elif isinstance(collection, set):
        return sought in collection
    elif isinstance(collection, dict):
        return sought in collection.values()
    
    return False

# Test cases
print(includes([1, 2, 3], 1))  # True
print(includes([1, 2, 3], 1, 2))  # False
print(includes("hello", "o"))  # True
print(includes(('Elmo', 5, 'red'), 'red', 1))  # True
print(includes({1, 2, 3}, 1))  # True
print(includes({1, 2, 3}, 1, 3))  # True (start ignored for sets)
print(includes({"apple": "red", "berry": "blue"}, "blue"))  # True

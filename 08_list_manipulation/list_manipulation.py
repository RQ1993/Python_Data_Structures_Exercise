def list_manipulation(lst, command, location, value=None):
    """Manipulate a list by adding or removing elements at the specified location.

    Args:
        lst (list): The input list.
        command (str): The command, either "remove" or "add".
        location (str): The location to remove/add, either "beginning" or "end".
        value: When adding, the value to add.

    Returns:
        - If the command is "remove":
            - If location is "beginning", remove and return the item at the beginning.
            - If location is "end", remove and return the item at the end.
        - If the command is "add":
            - If location is "beginning", add the value to the beginning and return the updated list.
            - If location is "end", add the value to the end and return the updated list.
        - If the command or location is invalid, return None.
    """
    if command == "remove":
        if location == "beginning":
            if lst:
                return lst.pop(0)  # Remove and return the first item
        elif location == "end":
            if lst:
                return lst.pop()  # Remove and return the last item
    elif command == "add":
        if location == "beginning":
            lst.insert(0, value)  # Add value to the beginning
            return lst
        elif location == "end":
            lst.append(value)  # Add value to the end
            return lst
    return None  # Invalid command or location

# Test cases
lst = [1, 2, 3]

print(list_manipulation(lst, 'remove', 'end'))  # Output: 3
print(list_manipulation(lst, 'remove', 'beginning'))  # Output: 1
print(lst)  # Output: [2]

print(list_manipulation(lst, 'add', 'beginning', 20))  # Output: [20, 2]
print(list_manipulation(lst, 'add', 'end', 30))  # Output: [20, 2, 30]
print(lst)  # Output: [20, 2, 30]

print(list_manipulation(lst, 'foo', 'end'))  # Output: None
print(list_manipulation(lst, 'add', 'dunno'))  # Output: None

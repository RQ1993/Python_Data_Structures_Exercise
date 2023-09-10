def valid_parentheses(parens):
    # Initialize an empty stack to keep track of opening parentheses
    stack = []

    # Define a dictionary to map closing parentheses to their corresponding opening parentheses
    parentheses_map = {')': '(', '}': '{', ']': '['}

    # Iterate through each character in the input string
    for char in parens:
        # If the character is an opening parenthesis, push it onto the stack
        if char in '({[':
            stack.append(char)
        # If the character is a closing parenthesis
        elif char in ')}]':
            # Check if the stack is empty or if the top of the stack does not match the corresponding opening parenthesis
            if not stack or stack.pop() != parentheses_map[char]:
                return False

    # After iterating through the string, the stack should be empty if parentheses are balanced
    return not stack

# Test cases
print(valid_parentheses("()"))  # Output: True
print(valid_parentheses("()()"))  # Output: True
print(valid_parentheses("(()())"))  # Output: True
print(valid_parentheses(")()"))  # Output: False
print(valid_parentheses("())"))  # Output: False
print(valid_parentheses("((())"))  # Output: False
print(valid_parentheses(")()("))  # Output: False

def partition(lst, fn):
    """Partition lst by a predicate function.

    Args:
        lst (list): The input list of items.
        fn (function): A predicate function that returns True or False.

    Returns:
        list: A new list containing two sublists: [a, b], where `a` contains items that passed the fn test,
              and `b` contains items that failed the fn test.
    """
    a = [item for item in lst if fn(item)]
    b = [item for item in lst if not fn(item)]
    return [a, b]

# Test cases
def is_even(num):
    return num % 2 == 0

def is_string(el):
    return isinstance(el, str)

print(partition([1, 2, 3, 4], is_even))              # Output: [[2, 4], [1, 3]]
print(partition(["hi", None, 6, "bye"], is_string))  # Output: [['hi', 'bye'], [None, 6]]

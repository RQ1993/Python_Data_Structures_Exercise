def find_the_duplicate(nums):
    # Create an empty set to store unique numbers
    unique_nums = set()
    
    # Iterate through the numbers in the list
    for num in nums:
        # If the number is already in the set, it's a duplicate
        if num in unique_nums:
            return num
        # Otherwise, add it to the set
        else:
            unique_nums.add(num)
    
    # If no duplicate is found, return None
    return None

# Test cases
print(find_the_duplicate([1, 2, 1, 4, 3, 12]))     # 1
print(find_the_duplicate([6, 1, 9, 5, 3, 4, 9]))  # 9
print(find_the_duplicate([2, 1, 3, 4]))          # None

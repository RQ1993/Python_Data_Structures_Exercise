def three_odd_numbers(nums):
    # Check if the list has at least 3 numbers
    if len(nums) < 3:
        return False

    # Iterate through the list up to the third-to-last element
    for i in range(len(nums) - 2):
        # Get three consecutive numbers
        num1, num2, num3 = nums[i], nums[i + 1], nums[i + 2]

        # Check if the sum of these three numbers is odd
        if (num1 + num2 + num3) % 2 == 1:
            return True

    # If no such three consecutive numbers are found, return False
    return False

# Test cases
print(three_odd_numbers([1, 2, 3, 4, 5]))  # Output: True
print(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]))  # Output: True
print(three_odd_numbers([5, 2, 1]))  # Output: False
print(three_odd_numbers([1, 2, 3, 3, 2]))  # Output: False

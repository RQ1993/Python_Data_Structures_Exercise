def sum_range(nums, start=0, end=None):
    # If end is not provided, set it to the end of the list
    if end is None:
        end = len(nums)
    
    # Ensure start and end are within valid bounds
    start = max(0, start)
    end = min(end, len(nums))
    
    # Calculate the sum of numbers in the specified range
    total = sum(nums[start:end])
    
    return total

# Test cases
nums = [1, 2, 3, 4]
print(sum_range(nums))           # 10
print(sum_range(nums, 1))        # 9
print(sum_range(nums, end=2))    # 6
print(sum_range(nums, 1, 3))     # 9
print(sum_range(nums, 1, 99))    # 9 (end beyond the list length is handled)

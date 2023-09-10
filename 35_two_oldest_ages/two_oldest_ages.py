def two_oldest_ages(ages):
    # Remove duplicates and sort the ages in descending order
    unique_sorted_ages = sorted(set(ages), reverse=True)
    
    # Check if there are at least two distinct ages
    if len(unique_sorted_ages) >= 2:
        # Return a tuple of the second-oldest and oldest ages
        return (unique_sorted_ages[1], unique_sorted_ages[0])
    else:
        # If there are not enough distinct ages, return None
        return None

# Test cases
print(two_oldest_ages([1, 2, 10, 8]))           # (8, 10)
print(two_oldest_ages([6, 1, 9, 10, 4]))        # (9, 10)
print(two_oldest_ages([1, 5, 5, 2]))            # (2, 5)

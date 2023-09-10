def weekday_name(day_of_week):
    """Return the name of the weekday based on its numerical representation.
    
    Args:
        day_of_week (int): An integer representing the day of the week (1 for Sunday, 2 for Monday, ..., 7 for Saturday).

    Returns:
        str: The name of the weekday (e.g., 'Sunday', 'Monday', etc.). Returns None for invalid inputs.
    """
    # Define a list of weekday names
    weekdays = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
    ]

    # Check if the input is within the valid range (1 to 7)
    if 1 <= day_of_week <= 7:
        return weekdays[day_of_week - 1]  # Adjust index by subtracting 1
    else:
        return None

# Test cases
print(weekday_name(1))  # Output: 'Sunday'
print(weekday_name(7))  # Output: 'Saturday'
print(weekday_name(9))  # Output: None
print(weekday_name(0))  # Output: None
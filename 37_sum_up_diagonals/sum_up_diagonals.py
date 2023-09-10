def sum_up_diagonals(matrix):
    # Initialize variables to store the sums of both diagonals
    diagonal1_sum = 0  # Top-left to bottom-right diagonal
    diagonal2_sum = 0  # Bottom-left to top-right diagonal
    
    # Get the size of the square matrix (number of rows or columns)
    size = len(matrix)
    
    # Iterate through the rows of the matrix
    for i in range(size):
        # Add the value from the top-left to bottom-right diagonal
        diagonal1_sum += matrix[i][i]
        
        # Add the value from the bottom-left to top-right diagonal
        diagonal2_sum += matrix[i][size - 1 - i]
    
    # Return the sum of both diagonals
    return diagonal1_sum + diagonal2_sum

# Test cases
m1 = [
    [1, 2],
    [30, 40],
]
print(sum_up_diagonals(m1))  # Output: 73

m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(sum_up_diagonals(m2))  # Output: 30

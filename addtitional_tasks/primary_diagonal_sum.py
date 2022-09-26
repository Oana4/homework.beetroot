# Write a Python program to read a square matrix from console and print the sum of matrix primary diagonal.
# Accept the size of the square matrix and elements separated with a
# space (for every row) as input from the user.

sum_of_primary_diagonal = 0

size_of_matrix = int(input("Please choose the size for your matrix: "))

matrix = [[0] * size_of_matrix for row in range(size_of_matrix)]

# input matrix
for i in range(size_of_matrix):

    row_input = list(map(int, input(f"Please choose your elements for row number {i}, separated with space: ").split()))

    for j in range(size_of_matrix):
        matrix[i][j] = row_input[j]

# determine the sum of primary diagonal
for i in range(size_of_matrix):
    for j in range(size_of_matrix):
        if i == j:
            sum_of_primary_diagonal += matrix[i][j]

print("Sum of primary diagonal is: ", sum_of_primary_diagonal)
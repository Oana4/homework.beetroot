# Write a program that takes an integer from user input,
# stores it in variable n and prints an n-by-n table
# such that there is an * in row i and column j if the greatest common divisor of i and j is 1
# (i and j are relatively prime) and a space character in that position otherwise.

import numpy as np

n = int(input("Please choose an integer: "))


def relatively_prime(a, b):
    common_divisor = 1

    for x in range(1, a + 1):
        if a % x == 0 and b % x == 0:
            common_divisor = x

    return common_divisor == 1


table = np.empty((n, n), dtype=str)

for i in range(n):
    for j in range(n):
        if relatively_prime(i+1, j+1):
            table[i][j] = '*'
        else:
            table[i][j] = ' '
print(table)

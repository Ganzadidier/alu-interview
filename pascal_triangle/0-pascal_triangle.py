#!/usr/bin/python3
"""Check readme for full description"""


def pascal_triangle(n):
    """ returns a list of lists of integers(Pascals triangle of n)"""

    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row as [1]

    for i in range(1, n):
        row = [1]  # Each row starts with 1
        for j in range(1, i):
            # Each element is the sum of two elements from the previous row
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Each row ends with 1
        triangle.append(row)

    return triangle

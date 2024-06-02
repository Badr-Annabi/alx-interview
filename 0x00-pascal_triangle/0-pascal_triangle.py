#!/usr/bin/python3
""" This Function returns a list of lists of integers representing
    the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """Displays Pascal's Triangle """
    if n <= 0:
        return
    triangle = []
    current_row = [1]
    for i in range(n):
        triangle.append(current_row)
        next_row = [1]
        for j in range(1, len(current_row)):
            next_row.append(current_row[j-1] + current_row[j])
        next_row.append(1)
        current_row = next_row
    return triangle

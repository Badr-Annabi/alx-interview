#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """this function returns the perimeter of the island grid"""
    prim = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == 1:
                prim += 4
                if i > 0 and grid[i - 1][j] == 1:
                    prim -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    prim -= 2
    return prim

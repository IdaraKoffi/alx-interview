#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of ints): A 2D grid representing the island

    Returns:
        int: The perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Assume 4 sides for each land cell
                perimeter += 4

                # Subtract 2 for each adjacent land cell
                # (to avoid double counting)
                if i > 0 and grid[i - 1][j] == 1:  # Check top
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Check left
                    perimeter -= 2

    return perimeter
#!/usr/bin/python3
"""
Test script for 0x07 - Rotate 2D Matrix
"""

rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original matrix:")
    for row in matrix:
        print(row)

    rotate_2d_matrix(matrix)

    print("\nRotated matrix:")
    for row in matrix:
        print(row)

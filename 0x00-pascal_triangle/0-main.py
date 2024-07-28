#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
    print_triangle(pascal_triangle(0))  # Should return an empty list
    print_triangle(pascal_triangle(1))  # Should return [[1]]
    print_triangle(pascal_triangle(3))  # Should return [[1], [1, 1], [1, 2, 1]]


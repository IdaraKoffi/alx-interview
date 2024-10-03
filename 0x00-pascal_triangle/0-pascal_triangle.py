def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's Triangle of n.
    
    :param n: number of rows in Pascal's Triangle
    :return: a list of lists of integers representing Pascal's Triangle
    """
    if n <= 0:
        return []
    
    # Initialize Pascal's triangle with the first row
    triangle = []
    
    for i in range(n):
        # Start each row with 1
        row = [1] * (i + 1)
        
        # Calculate the inner values of the row (if i > 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle


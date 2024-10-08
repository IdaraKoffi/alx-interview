# Pascal's Triangle

## Project Overview

This project implements a function that generates Pascal's Triangle. Pascal's Triangle is a triangular array of the binomial coefficients. Each number is the sum of the two numbers directly above it in the previous row. The triangle starts with a single `1` at the top, and each row corresponds to the coefficients of the binomial expansion.

## Requirements

To successfully complete this project, you should have a basic understanding of the following Python concepts:

- Lists and List Comprehensions
- Functions
- Loops (for and while)
- Conditional Statements (if, elif, else)
- (Optional) Recursion
- Arithmetic Operations
- Indexing and Slicing
- Memory Management
- (Optional) Error and Exception Handling
- Efficiency and Optimization

## Implementation

### Function

```python
def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of size n.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    List[List[int]]: A list of lists representing the triangle.
    """


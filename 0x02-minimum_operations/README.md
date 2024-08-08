# 0x02. Minimum Operations

## Description

This project is about solving the problem of finding the minimum number of operations needed to get exactly `n` characters `H` in a file, starting with just one character `H`. The only operations you can perform are:

- `Copy All`: This operation copies all the characters in the file.
- `Paste`: This operation pastes the last copied characters.

The task is to determine the fewest number of operations required to achieve exactly `n` characters.

## Concepts Used

The solution to this problem involves understanding the following concepts:

- **Prime Factorization:** The problem can be reduced to finding the sum of the prime factors of the target number `n`.
- **Greedy Algorithms:** The problem can be approached with a greedy algorithm, choosing the best option at each step.
- **Optimization:** Finding the most efficient solution requires minimizing the number of operations.

## Files

- `0-minoperations.py`: Contains the function `minOperations(n)` that calculates the minimum number of operations needed to reach `n` characters.
- `0-main.py`: This is a test file used to validate the function with various inputs.

## Function Prototype

```python
def minOperations(n)


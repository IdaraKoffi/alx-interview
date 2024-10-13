markdown
Copy code
# Lockboxes

This project involves determining if a series of locked boxes can all be opened given a specific set of keys. The problem is solved using a depth-first search (DFS) approach to traverse through the keys and boxes, allowing you to see if all boxes can be unlocked from the first box.

## Project Requirements

- All code files will be interpreted on Ubuntu 20.04 LTS using Python 3.
- PEP 8 style guidelines must be followed.
- A `README.md` file is mandatory in the root folder.
- All Python files must be executable.

## Problem Description

You are given `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and may contain keys to other boxes. The task is to write a method that determines if all the boxes can be opened.

### Function Prototype

```python
def canUnlockAll(boxes)
Input: boxes is a list of lists, where each list represents a box containing keys to other boxes.
Output: The function should return True if all boxes can be opened, else False.
Constraints
Box 0 is always unlocked.
A key with the same number as a box unlocks that box.
All keys are positive integers.
There can be keys without corresponding boxes.
Example
python
Copy code
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Expected output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Expected output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Expected output: False
Approach
The solution uses a depth-first search (DFS) to explore which boxes can be opened:

Use a stack to keep track of which boxes are accessible.
Start by adding box 0 to a opened_boxes set since it is unlocked by default.
For each box, add any new keys found to the stack if they correspond to boxes that haven't been opened.
After exploring all keys and boxes, check if the number of opened boxes equals the total number of boxes. If so, return True; otherwise, return False.
Installation and Usage
Clone the repository:

bash
Copy code
git clone <repository-url>
cd 0x01-lockboxes
Make sure your Python file is executable:

bash
Copy code
chmod +x 0-lockboxes.py
Run the test script:

bash
Copy code
./main_0.py
Project Files
0-lockboxes.py: Contains the canUnlockAll function implementation.
main_0.py: A test file with sample test cases to verify the solution.
README.md: Project description and usage instructions.
Additional Information
This project requires a good understanding of Python lists, sets, and recursion/iteration. Familiarity with DFS or BFS is helpful, as the problem can be visualized as graph traversal. For more information, you can refer to the following topics:

Lists and List Manipulation in Python
Graph Theory Basics
Algorithmic Complexity
Python Sets
Recursion and Iteration
Author
This project is part of the ALX Interview Preparation series.

#!/usr/bin/python3
def canUnlockAll(boxes):
    # Number of boxes
    n = len(boxes)
    # Set to track opened boxes
    opened_boxes = set([0])
    # Stack for DFS traversal
    stack = [0]
    # Traverse until no more boxes can be opened
    while stack:
        current_box = stack.pop()
        # Get the keys inside the current box
        for key in boxes[current_box]:
            # Check if the box corresponding to the key hasn't been opened
            if key < n and key not in opened_boxes:
                opened_boxes.add(key)
                stack.append(key)

    # If the number of opened boxes equals the number of boxes, return True
    return len(opened_boxes) == n

#!/usr/bin/python3
def canUnlockAll(boxes):
    """Determine if all the boxes can be opened."""
    if not boxes:
        return False

    # Initialize the set of opened boxes and the stack with the first box
    opened_boxes = set([0])
    stack = [0]

    while stack:
        # Get the current box index
        current_box = stack.pop()
        # Iterate through all keys in the current box
        for key in boxes[current_box]:
            # If the key is a valid box number and it's not yet opened
            if key < len(boxes) and key not in opened_boxes:
                opened_boxes.add(key)
                stack.append(key)
    
    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)


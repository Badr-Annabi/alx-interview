#!/usr/binenv python3


"""This function determines if all the boxes can be opened."""
def canUnlockAll(boxes):
    n = len(boxes)
    visited = set()
    queue = [0]

    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.add(current)
            for key in boxes[current]:
                if key < n:
                    queue.append(key)
    return len(visited) == n
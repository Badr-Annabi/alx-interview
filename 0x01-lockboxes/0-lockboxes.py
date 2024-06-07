#!/usr/bin/python3
"""This function determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """
     a method that determines if all the boxes can be opened.

    :param boxes:
    :return: True or False
    """
    if not boxes or type(
        boxes) is not list or not all(
            isinstance(box, list) for box in boxes):
        return False
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
    if len(visited) == n:
        return True
    return False

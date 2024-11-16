"""Practice  with linked list data structure."""

from __future__ import annotations

__author__ = "730622230"


class Node:
    """Defining the Node class."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializing the Node class."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """String representation of the Node class."""
        rest: str = "TODO"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Find the value of the Node at given index."""
    idx: int = index
    if head is None:  # Out of range if reached the end but still has index left
        raise IndexError("Index is out of bounds on the list.")
    elif idx == 0:  # Base case
        return head.value
    else:
        idx -= 1
        return value_at(head.next, idx)  # Recursive case


def max(head: Node | None) -> int:
    """Find the max value of the Node."""
    if head is None:
        raise ValueError("Cannot call max with None")
    elif head.next is None:  # Base case
        return head.value
    else:
        if head.value < max(head.next):  # Recursive case
            return max(head.next)
        else:
            return head.value


def linkify(items: list[int]) -> Node | None:
    """Create a Linked List of Nodes."""
    if len(items) == 0:  # Base case
        return None
    else:
        nd: Node = Node(items[0], linkify(items[1:]))  # Recursive case
        return nd


def scale(head: Node | None, factor: int) -> Node | None:
    """Multiply each value in the Node by the factor."""
    if head is None:  # Base case
        return None
    else:
        nd: Node = Node(head.value * factor, scale(head.next, factor))
        return nd  # Recursive case

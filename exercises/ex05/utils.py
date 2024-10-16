"""EX05 - Reverse engineering list utility functions Part 2"""

__author__ = "730622230"


def only_evens(list_1: list[int]) -> list[int]:
    even_list: list[int] = []  # Empty list as the default return
    for elem in list_1:
        if elem % 2 == 0:
            even_list.append(elem)
    return even_list


def sub(list_2: list[int], start_index: int, end_index: int) -> list[int]:
    if (
        len(list_2) == 0 or start_index >= len(list_2) or end_index <= 0
    ):  # Dealing with edge cases first
        return []
    sublist: list[int] = []
    true_start: int = start_index
    true_end: int = end_index
    if (
        start_index < 0
    ):  # Alter the actual start index when inputs are out of range, similar for end_index
        true_start = 0
    if end_index > len(list_2):
        true_end = len(list_2)
    for idx in range(
        true_start, true_end
    ):  # range does not include the end point so no need to -1
        sublist.append(list_2[idx])
    return sublist


def add_at_index(list_3: list[int], elem_add: int, index_add: int) -> None:
    if index_add < 0 or index_add > len(list_3):
        raise IndexError("Index is out of bounds for the input list")
    list_3.append(0)  # Add an extra space at the end for moving elements to the right
    idx: int = (
        len(list_3) - 1
    )  # The index of the place we want the old element to move to
    while idx > index_add:  # Stop at the element right after the insertion
        list_3[idx] = list_3[idx - 1]
        idx -= 1  # We move backwards otherwise the old element at the insertion index would overwrite everything behind
    list_3[index_add] = elem_add

"""EX04 - Reverse engineering list utility functions"""

__author__ = "730622230"


def all(list_1: list[int], int_1: int) -> bool:
    idx: int = 0
    if list_1 == []:
        return False  # Eliminating the case when the list is empty
    while idx < len(list_1):
        if list_1[idx] == int_1:
            idx += 1  # Only advance to the next element if the current element = int_1
        else:
            return False  # Short circuit the loop whenever discrepancy appears
    return True  # Return True if all elements = int_1


def max(list_2: list[int]) -> int:
    if len(list_2) == 0:
        raise ValueError("max() arg is an empty List")
    mxm: int = list_2[0]  # Initialize the maximum as the first element
    idx: int = 0
    while idx < len(list_2):
        if list_2[idx] > mxm:
            mxm = list_2[idx]  # If the current element > mxm, it becomes the new mxm
        idx += 1
    return mxm


def is_equal(list_3: list[int], list_4: list[int]) -> bool:
    if len(list_3) == len(list_4):  # Only proceed if lengths are equal
        idx: int = 0
        while idx < len(list_3):
            if list_3[idx] == list_4[idx]:
                idx += 1
            else:
                return False
        return True  # This while loop is similar to the one in all
    else:
        return False  # If lengths are not equal in the first place, then False clearly


def extend(list_5: list[int], list_6: list[int]) -> None:
    idx: int = 0
    while idx < len(list_6):
        list_5.append(list_6[idx])
        idx += 1

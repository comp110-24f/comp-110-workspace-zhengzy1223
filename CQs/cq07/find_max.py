"""Practice with list modification"""

__author__ = "730622230"


def find_and_remove_max(list_1: list[int]) -> int:
    if len(list_1) == 0:
        return -1
    max: int = list_1[0]
    for elem in list_1:
        if elem >= max:
            max = elem
    idx: int = 0
    while idx < len(list_1):
        if list_1[idx] == max:
            list_1.pop(idx)
        else:
            idx += 1
    return max

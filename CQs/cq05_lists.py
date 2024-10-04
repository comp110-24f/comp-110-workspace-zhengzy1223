"""Mutating functions."""

__author__ = "730622230"


def manual_append(list: list[int], appendix: int) -> None:
    list.append(appendix)


def double(single: list[int]) -> None:
    idx: int = 0
    while idx < len(single):
        single[idx] = single[idx] * 2
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)

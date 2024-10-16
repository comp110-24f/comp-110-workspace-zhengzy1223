"""Practice with unit tests"""

__author__ = "730622230"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_max_return() -> None:
    """Testing find_and_remove_max returns the max number in a list"""
    assert find_and_remove_max([2, 4, 5, 5, 4]) == 5


def test_find_and_remove_max_list_mutation() -> None:
    """Testing find_and_remove_max mutates the list correctly"""
    list_a: list[int] = [2, 4, 5, 5, 4]
    find_and_remove_max(list_a)
    assert list_a == [2, 4, 4]


def test_find_and_remove_max_edge_case() -> None:
    """Testing find_and_remove_max returns the correct value on an empty list"""
    assert find_and_remove_max([]) == -1

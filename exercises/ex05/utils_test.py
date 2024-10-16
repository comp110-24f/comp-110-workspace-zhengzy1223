"""EX05 - Reverse engineering list utility functions Part 2_Unit Test"""

__author__ = "730622230"

from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_edge_case() -> None:
    """Testing only_evens on empty list"""
    assert only_evens([]) == []


def test_only_evens_use_case() -> None:
    """Testing only_evens returns only the even elements"""
    assert only_evens([2, 4, 5, 6]) == [2, 4, 6]


def test_only_evens_list_mutation() -> None:
    """Testing only_evens does not mutate the original list"""
    list_a: list[int] = [2, 4, 5, 6]
    only_evens(list_a)
    assert list_a == [2, 4, 5, 6]


def test_sub_edge_case() -> None:
    """Testing sub on empty list"""
    assert sub([], 1, 3) == []


def test_sub_use_case() -> None:
    """Testing sub returns a sublist between the start index and the end index - 1"""
    assert sub([2, 4, 5, 6], 0, 3) == [2, 4, 5]


def test_sub_list_mutation() -> None:
    """Testing sub does not mutate the original list"""
    list_a: list[int] = [2, 4, 5, 6]
    sub([2, 4, 5, 6], 0, 3)
    assert list_a == [2, 4, 5, 6]


import pytest


def test_add_at_index_raises_index_error() -> None:
    """Testing add_at_index raises an IndexError for an invalid index."""
    with pytest.raises(IndexError):
        add_at_index([2, 4, 5, 6], 9, 5)


def test_add_at_index_use_case() -> None:
    """Testing add_at_index adds the element at the desired index"""
    list_a: list[int] = [2, 4, 5, 6]
    add_at_index(list_a, 9, 4)
    assert list_a == [2, 4, 5, 6, 9]


def test_add_at_index_return() -> None:
    """Testing add_at_index returns None"""
    assert add_at_index([2, 4, 5, 6], 9, 4) == None

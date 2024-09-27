"""CQ03 Practice with While Loop"""

__author__ = "730622230"


def num_instances(phrase: str, search_char: str) -> int:
    i: int = 0
    count: int = 0
    while i < len(phrase):
        if phrase[i] == search_char:
            count = count + 1
        i = i + 1
    return count

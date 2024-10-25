"""EX06 - Reverse engineering dictionary utility functions"""

__author__ = "730622230"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    idict1: dict[str, str] = {}  # Initializing an empty dictionary
    for key in dict1:
        if dict1[key] in idict1:  # If the value at the current key has occured before
            raise KeyError("More than one same key!")
        else:
            idict1[dict1[key]] = key  # Inversion
    return idict1


def favorite_color(dict2: dict[str, str]) -> str:
    color_count: dict[str, int] = (
        dict()
    )  # A new dictionary for counting the number of occurence for each color
    for key in dict2:  # Similar to the implementation strategy for count
        if key in color_count:
            color_count[dict2[key]] += 1
        else:
            color_count[dict2[key]] = 1
    count: int = 0
    popco: str = ""
    for key in color_count:
        if (
            color_count[key] > count
        ):  # No equal here since the color that occurs first should be displayed when tie happens
            count = color_count[key]
            popco = key
    return popco


def count(list1: list[str]) -> dict[str, int]:
    list_count: dict[str, int] = dict()
    for elem in list1:
        if elem in list_count:
            list_count[elem] += 1
        else:
            list_count[elem] = 1
    return list_count


def alphabetizer(list2: list[str]) -> dict[str, list[str]]:
    alpha_count: dict[str, list[str]] = dict()
    for (
        elem
    ) in (
        list2
    ):  # Essentially the same logic as in the previous two functions: if occurs before add one to the current entry if not add a new entry
        if elem[0].lower() in alpha_count:
            alpha_count[elem[0].lower()].append(elem)
        else:
            alpha_count[elem[0].lower()] = [elem]
    return alpha_count


def update_attendance(dict3: dict[str, list[str]], day: str, name: str) -> None:
    if day in dict3:
        for elem in dict3[day]:
            if (
                elem != name
            ):  # No need to update if the new attendance has been recorded already
                dict3[day].append(name)
    else:
        dict3[day] = [name]

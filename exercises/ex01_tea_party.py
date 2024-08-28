"""Calculating the required resources for a tea party"""

__author__ = "730622230"


def main_planner(guests: int) -> None:
    """Coordinates all the functions"""
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # Convert the number output to strings and add spaces when needed
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  # The function "cost" contains two parameters, tea_count is the same as the output of tea_bags and treat_count is the same as that of treats


def tea_bags(people: int) -> int:
    """The number of tea bags required"""
    return 2 * people


def treats(people: int) -> int:
    """The number of treats required"""
    return int(
        1.5 * tea_bags(people=people)
    )  # Make a function call for tea_bags and use keyword argument for its parameter "people"


def cost(tea_count: int, treat_count: int) -> float:
    """The cost of tea bags and treats combined"""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

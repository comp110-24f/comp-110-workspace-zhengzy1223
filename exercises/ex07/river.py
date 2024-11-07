"""File to define River class."""

__author__ = "730622230"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Properties of River."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove bears and fish that are old."""
        newf_list: list[Fish] = list()
        newb_list: list[Bear] = list()
        for _ in range(0, len(self.fish)):
            if self.fish[_].age <= 3:
                newf_list.append(
                    self.fish[_]
                )  # Add only fish younger than 3 yrs old to the new list
        for _ in range(0, len(self.bears)):
            if self.bears[_].age <= 5:
                newb_list.append(self.bears[_])
        self.fish = newf_list
        self.bears = newb_list
        return None

    def remove_fish(self, amount: int):
        """Remove fish that are due to bears eating."""
        for _ in range(0, amount):
            self.fish.pop(0)
        return None

    def bears_eating(self):
        """Implement one cycle of bear eating."""
        for _ in range(0, len(self.bears)):
            if len(self.fish) >= 5:
                self.remove_fish(3)
                self.bears[_].eat(3)  # Every bear eats three fish
        return None

    def check_hunger(self):
        """Remove bears that starve."""
        newb_list: list[Bear] = list()
        for _ in range(0, len(self.bears)):
            if self.bears[_].hunger_score >= 0:
                newb_list.append(self.bears[_])
        self.bears = newb_list
        return None

    def repopulate_fish(self):
        """Fish regenerates."""
        for _ in range(
            0, (len(self.fish) // 2) * 4
        ):  # Using the floor division to get the number of new fish
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Bears regenerate."""
        for _ in range(
            0, len(self.bears) // 2
        ):  # Using the floor division to get the number of new bears
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Output the current population status."""
        print(
            f"~~~ Day {self.day}: ~~~\nFish population: {len(self.fish)}\nBear population: {len(self.bears)}"
        )  # Using f-srting and escape sequence
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river."""
        for _ in range(0, 7):
            self.one_river_day()  # Call one_river_day seven times

"""File to define Bear class."""


class Bear:
    """Properties of Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Newborn bear that has 0 hunger_score."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Bears get one day older and one score hungrier."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Bears eat num_fish Fish."""
        self.hunger_score += num_fish
        return None

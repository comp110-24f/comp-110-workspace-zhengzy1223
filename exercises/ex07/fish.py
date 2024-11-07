"""File to define Fish class."""


class Fish:
    """Properties of Fish."""

    age: int

    def __init__(self):
        """Newborn fish."""
        self.age = 0
        return None

    def one_day(self):
        """Fish gets one day older."""
        self.age += 1
        return None

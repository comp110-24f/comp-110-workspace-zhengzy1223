"""CQ04 Practice with import"""

__author__ = "730622230"


def get_coords(xs: str, ys: str) -> None:
    idxx: int = 0
    idxy: int = 0
    while idxx < len(xs):
        while idxy < len(ys):
            print(f"({xs[idxx]},{ys[idxy]})")
            idxy += 1
        idxx += 1
        idxy = 0  # Resetting idxy in preparation for another round of the inner loop

"""CQ00 Writing Functions"""

__author__ = "730622230"


def mimic(message: str) -> str:
    """Returns the input"""
    return message


def main() -> None:
    """Pulls together functions into a main function"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()

"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730622230"


def input_word() -> str:
    user_word: str = input(
        "Enter a 5-character word: "
    )  # A str local variable to store user input of the word
    if len(user_word) != 5:  # Checking the length of the word
        print("Error: Word must contain 5 characters.")
        exit()  # exit() should come after the error message, and everything after will not be reached
    else:
        return user_word


def input_letter() -> str:
    user_letter: str = input("Enter a single character: ")
    if len(user_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        return user_letter


def contains_char(word: str, letter: str) -> None:
    count: int = (
        0  # The initial value of count should start with 0 since if word has no letters, its instances in the word should be 0
    )
    print(
        "Searching for " + letter + " in " + word
    )  # Note this searching message comes before others
    if letter == word[0]:
        print(letter + " found at index 0")
        count = count + 1  # Increasing count by 1 every time the letter appears
    if letter == word[1]:
        print(letter + " found at index 1")
        count = count + 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count = count + 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count = count + 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print(
            str(count) + " instance of " + letter + " found in " + word
        )  # instance is singular when count = 1
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()

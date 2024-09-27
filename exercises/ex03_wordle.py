"""EX03 - Wordle"""

__author__ = "730622230"


def input_guess(secret_word_len: int) -> str:
    user_input: str = input(
        f"Enter a {secret_word_len} character word: "
    )  # Use f-string to generate the prompt
    while len(user_input) != secret_word_len:
        user_input = input(
            f"That wasn't {secret_word_len} chars! Try again: "
        )  # Require additional input if input length does not satisfy
    return user_input


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Searching for the existence of char_guess in secret_word"""
    assert len(char_guess) == 1
    idx: int = 0
    while idx < len(secret_word):
        if secret_word[idx] == char_guess:
            return True  # Return True once occurence appears
        else:
            idx += 1
    return False  # Since the return statement quit the function body, we can place the False return here


def emojified(guess: str, secret: str) -> str:
    """Comparing the characters in two words and determining if they are in the same position"""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idxg: int = 0
    emo: str = ""  # Initialize the output emoji
    while idxg < len(guess):  # Go over every character of guess
        if contains_char(
            secret_word=secret, char_guess=guess[idxg]
        ):  # Check if character at idxg of guess is contained in secret (not considering position for now)
            if secret[idxg] == guess[idxg]:
                emo = emo + GREEN_BOX
            else:
                emo = (
                    emo + YELLOW_BOX
                )  # Only use GREEN-BOX if the character at idxg of guess both occurs in secret and is in the same position in secret
        else:
            emo = emo + WHITE_BOX
        idxg += 1
    return emo


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        input: str = input_guess(secret_word_len=len(secret))  # Record the user input
        print(emojified(guess=input, secret=secret))
        if input == secret:
            print(f"You won in {turn}/6 turns!")
            turn = 8  # We do not want to enter another round if user wins, so set turn > 6 exits the while loop (also !=7)
        else:
            turn += 1
    if turn == 7:
        print(
            "X/6 - Sorry, try again tomorrow!"
        )  # If winning does not occur at turn 6, turn adds to 7 and we should print a losing message


if __name__ == "__main__":
    main(secret="codesd")

# Filename:     count_frequency.py
# Date:         1/14/2022
# Purpose:      Count the number of chars in a string
# Name:         Nathan Pham


def prompt(message: str) -> str:
    return input(message).lower()


def main() -> None:
    while True:
        name = prompt("Enter a name > ")
        frequency = {}

        if name == "quit": break
        for char in name: frequency[char] = frequency.get(char, 0) + 1
        for char, n in frequency.items(): print(f"The name {name} contains {n} {char}'s.")


if __name__ == "__main__":
    main()
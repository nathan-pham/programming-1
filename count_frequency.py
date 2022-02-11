# Filename:     count_frequency.py
# Date:         1/14/2022
# Purpose:      Count the number of chars in a string
# Name:         Nathan Pham


from typing import Dict, Any


def prompt(message: str) -> str:
    return input(message).lower()


def count_char_frequency(message: str) -> Dict[Any, int]:
    """
    Count the number of chars in a string
    """

    frequency = {}
    for char in message: frequency[char] = frequency.get(char, 0) + 1
    return frequency


def count_word_frequency(message: str) -> Dict[Any, int]:
    """
    Count the number of words in a string
    """
    
    frequency = {}
    for word in message.replace("\n", " ").split(): frequency[word] = frequency.get(word, 0) + 1
    return frequency


def main() -> None:
    while True:
        name = prompt("Enter a name > ")
        frequency = {}

        if name == "quit": break
        for char in name: frequency[char] = frequency.get(char, 0) + 1
        for char, n in frequency.items(): print(f"The name {name} contains {n} {char}'s.")


if __name__ == "__main__":
    main()
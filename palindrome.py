# Filename:     palindrom.py
# Date:         1/14/2022
# Purpose:      Determine if a string is a palindrome
# Name:         Nathan Pham


def prompt(message: str) -> str:
    return input(message).lower()


def main() -> None:
    while True:
        name = prompt("Enter a name > ")
        if name == "quit": break
        print(f"{name} is a palindrome." if name == name[::-1] else f"{name} is not a palindrome.")

if __name__ == "__main__":
    main()
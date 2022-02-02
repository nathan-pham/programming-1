# Filename:     average_test_score.py
# Date:         1/14/2022
# Purpose:      Calculate the next test score u need
# Name:         Nathan Pham


from typing import List
import re


def prompt(message: str, enforce: List[str] = []) -> str:
    response = input(message)
    if response in enforce or not enforce:
        return response
    return prompt(message, enforce)


def print_menu() -> List[str]:
    options = [
        "[g] find average test score",
        "[a] add another test score",
        "[p] predict what you need to get to earn a B",
        "[q] quit"
    ]

    print("\n" + "\n".join(options))
    return [re.search(r"\[([^]]+)]", option).group(1) for option in options]


def main(test: List[int]) -> None:
    while True:
        enforce = print_menu()
        mode = prompt("enter an option > ", enforce)

        if mode == "g":
            avg = sum(test) / len(test)
            print(f"average test score: {avg:.2f}")

        elif mode == "a":
            test.append(int(prompt("enter a new test score > ")))
        
        elif mode == "p":
            res = 80 * (len(test) + 1) - (sum(test))
            print(f"you need at least a {res:.2f} on your next test")

        if mode == "q": break

    return

if __name__ == "__main__":
    tests = [85, 79, 92, 98, 88, 64, 94]
    main(tests)
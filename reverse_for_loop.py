# Filename:     reverse_for_loop.py
# Date:         1/12/2022
# Purpose:      Demonstrate for loop
# Name:         Nathan Pham

def prompt(message: str) -> int:
    try:
        return int(input(message))
    except ValueError:
        return prompt(message)


def sum_until(number: int) -> int:
    sum = 0
    for i in range(number + 1):
        sum += i
    return sum


def main() -> None:
    number = prompt("Enter a number > ")

    for i in range(number + 1):
        total = sum_until(i)
        if total > number:
            print(i - 1)
            break

main()

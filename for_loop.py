# Filename:     for_loop.py
# Date:         1/12/2022
# Purpose:      Demonstrate for loop
# Name:         Nathan Pham

def prompt(message: str) -> int:
    try: return int(input(message))
    except ValueError: return prompt(message)

def main() -> None:
    number = prompt("Enter a number > ")
    sum = 0
    for i in range(number + 1):
        sum += i

    print(f"The sum of the numbers from 0 to {number} is {sum}." if sum < 1000 else f"God damn that's a big number. The sum is {sum}.")

main()
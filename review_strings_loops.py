# Filename:     review_strings_loops.py
# Date:         1/18/2022
# Purpose:      Small programs that showcase Strings and loops
# Name:         Nathan Pham


# print every second letter of a string
def program_1(start: int = 0) -> None:
    string = input("Enter a string > ")

    for i in range(start, len(string), 2):
        print(string[i])


# print every second letter of a string starting from index 1
def program_2() -> None:
    program_1(1)


# add up every third digit
def program_3() -> None:
    number = input("Enter a number > ")
    result = sum([int(number[i]) for i in range(0, len(number), 3)])
    print(f"result = {result}")


# random shit
def program_4() -> None:
    number = int(input("Enter a number > ")) * 3
    result = sum([int(i) for i in list(str(number))]) if number > 10 else number
    print(f"result = {result}")


if __name__ == "__main__":
    program_1()
    program_2()
    program_3()
    program_4()


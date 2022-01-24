# Filename:     phone_number_checker.py
# Date:         1/24/2022
# Purpose:      Validate phone number format
# Name:         Nathan Pham

import re


# remove special chars and whitespace
def remove_formatting(phone_number: str) -> str:
    return re.sub(r"[()-.\s]", "", phone_number)


# re-add special chars and whitespace
def add_formatting(phone_number: str) -> str:
    return f"({phone_number[:3]}) {phone_number[3:6]} - {phone_number[6:len(phone_number)]}"


# main method
def main() -> None:
    while True:
        phone_number = input("Enter a phone number > ")

        if phone_number == "quit":
            break

        phone_number = remove_formatting(phone_number)

        print(phone_number, len(phone_number), add_formatting(phone_number))

        print(f"Phone number: {add_formatting(phone_number)}" if len(
            phone_number) == 10 else "Invalid phone number.")


if __name__ == "__main__":
    main()

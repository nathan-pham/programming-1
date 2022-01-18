# Filename:     password_checker.py
# Date:         1/18/2022
# Purpose:      Determine if a password is a strong password
# Name:         Nathan Pham


from typing import List, Tuple
import re


# prompt user for a string
def prompt(message: str) -> str:
    return input(message)


# get password strength as defined by conditions
def get_password_strength(password: str) -> Tuple[List[bool], List[str]]:

    conditions = [
        len(password) >= 8,
        True in [char.islower() for char in password],
        True in [char.isupper() for char in password],
        True in [char.isnumeric() for char in password],
        re.compile("[@_!#$%^&*()<>?/\|}{~:]").search(password) is not None,
    ]

    errors = [
        "more than 8 characters.",
        "a lowercase letter.",
        "an uppercase letter.",
        "a number.",
        "a special character.",
    ]

    return conditions, errors


# get an adjective to describe strength 
def get_adjective(strength: int) -> str:

    adjectives = {
        5: "Really strong",
        4: "Strong",
        3: "Medium",
        2: "Weak"
    }

    adjective = adjectives.get(strength, "Weak")
    return adjective


# main method
def main() -> None:

    while True:

        # prompt for a password
        password = prompt("Enter a password > ")

        # quit if necessary
        if password.lower() == "quit": break

        conditions, errors = get_password_strength(password)
        strength = conditions.count(True)

        adjective = get_adjective(strength)
        print(f"{adjective} password!")

        # if password strength is below medium, describe what's missing
        if strength < 3:

            # loop through conditions and errors
            for i in range(len(conditions)):
                condition = conditions[i]
                error = errors[i]

                # print the error
                if not condition: 
                    print(f"To improve your password, use {error}")

if __name__ == "__main__":
    main()
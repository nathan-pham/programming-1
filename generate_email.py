# Filename:     generate_email.py
# Date:         2/18/2022
# Purpose:      generate an email given the first & last name
# Name:         Nathan Pham


def generate_email(first_name: str, last_name: str) -> str:
    domain = "puhsd.k12.ca.us"
    return f"{last_name}{first_name[0]}@{domain}".lower()


def main() -> None:
    first_name = input("enter your first name > ")
    last_name = input("enter your last name > ")

    print(f"your email is {generate_email(first_name, last_name)}")


if __name__ == "__main__":
    main()
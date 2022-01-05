# import libraries
from typing import List

# prompt for a message & enforce a certain list of string responses
def prompt(message: str, enforce: List[str] = []) -> str:
    result = input(message)
    return prompt(message, enforce) if (result not in enforce and len(enforce) > 0) else result 

# prompt for name & favorite beverage/gum
name = prompt("What is your name? ")
food = prompt("Do you like soda or gum? ", [ "soda", "gum" ])

# if food is soda then prompt for a soda type
if food == "soda":
    soda_type = prompt("Do you like pepsi or coke? ", [ "pepsi", "coke" ])

    # print a message based on the soda type
    print(f"{name} likes {soda_type}.")

# else if food is gum then prompt for a gum flavor
elif food == "gum":
    gum_flavor = prompt("Do you like orange or mint flavored gum? ", [ "orange", "mint" ])

    # print a message based on the gum flavor
    print(f"{name} likes {gum_flavor} {food}.")
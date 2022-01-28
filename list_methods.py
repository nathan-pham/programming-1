# Filename:     list_methods.py
# Date:         1/27/2022
# Purpose:      Use some list methods
# Name:         Nathan Pham

from typing import List, Tuple

# get the first char & lowercase it
get_first = lambda char : char[0].upper()

# generate a menu
def create_menu(options: List[str]) -> Tuple[str, List[str]]:
    menu = "\n".join([f"[{get_first(o)}] {o} item" for o in options])
    options = [get_first(o) for o in options]
    return menu, options

# prompt user for a string & enforce list of responses
def prompt(message: str, enforce: List[str] = []) -> str:
    response = input(message)
    return response if (response.upper() in enforce or not enforce) else prompt(message, enforce)

# main method
def main() -> None:
    array = ["apple", "orange", "cherry"]
    options = ["add", "insert", "count occurences of", "delete", "replace", "quit"]
    menu, enforce_options = create_menu(options)

    # print array statex
    print_array = lambda : print(f"\narray: {', '.join(array)}")
    print_array()
    
    while True:
        
        print(menu)
        option = prompt("Enter an option > ", enforce=enforce_options).lower()

        if option == "q": break        
        elif option == "a": array.append(prompt("Enter an item to add > "))
    
        elif option == "i": 
            item = prompt("Enter an item to insert > ")
            index = int(prompt("Enter an index > "))
            array.insert(index, item)

        elif option == "c": print(str(array.count(prompt("Enter an item to count > "))) + " occurrences")
        elif option == "d": array.remove(prompt("Enter an item to remove > "))

        elif option == "r": 
            to_remove = prompt("Enter a item to remove > ")
            replace_with = prompt("Ente ran item to replace it with > ")
            array = [replace_with if el == to_remove else el for el in array]
        
        # print array state
        print_array()
        
if __name__ == "__main__":
    main()
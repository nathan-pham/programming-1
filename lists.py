# Filename:     lists.py
# Date:         1/26/2022
# Purpose:      Showcase a list
# Name:         Nathan Pham

# main method
def main() -> None:

    # declare variables, arbitrary list
    lists = ["goldfish", "cheezit", "cheetoes", "chips"]
    item = input("Enter an item > ")
    
    print(f"\"{item}\" is in the list at index {lists.index(item)}" if item in lists else f"\"{item}\" is not in the list.")

if __name__ == "__main__":
    main()
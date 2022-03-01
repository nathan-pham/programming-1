# Filename:     separate_animals.py
# Date:         2/28/2022
# Purpose:      Separate a string of animals into a list
# Name:         Nathan Pham


from typing import List


def break_string(string: str) -> List:
    """
    Separate a string of animals into a list

    Args:
        string (str): list of animals

    Returns:
        List: array of all of the animals within the string

    Examples:
    >>> break_string("elephantkangarooaardvark")
    """

    array = []

    for i in range(0, len(string), 8):
        array.append(string[i:i+8])

    return array


def main() -> None:
    mystring = "elephantkangarooaardvarkanteatersquirrelflamingomongoosechipmunkgoldfishbluebirdstarfishbullfrog"
    for animal in break_string(mystring):
        print(animal)
        

if __name__ == "__main__":
    main()
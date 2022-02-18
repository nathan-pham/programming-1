# Filename:     vertical_graph.py
# Date:         2/18/2022
# Purpose:      create a text-based vertical graph from a list
# Name:         Nathan Pham


from horizontal_graph import to_2d
from typing import List, Any


def print_graph(array: List[List[Any]]) -> None:
    """
    print a vertical graph
    """

    # get maximum height of a single bar
    padding = max([item[-1] for item in array])

    # pad all single characters with spaces
    pad = lambda item : [f" {char} " if len(char) == 1 else char for char in item]

    # columns array
    columns = []

    # loop through array
    for item, value in array:

        # assemble a column (padding + asterisks + --- + item)
        columns.append(list((padding - value) * " ") + list(value * "*") + ["---"] + list(item))

    # ensure that each array is the same length by adding spaces if necessary
    padding = max([len(row) for row in columns])
    columns = [ pad(row + list((padding - len(row)) * " ")) for row in columns]
    
    # print the graph sort of like a printer (1st line -> 2nd line -> 3rd line)
    print()
    for i in range(len(columns[0])):
        for row in columns:
            print(row[i], end="")
        print()

def main() -> None:
    print_graph(to_2d(["cat", 5, "dog", 3, "zebra", 2, "bird", 7]))


if __name__ == "__main__":
    main()

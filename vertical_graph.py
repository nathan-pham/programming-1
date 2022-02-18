# Filename:     vertical_graph.py
# Date:         2/18/2022
# Purpose:      create a text-based vertical graph from a list
# Name:         Nathan Pham


from horizontal_graph import to_2d
from typing import List, Any


def print_graph(array: List[List[Any]]) -> None:
    padding = max([item[-1] for item in array])
    pad = lambda item : [f" {char} " if len(char) == 1 else char for char in item]

    columns = []

    for item, value in array:
        columns.append(list((padding - value) * " ") + list(value * "*") + ["___"] + list(item))
        # columns.append(list(item))

    padding = max([len(row) for row in columns])
    columns = [ pad(row + list((padding - len(row)) * " ")) for row in columns]
    
    print()
    for i in range(len(columns[0])):
        for row in columns:
            print(row[i], end="")
        print()

def main() -> None:
    print_graph(to_2d(["cat", 5, "dog", 3, "zebra", 2, "bird", 7]))


if __name__ == "__main__":
    main()

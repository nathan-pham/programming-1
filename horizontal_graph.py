# Filename:     horizontal_graph.py
# Date:         2/18/2022
# Purpose:      create a text-based horizontal graph from a list
# Name:         Nathan Pham

from typing import List, Tuple, Union, Any


def print_graph(array: List[List[Any]]) -> None:
    for (title, value) in array:
        print("%-10s | %s" % (title, "* " * value))


def to_2d(array: List[Union[str, int]]) -> List[List[Any]]:
    new_array = []

    for i in range(0, len(array) - 1, 2):
        new_array.append([array[i], array[i + 1]])

    return new_array


def main() -> None:
    print_graph(to_2d(["cat", 5, "dog", 3, "zebra", 2, "bird", 7]))


if __name__ == "__main__":
    main()

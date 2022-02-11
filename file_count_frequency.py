# Filename:     file_count_frequnecy.py
# Date:         2/11/2022
# Purpose:      Count the number of words in a file
# Name:         Nathan Pham


from typing import Tuple, List, Dict, Any

from count_frequency import count_word_frequency
from heap_sort import random_sort


def dict_to_params(frequency: Dict[str, int]) -> Tuple[List[str], List[int]]:
    """
    Convert a dictionary to a list of parameters (keys & values for random_sort)
    """

    keys = []
    values = []

    for key, value in frequency.items():
        keys.append(key)
        values.append(value)

    return keys, values


def print_frequency(labels: List[str], scores: List[int]) -> None:
    """
    Print the frequency of each word in the file
    """

    for i in range(len(labels)):
        print("%-20s %s" % (labels[i], scores[i]))


def main() -> None:
    with open("./files/i_too_poem.txt") as file:
        frequency = count_word_frequency(file.read().lower())
        print_frequency(*random_sort(*dict_to_params(frequency)))

if __name__ == "__main__":
    main()
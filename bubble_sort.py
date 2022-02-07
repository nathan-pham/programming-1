# Filename:     bubble_sort.py
# Date:         2/7/2022
# Purpose:      Sort a list of integers with bubble sort
# Name:         Nathan Pham


from typing import List


def bubble_sort(array: List[int]) -> List[int]:

    for j in range(len(array)):
        for i in range(len(array) - 1 - j):
            next_i = i + 1
            if array[i] > array[next_i]:
                array[i], array[next_i] = array[next_i], array[i]

    return array


if __name__ == "__main__":
    test = [91, 62, 92, 78, 86, 74, 94, 85]
    print(test)
    print(bubble_sort(test))    
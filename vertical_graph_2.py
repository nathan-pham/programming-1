# Filename:     vertical_graph_2.py
# Date:         5/6/2022
# Purpose:      create a text-based vertical graph from a list
# Name:         Nathan Pham

from typing import List, Union

def print_graph(array: List[Union[int, str]]):
    max_stars = max(*[array[i] for i in range(1, len(array), 2)]) # 7
    max_animal = max(*[len(array[i]) for i in range(0, len(array), 2)]) # 5

    for i in range(max_stars): # loop through height of graph
        for j in range(1, len(array), 2): 
            if array[j] + i > max_stars: # if number in array + current row > maximum; switch prints to switch alignment
                print("*", end=" ") # print star
            else:
                print(" ", end=" ") # otherwise add padding
        print()

    print("-" * (len(array) - 1))

    for i in range(max_animal): # loop through height of bottom graph
        for j in range(0, len(array), 2):
            if i < len(array[j]): # if current row < length of animal in array then you can print cell
                print(array[j][i], end=" ") # print character at row 
            else:
                print(" ", end=" ") # otherwise add padding
        print()

def main():
    print_graph(["cat", 5, "dog", 3, "zebra", 2, "bird", 7])

if __name__ == "__main__":
    main()

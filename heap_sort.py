# Filename:     heap_sort.py
# Date:         2/1/2022
# Purpose:      Heap sort
# Name:         Nathan Pham

from typing import Tuple, List
from copy import deepcopy

def random_sort(labels: List[str], scores: List[int]) -> Tuple[List[str], List[int]]:
    if len(scores) != len(scores):
        return None

    for i in range(len(scores)):
        for j in range(i, len(scores)):
            if scores[j] > scores[i]:
                labels[j], labels[i] = labels[i], labels[j]
                scores[j], scores[i] = scores[i], scores[j]

    return labels, scores



if __name__ == "__main__":
    students = ["dog", "cat", "zebra", "bird", "pinguin", "fish", "whale", "tuna"]
    scores = [91, 62, 92, 78, 86, 74, 94, 85]

    labels, scores = random_sort(deepcopy(students), deepcopy(scores))
    for i in range(len(labels)):
        print("%-20s %s" % (labels[i], scores[i]))
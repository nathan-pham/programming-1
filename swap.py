# Filename:     swap.py
# Date:         2/1/2022
# Purpose:      Swap elements in an array
# Name:         Nathan Pham

from functools import reduce

_min = lambda array : reduce(lambda a, b : a if a < b else b, array)
_max = lambda array : reduce(lambda a, b : a if a > b else b, array)

def main() -> None:
    array = [11, 23, 4, 3, 2, 9, 16]
    
    min_el, max_el = _min(array), _max(array)
    i, j = array.index(min_el), array.index(max_el)
    
    array[0], array[i] = min_el, array[0]
    array[-1], array[j] = max_el, array[-1]
    
    print(array)


if __name__ == "__main__":
    main()
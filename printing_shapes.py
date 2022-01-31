# Filename:     printing_shapes.py
# Date:         1/24/2022
# Purpose:      Print 4 different shapes with .center()
# Name:         Nathan Pham

from typing import List
import math, sys

# error allowed when generating shapes
EPSILON = 2

# create a 2D grid of size grid_size
def create_grid(grid_size: int) -> List[List[int]]:
    grid = [["⬛" for x in range(grid_size)] for y in range(grid_size)]
    return grid

# print a circle
def create_circle(grid_size: int) -> None:
    grid = create_grid(grid_size)

    center_x = grid_size // 2
    center_y = grid_size // 2
    radius = 5

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (x - center_x)**2 + (y - center_y)**2 <= radius**2 - EPSILON**2:
                grid[y][x] = "🟩"

    return grid

# print 2 triangles -> hourglass
def create_hourglass(grid_size: int) -> None:
    grid = create_grid(grid_size)

    center_x = grid_size // 2
    center_y = grid_size // 2

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if x <= y and y >= center_y - x + center_x: grid[y][x] = "🟩"
            if x >= y and y <= center_y - x + center_x: grid[y][x] = "🟩"

    return grid

# print a right triangle
def create_triangle(grid_size: int) -> None:
    grid = create_grid(grid_size)

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if x <= y:
                grid[y][x] = "🟩"

    return grid

# print a bizarre #
def create_cross(grid_size: int) -> None:
    grid = create_grid(grid_size)

    center_x = grid_size // 2
    center_y = grid_size // 2

    margin = 4

    a, b = margin, margin
    c, d = grid_size - margin, grid_size - margin

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if math.sqrt(abs((a - x) * (x - c))) * math.sqrt(abs((b - y) * (y - d))) <= EPSILON / 2:
                grid[y][x] = "🟩"

    return grid

# render a 2D grid
def render_grid(grid: List[List[int]]) -> None:
    print("\n".join(["".join(row) for row in grid]))


# prompt & restrict responses to list
def prompt(message: str, enforce: List[str]) -> str:
    response = input(message)
    if response in enforce: return response
    return prompt(message, enforce)

def main() -> None:
    grid_size = 11
    shapes = {
        "circle": create_circle,
        "hourglass": create_hourglass,
        "triangle": create_triangle,
        "cross": create_cross,
        "quit": lambda _ : sys.exit(0)
    }

    while True:
        shape = prompt("Choose a shape: ", list(shapes.keys()))
        render_grid(shapes[shape](grid_size))

if __name__ == "__main__":
    main()
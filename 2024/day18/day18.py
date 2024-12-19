SIZE = 71
from copy import deepcopy


def ingest_bytes(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
        for line in range(len(lines)):
            lines[line] = (int(lines[line].split(",")[0]), int(lines[line].split(",")[1]))
    return lines


def make_grid(size):
    grid = [["." for x in range(size + 2)] for y in range(size + 2)]
    grid[size][size] = "0"
    for i in range(size + 2):
        grid[0][i] = "#"
        grid[size + 1][i] = "#"
        grid[i][0] = "#"
        grid[i][size + 1] = "#"
    return grid


def mark_neighbours(grid, row, column):
    new_value = int(grid[row][column]) + 1
    if grid[row][column + 1] == ".":
        grid[row][column + 1] = str(new_value)
    elif grid[row][column + 1].isdigit():
        grid[row][column + 1] = str(min(new_value, int(grid[row][column + 1])))
    if grid[row][column - 1] == ".":
        grid[row][column - 1] = str(new_value)
    elif grid[row][column - 1].isdigit():
        grid[row][column - 1] = str(min(new_value, int(grid[row][column - 1])))
    if grid[row + 1][column] == ".":
        grid[row + 1][column] = str(new_value)
    elif grid[row + 1][column].isdigit():
        grid[row + 1][column] = str(min(new_value, int(grid[row + 1][column])))
    if grid[row - 1][column] == ".":
        grid[row - 1][column] = str(new_value)
    elif grid[row - 1][column].isdigit():
        grid[row - 1][column] = str(min(new_value, int(grid[row - 1][column])))
    return grid

def iterate(grid):
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] not in [".", "#"]:
                grid = mark_neighbours(grid, row, column)
    return grid


def day_18(input_name):
    total = 0
    grid = make_grid(SIZE)
    bytes = ingest_bytes(input_name)
    for i in range(min(1024, len(bytes))):
        column, row = bytes[i]
        grid[row + 1][column + 1] = "#"
    for row in grid:
        print(row)
    done = False
    while not done:
        og_grid = deepcopy(grid)
        grid = iterate(grid)
        if og_grid == grid:
            done = True
    for row in grid:
        print(row)
    return grid[1][1]


def day_18_part_2(input_name):
    total = 0
    grid = make_grid(SIZE)
    bytes = ingest_bytes(input_name)
    for i in range(1024):
        column, row = bytes[i]
        grid[row + 1][column + 1] = "#"

    for i in range(1024, len(bytes)):
        done = False
        column, row = bytes[i]
        grid[row + 1][column + 1] = "#"
        attempt_grid = deepcopy(grid)
        while not done:
            og_grid = deepcopy(attempt_grid)
            attempt_grid = iterate(attempt_grid)
            if og_grid == attempt_grid:
                done = True
        if attempt_grid[1][1] == ".":
            for row in grid:
                print(row)
            return bytes[i]
        print(f"Solvable for i = {i}")


if __name__ == '__main__':
    print("Running main")
    result = day_18_part_2(input_name="day18_input.txt")
    print(result)

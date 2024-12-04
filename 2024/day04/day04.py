import re
ROW_LENGTH = 140
COLUMNS = 140
def ingest_message(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
    return lines
def check_directions(lines, row, column):
    total = 0
    total += check_right(lines,row, column)
    total += check_left(lines, row, column)
    total += check_up(lines, row, column)
    total += check_down(lines, row, column)
    total += check_up_left(lines, row, column)
    total += check_up_right(lines, row, column)
    total += check_down_left(lines, row, column)
    total += check_down_right(lines, row, column)
    return total

def check_crosses(lines, row, column):
    total = 0
    total += check_diagonal_cross(lines, row, column)
    return total

def valid_cross_elements(first, second):
    aspas = set()
    aspas.update(first)
    aspas.update(second)
    return "M" in aspas and "S" in aspas


def check_diagonal_cross(lines, row, column):
    if row < 1 or row > (ROW_LENGTH - 1) or column < 1 or column > (COLUMNS - 1):
        return 0
    if valid_cross_elements(lines[row-1][column-1], lines[row+1][column+1]) and \
            valid_cross_elements(lines[row+1][column-1], lines[row-1][column+1]):
        print(f"Found diagonal cross at {row}, {column}")
        return 1
    return 0

def check_right(lines, row, column):
    if column > (ROW_LENGTH - 4):
        return 0
    if lines[row][column+1] == "M" and lines[row][column+2] == "A" and lines[row][column+3] == "S":
        print(f"XMAS found going right at {row}, {column}")
        return 1
    return 0


def check_left(lines, row, column):
    if column < 3:
        return 0
    if lines[row][column-1] == "M" and lines[row][column-2] == "A" and lines[row][column-3] == "S":
        print(f"XMAS found going left at {row}, {column}")
        return 1
    return 0


def check_up(lines, row, column):
    if row < 3:
        return 0
    if lines[row-1][column] == "M" and lines[row-2][column] == "A" and lines[row-3][column] == "S":
        print(f"XMAS found going up at {row}, {column}")
        return 1
    return 0


def check_down(lines, row, column):
    if row > (ROW_LENGTH - 4):
        return 0
    if lines[row+1][column] == "M" and lines[row+2][column] == "A" and lines[row+3][column] == "S":
        print(f"XMAS found going down at {row}, {column}")
        return 1
    return 0


def check_down_left(lines, row, column):
    if row > (ROW_LENGTH - 4) or column < 3:
        return 0
    if lines[row+1][column-1] == "M" and lines[row+2][column-2] == "A" and lines[row+3][column-3] == "S":
        print(f"XMAS found going down left at {row}, {column}")
        return 1
    return 0


def check_down_right(lines, row, column):
    if row > (ROW_LENGTH - 4) or column > (COLUMNS - 4):
        return 0
    if lines[row+1][column+1] == "M" and lines[row+2][column+2] == "A" and lines[row+3][column+3] == "S":
        print(f"XMAS found going down right at {row}, {column}")
        return 1
    return 0


def check_up_left(lines, row, column):
    if row < 3 or column < 3:
        return 0
    if lines[row-1][column-1] == "M" and lines[row-2][column-2] == "A" and lines[row-3][column-3] == "S":
        print(f"XMAS found going up left at {row}, {column}")
        return 1
    return 0


def check_up_right(lines, row, column):
    if row < 3 or column > (COLUMNS - 4):
        return 0
    if lines[row-1][column+1] == "M" and lines[row-2][column+2] == "A" and lines[row-3][column+3] == "S":
        print(f"XMAS found going up right at {row}, {column}")
        return 1
    return 0


def day_04(input_name):
    lines = ingest_message(input_name=input_name)
    print(type(lines))
    total = 0
    for row in range(len(lines)):
        for column in range(len(lines[row])):
            if lines[row][column] == 'X':
                print(f"X found at {row}, {column}")
                total += check_directions(lines, row, column)
    return total

def day_04_part_2(input_name):
    lines = ingest_message(input_name=input_name)
    print(type(lines))
    total = 0
    for row in range(len(lines)-1):
        for column in range(len(lines[row])-1):
            if lines[row][column] == 'A':
                print(f"A found at {row}, {column}")
                total += check_crosses(lines, row, column)
    print(total)
    return total



if __name__ == '__main__':
    print("Running main")
    result = day_04_part_2(input_name="day04_input.txt")
    print(result)

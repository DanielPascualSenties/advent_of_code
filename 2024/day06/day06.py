SIZE = 130
def ingest_message(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
    for line in range(len(lines)):
        lines[line] = list(lines[line])
        if "\n" in lines[line]:
            lines[line].remove("\n")
    return lines


def is_guard(character):
    return character in ["<", ">", "^", "v"]


def locate_guard(lab_map):
    for i in range(len(lab_map)):
        for j in range(len(lab_map[i])):
            if is_guard(lab_map[i][j]):
                return i, j
    print('Didnt find the guard')
    raise EOFError


def spin_guard(lab_map, row, column):
    guard = lab_map[row][column]
    if guard == '>':
        lab_map[row][column] = "v"
        return lab_map
    if guard == 'v':
        lab_map[row][column] = "<"
        return lab_map
    if guard == '<':
        lab_map[row][column] = "^"
        return lab_map
    if guard == '^':
        lab_map[row][column] = ">"
        return lab_map
    print(f"Misidentified the guard when spinning, read {guard}")
    return lab_map


def identify_next_step(lab_map, row, column):
    guard = lab_map[row][column]
    if guard == '>':
        return row, column+1
    if guard == '<':
        return row, column-1
    if guard == '^':
        return row-1, column
    if guard == 'v':
        return row+1, column
    print(f"Misidentified the guard, read {guard}")
    return -1, -1

def move_guard(lab_map, row, column, total):
    next_row, next_column = identify_next_step(lab_map, row, column)
    if next_row < 0 or next_row >= SIZE or next_column < 0 or next_column >= SIZE:
        print("We are about to leave the map")
        return lab_map, next_row, next_column, total
    if lab_map[next_row][next_column] == ".":
        total += 1
        lab_map[next_row][next_column] = lab_map[row][column]
        lab_map[row][column] = "X"
        row = next_row
        column = next_column
        return lab_map, row, column, total
    if lab_map[next_row][next_column] == "X":
        lab_map[next_row][next_column] = lab_map[row][column]
        lab_map[row][column] = "X"
        row = next_row
        column = next_column
        return lab_map, row, column, total
    if lab_map[next_row][next_column] == "#":
        lab_map = spin_guard(lab_map, row, column)
        return lab_map, row, column, total

def print_lab(lab_map):
    for row in lab_map:
        print(row)

def day_06(input_name):
    lab_map = ingest_message(input_name=input_name)
    total = 1
    row, column = locate_guard(lab_map)
    while True:
        if row < 0 or row >= SIZE or column < 0 or column >= SIZE:
            return total
        #print_lab(lab_map)
        lab_map, row, column, total = move_guard(lab_map, row, column, total)
    return total

def unsolvable_map(lab_map, row, column):
    steps_taken = 0
    total = 0
    while steps_taken < SIZE * SIZE:
        steps_taken += 1
        if row < 0 or row >= SIZE or column < 0 or column >= SIZE:
            return False
            #print("This map is not unsolvable")
        lab_map, row, column, total = move_guard(lab_map, row, column, total)

    print("This map is unsolvable")
    return True


def day_06_part_2(input_name):
    lab_map = ingest_message(input_name=input_name)
    total = 1
    row, column = locate_guard(lab_map)
    unsolvables = 0
    for i in range(len(lab_map)):
        for j in range(len(lab_map[i])):
            if lab_map[i][j] == '.':
                new_lab_map = [x[:] for x in lab_map]
                new_lab_map[i][j] = "#"
                #print_lab(new_lab_map)
                if unsolvable_map(new_lab_map, row, column):
                    unsolvables += 1
    return unsolvables



if __name__ == '__main__':
    print("Running main")
    result = day_06_part_2(input_name="day06_input.txt")
    print(result)

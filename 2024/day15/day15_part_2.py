def ingest_moves(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    result = []
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
        for line in lines:
            line = list(line.replace("\n", ""))
            result += line
    print(result)
    return result


def ingest_sea_map(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
        for line in range(len(lines)):
            lines[line] = list(lines[line].replace("\n", "").replace("#", "##").replace(".", "..").replace("O", "[]")
                               .replace("@", "@."))

    return lines


def find_robot(sea_map):
    for row in range(len(sea_map)):
        if "@" in sea_map[row]:
            return row, sea_map[row].index("@")
    print("COULD NOT FIND THE ROBOT")
    raise Exception


def move_right(sea_map):
    robot_row, robot_column = find_robot(sea_map)
    for i in range(robot_column + 1, 100):
        if sea_map[robot_row][i] == ".":
            for j in range(i, robot_column + 1, -1):
                sea_map[robot_row][j] = sea_map[robot_row][j - 1]
            sea_map[robot_row][robot_column] = "."
            sea_map[robot_row][robot_column + 1] = "@"
            print("Moved right")
            return sea_map
        if sea_map[robot_row][i] in ["]", "["]:
            pass
        if sea_map[robot_row][i] == "#":
            print("Cannot move right")
            return sea_map


def move_left(sea_map):
    robot_row, robot_column = find_robot(sea_map)
    for i in range(robot_column, -1, -1):
        if sea_map[robot_row][i] == ".":
            for j in range(i, robot_column):
                sea_map[robot_row][j] = sea_map[robot_row][j + 1]
            sea_map[robot_row][robot_column] = "."
            print("Moved left")
            return sea_map
        if sea_map[robot_row][i] in ["]", "["]:
            pass
        if sea_map[robot_row][i] == "#":
            print("Cannot move left")
            return sea_map


def can_move_down(sea_map, row, column):
    if sea_map[row][column] == ".":
        return True
    if sea_map[row][column] == "#":
        return False
    if sea_map[row][column] == "[":
        return can_move_down(sea_map, row + 1, column) and can_move_down(sea_map, row + 1, column + 1)
    if sea_map[row][column] == "]":
        return can_move_down(sea_map, row + 1, column) and can_move_down(sea_map, row + 1, column - 1)


def push_down(sea_map, row, column):
    if sea_map[row + 1][column] == ".":
        sea_map[row + 1][column] = sea_map[row][column]
        return sea_map
    elif sea_map[row + 1][column] == "[":
        sea_map = push_down(sea_map, row + 1, column)
        sea_map = push_down(sea_map, row + 1, column + 1)
        sea_map[row + 1][column] = sea_map[row][column]
        sea_map[row + 1][column+1] = "."
        return sea_map
    elif sea_map[row + 1][column] == "]":
        sea_map = push_down(sea_map, row + 1, column)
        sea_map = push_down(sea_map, row + 1, column - 1)
        sea_map[row + 1][column] = sea_map[row][column]
        sea_map[row + 1][column-1] = "."
        return sea_map
    elif sea_map[row + 1][column] == "#":
        print("WE SHOULD NOT BE TRYING TO MOVE HERE")
        raise Exception


def push_up(sea_map, row, column):
    if sea_map[row - 1][column] == ".":
        sea_map[row - 1][column] = sea_map[row][column]
        return sea_map
    elif sea_map[row - 1][column] == "[":
        sea_map = push_up(sea_map, row - 1, column)
        sea_map = push_up(sea_map, row - 1, column + 1)
        sea_map[row - 1][column] = sea_map[row][column]
        sea_map[row - 1][column+1] = "."
        return sea_map
    elif sea_map[row - 1][column] == "]":
        sea_map = push_up(sea_map, row - 1, column)
        sea_map = push_up(sea_map, row - 1, column - 1)
        sea_map[row - 1][column] = sea_map[row][column]
        sea_map[row - 1][column-1] = "."
        return sea_map
    elif sea_map[row - 1][column] == "#":
        print("WE SHOULD NOT BE TRYING TO MOVE HERE")
        raise Exception


def move_robot_down(sea_map):
    robot_row, robot_column = find_robot(sea_map)
    if can_move_down(sea_map, robot_row + 1, robot_column):
        print("Can move down")
        sea_map = push_down(sea_map, robot_row, robot_column)
        sea_map[robot_row][robot_column] = "."
        return sea_map
    else:
        print("Cannot move down")
        return sea_map


def can_move_up(sea_map, row, column):
    if sea_map[row][column] == ".":
        return True
    if sea_map[row][column] == "#":
        return False
    if sea_map[row][column] == "[":
        return can_move_up(sea_map, row - 1, column) and can_move_up(sea_map, row - 1, column + 1)
    if sea_map[row][column] == "]":
        return can_move_up(sea_map, row - 1, column) and can_move_up(sea_map, row - 1, column - 1)


def move_robot_up(sea_map):
    robot_row, robot_column = find_robot(sea_map)
    if can_move_up(sea_map, robot_row - 1, robot_column):
        print("Can moveup")
        sea_map = push_up(sea_map, robot_row, robot_column)
        sea_map[robot_row][robot_column] = "."
        return sea_map
    else:
        print("Cannot move up")
        return sea_map


def move_robot(sea_map, move):
    robot_row, robot_column = find_robot(sea_map)
    print(f"robot at ({robot_row}, {robot_column})")
    match move:
        case ">":
            print(f"Moving right")
            return move_right(sea_map)
        case "v":
            print(f"Moving down")
            return move_robot_down(sea_map)
        case "<":
            print(f"Moving left")
            return move_left(sea_map)
        case "^":
            print(f"Moving up")
            return move_robot_up(sea_map)
        case _:
            print(f"ILLEGAL MOVE {move}")
            raise Exception


def get_coordinates(sea_map, row, column):
    if sea_map[row][column] == "[":
        print(f"Found box at {row},{column}")
        coordinates = 100 * row + column
        print(f"Coordinates = {coordinates}")
        return coordinates
    else:
        return 0


def day_15_part_2(input_name):
    total = 0
    map_file = input_name + "_map.txt"
    moves_file = input_name + "_moves.txt"
    sea_map = ingest_sea_map(map_file)
    moves = ingest_moves(moves_file)
    for row in sea_map:
        print(row)
    for move in moves:
        sea_map = move_robot(sea_map, move)
    for row in sea_map:
        print(row)
    for row in range(len(sea_map)):
       for column in range(len(sea_map[row])):
           total += get_coordinates(sea_map, row, column)

    return total


if __name__ == '__main__':
    print("Running main")
    result = day_15_part_2(input_name="day15_input")
    print(result)

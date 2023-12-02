MR = 12
MG = 13
MB = 14


def ingest_message(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
    return lines


def split_color_number(cubes):
    number, color = cubes.strip().split(" ")
    return int(number), color


def compare_with_limits(r, g, b):
    return r <= MR and g <= MG and b <= MB


def get_max_cubes_in_turn(turn):
    color_cubes = turn.split(",")
    red = green = blue = 0
    for color_cube in color_cubes:
        number, color = split_color_number(color_cube)
        if color == "red" and number > red:
            red = number
        if color == "green" and number > green:
            green = number
        if color == "blue" and number > blue:
            blue = number
    return red, green, blue


def get_max_cubes(turns):
    # (red, green, blue)
    max_red = max_green = max_blue = 0
    for turn in turns:
        red, green, blue = get_max_cubes_in_turn(turn)
        max_red = max(max_red, red)
        max_green = max(max_green, green)
        max_blue = max(max_blue, blue)
    return max_red, max_green, max_blue


def sepparate_row(line):
    game, cubes_shown = line.split(":")
    game_number = int("".join([x for x in game if x.isdigit()]))
    return game_number, cubes_shown


def sepparate_turns(cubes_shown):
    turns = cubes_shown.split(";")
    return turns


def day_02(input_name):
    lines = ingest_message(input_name=input_name)
    total = 0
    for line in lines:
        game_number, cubes_shown = sepparate_row(line)
        turns = sepparate_turns(cubes_shown)
        r, g, b = get_max_cubes(turns)
        if compare_with_limits(r, g, b):
            total += game_number

    return total


def day_02_part2(input_name):
    lines = ingest_message(input_name=input_name)
    total = 0
    for line in lines:
        game_number, cubes_shown = sepparate_row(line)
        turns = sepparate_turns(cubes_shown)
        r, g, b = get_max_cubes(turns)
        total += r * g * b
    return total


if __name__ == '__main__':
    print("Running main")
    message = day_02_part2(input_name="day02_input.txt")
    print(message)

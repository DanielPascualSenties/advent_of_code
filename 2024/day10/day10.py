SIZE = 58


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
            lines[line] = [int(x) for x in lines[line]]
    return lines


def get_trail_heads(trail_map):
    trail_heads = []
    for row in range(len(trail_map)):
        for column in range(len(trail_map[row])):
            if trail_map[row][column] == 0:
                trail_heads.append((row, column))
    return trail_heads


def flatten(ls):
    flat_list = []
    for x in ls:
        if isinstance(x, list):
            flat_list += flatten(x)
        else:
            flat_list.append(x)
    return flat_list


def get_summits(trail_map, position):
    row, column = position[0], position[1]
    height = trail_map[row][column]
    summits = []
    if height == 9:
        return row, column
    else:
        if row < SIZE - 1:
            if trail_map[row + 1][column] == height + 1:
                summits.append(get_summits(trail_map, (row + 1, column)))
        if row > 0:
            if trail_map[row - 1][column] == height + 1:
                summits.append(get_summits(trail_map, (row - 1, column)))
        if column < SIZE - 1:
            if trail_map[row][column + 1] == height + 1:
                summits.append(get_summits(trail_map, (row, column + 1)))
        if column > 0:
            if trail_map[row][column - 1] == height + 1:
                summits.append(get_summits(trail_map, (row, column - 1)))
    flattened_summits = flatten(summits)
    return flattened_summits


def get_summits_part_2(trail_map, position):
    row, column = position[0], position[1]
    height = trail_map[row][column]
    summits = 0
    if height == 9:
        return 1
    else:
        if row < SIZE - 1:
            if trail_map[row + 1][column] == height + 1:
                summits += get_summits_part_2(trail_map, (row + 1, column))
        if row > 0:
            if trail_map[row - 1][column] == height + 1:
                summits += get_summits_part_2(trail_map, (row - 1, column))
        if column < SIZE - 1:
            if trail_map[row][column + 1] == height + 1:
                summits += get_summits_part_2(trail_map, (row, column + 1))
        if column > 0:
            if trail_map[row][column - 1] == height + 1:
                summits += get_summits_part_2(trail_map, (row, column - 1))
    return summits


def day_10(input_name):
    trail_map = ingest_message(input_name=input_name)
    print(trail_map)
    total = 0
    trail_heads = get_trail_heads(trail_map)
    print(trail_heads)
    for trail_head in trail_heads:
        summits = get_summits(trail_map, trail_head)
        print(summits)
        total += len(set(summits))
    return total


def day_10_part_2(input_name):
    trail_map = ingest_message(input_name=input_name)
    print(trail_map)
    total = 0
    trail_heads = get_trail_heads(trail_map)
    print(trail_heads)
    for trail_head in trail_heads:
        summits = get_summits_part_2(trail_map, trail_head)
        print(f"Trail head {trail_head} has a score of {summits}")
        total += summits
    return total


if __name__ == '__main__':
    print("Running main")
    result = day_10_part_2(input_name="day10_input.txt")
    print(result)

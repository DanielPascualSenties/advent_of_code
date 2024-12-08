SIZE = 50


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


def distinct_frequencies(map):
    frequencies = {}
    for row in range(len(map)):
        for column in range(len(map[row])):
            elem = map[row][column]
            if elem in frequencies:
                frequencies[elem].append((row, column))
            else:
                frequencies[elem] = [(row, column)]
    frequencies.pop(".")
    return frequencies


def valid_antinode(antinode):
    row = antinode[0]
    column = antinode[1]
    return -1 < row < SIZE and -1 < column < SIZE


def get_antinodes_for_pair_of_antennas(pair, antinodes):
    print(pair)
    first = pair[0]
    second = pair[1]
    difference = (first[0] - second[0], first[1] - second[1])
    print(difference)
    antinode_1 = (first[0] + difference[0], first[1] + difference[1])
    antinode_2 = (second[0] - difference[0], second[1] - difference[1])
    if valid_antinode(antinode_1):
        antinodes.add(antinode_1)
    if valid_antinode(antinode_2):
        antinodes.add(antinode_2)
    return antinodes


def get_antinodes_for_pair_of_antennas_part_2(pair, antinodes):
    print(pair)
    first = pair[0]
    second = pair[1]
    difference = (first[0] - second[0], first[1] - second[1])
    print(difference)
    still_valid = True
    n = 0
    while still_valid:
        antinode_1 = (first[0] + n*difference[0], first[1] + n*difference[1])
        if valid_antinode(antinode_1):
            antinodes.add(antinode_1)
        else:
            still_valid = False
        n+=1
    still_valid = True
    n = 0
    while still_valid:
        antinode_2 = (second[0] - n*difference[0], second[1] - n*difference[1])
        if valid_antinode(antinode_2):
            antinodes.add(antinode_2)
        else:
            still_valid = False
        n += 1
    return antinodes


def get_frequency_antinodes(locations):
    print(locations)
    pairs = [(a, b) for idx, a in enumerate(locations) for b in locations[idx + 1:]]
    print(pairs)
    antinodes = set()
    for pair in pairs:
        get_antinodes_for_pair_of_antennas(pair, antinodes)
    return antinodes


def get_frequency_antinodes_part_2(locations):
    print(locations)
    pairs = [(a, b) for idx, a in enumerate(locations) for b in locations[idx + 1:]]
    print(pairs)
    antinodes = set()
    for pair in pairs:
        get_antinodes_for_pair_of_antennas_part_2(pair, antinodes)
    return antinodes


def day_08(input_name):
    antenna_map = ingest_message(input_name=input_name)
    frequencies = distinct_frequencies(antenna_map)
    antinodes = set()
    for frequency in frequencies:
        antinodes = antinodes.union(get_frequency_antinodes(frequencies[frequency]))
    print(antinodes)
    return len(antinodes)


def day_08_part_2(input_name):
    antenna_map = ingest_message(input_name=input_name)
    frequencies = distinct_frequencies(antenna_map)
    antinodes = set()
    for frequency in frequencies:
        antinodes = antinodes.union(get_frequency_antinodes_part_2(frequencies[frequency]))
    print(antinodes)
    return len(antinodes)


if __name__ == '__main__':
    print("Running main")
    result = day_08_part_2(input_name="day08_input.txt")
    print(result)

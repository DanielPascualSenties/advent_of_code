NUM_BLINKS = 40


def ingest_corridor(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
        line = lines[0]
        corridor = line.split(" ")
    return corridor


def engrave(stone):
    stone_value = int(stone)
    stone_length = len(stone)
    if stone_value == 0:
        return ["1"]
    if stone_length % 2 == 0:
        return [stone[:stone_length // 2], str(int(stone[stone_length // 2:]))]
    return [str(stone_value * 2024)]


def blink(corridor):
    new_corridor = []
    for stone in corridor:
        new_corridor += engrave(stone)
    return new_corridor


def day_11(input_name):
    corridor = ingest_corridor(input_name=input_name)
    for i in range(NUM_BLINKS):
        corridor = blink(corridor)

    print(corridor)
    with open('after_35_blinks.txt', 'w') as f:
        for item in corridor:
            f.write(f"{item} ")
    return len(corridor)


def engrave_recursive(stone, blink_num):
    stone_length = len(stone)
    if blink_num == 1:
        if stone_length % 2 == 0:
            return 2
        else:
            return 1
    stone_value = int(stone)

    if stone_value == 0:
        return engrave_recursive("1", blink_num - 1)
    if stone_length % 2 == 0:
        return engrave_recursive(stone[:stone_length // 2], blink_num - 1) + engrave_recursive(
            str(int(stone[stone_length // 2:])), blink_num - 1)
    return engrave_recursive(str(stone_value * 2024), blink_num - 1)


def day_11_part_2(input_name):
    corridor = ingest_corridor(input_name=input_name)
    total = 0
    counter = 0

    counts = dict()
    for i in corridor:
        counts[i] = counts.get(i, 0) + 1
    elements = len(counts)
    for stone in counts:
        print(f"Calculating values for stone {stone}")
        stone_value = engrave_recursive(stone, NUM_BLINKS) * counts[stone]
        print(f"Value for stone = {stone_value}")
        total += stone_value
        counter += 1
        print(f"Done for {counter} stones of {elements}")

    return total


if __name__ == '__main__':
    print("Running main")
    result = day_11_part_2(input_name="after_35_blinks.txt")
    print(result)

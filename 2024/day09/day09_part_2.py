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
    return lines[0]


def day_09_part_2(input_name):
    layout = ingest_message(input_name=input_name)
    total = 0
    memory_map = generate_memory_map(layout)
    compacted_memory_map = compact_memory_map(memory_map)
    checksum = get_checksum(compacted_memory_map)
    return checksum

def get_checksum(compacted_memory_map):
    total = 0
    multiplier= 0
    for i in compacted_memory_map:
        if i != ".":
            total += int(i) * multiplier
        multiplier += 1
    return total

def get_top_block_size(compacted_memory_map, top):
    top_elem = compacted_memory_map[top]
    return compacted_memory_map.count(top_elem)


def get_first_block_of_size(compacted_memory_map, size):
    sublist = ["."]*size
    i = 0
    occurrences = [i for i in range(len(compacted_memory_map)) if compacted_memory_map[i:i + len(sublist)] == sublist]
    if not occurrences:
        return -1
    else:
        return occurrences[0]

def swap_places(compacted_memory_map, first_block_of_size, top, block_size):
    element_moving = compacted_memory_map[top]
    for i in range(block_size):
        compacted_memory_map[first_block_of_size+i] = element_moving
        compacted_memory_map[top-i] = "."
    return compacted_memory_map

def compact_memory_map(memory_map):
    compacted_memory_map = memory_map.copy()
    top = len(memory_map)-1
    while top > 0:
        print(f"Top = {top}")
        if compacted_memory_map[top] == ".":
            top -= 1
            continue
        block_size = get_top_block_size(compacted_memory_map, top)
        first_block_of_size = get_first_block_of_size(compacted_memory_map, block_size)

        if first_block_of_size == -1 or first_block_of_size > top:
            top -= block_size
        else:
            compacted_memory_map = swap_places(compacted_memory_map,first_block_of_size, top, block_size)
            top -= block_size

    return compacted_memory_map


def generate_memory_map(layout):
    i = 0
    id_number = 0
    memory_map = []
    while i < len(layout):
        block = int(layout[i])
        i += 1
        id_as_str = str(id_number)
        for j in range(block):
            memory_map.append(id_as_str)

        if i < len(layout):
            space = int(layout[i])
            i += 1
            for j in range(space):
                memory_map.append(".")
        id_number += 1

    return memory_map


if __name__ == '__main__':
    print("Running main")
    result = day_09_part_2(input_name="day09_input.txt")
    print(result)

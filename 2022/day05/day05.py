def ingest_crates(line, pillars):
    line_length = len(line)
    split_line = list(line)
    pos = 1
    column = 1
    while pos <= line_length:
        if split_line[pos] != " ":
            pillars[column].append(split_line[pos].strip())
        pos += 4
        column += 1
    return pillars


def read_top(pillars):
    res = ""
    for i in pillars:
        res += pillars[i][0]
    return res


def clean_pillars(pillars):
    empty = []
    for k, v in pillars.items():
        if v:
            v.pop()
        else:
            empty.append(k)
    for k in empty:
        del pillars[k]
    return pillars


def ingest_move(line):
    line = line.split(" ")
    return int(line[1]), int(line[3]), int(line[5])


def make_move(move, pillars):
    number_of_items = move[0]
    source_column = move[1]
    destination_column = move[2]
    for i in range(number_of_items):
        crane = pillars[source_column].pop(0)
        pillars[destination_column].insert(0, crane)
    return pillars


def make_move_part2(move, pillars):
    number_of_items = move[0]
    source_column = move[1]
    destination_column = move[2]
    for i in range(number_of_items):
        crane = pillars[source_column].pop(number_of_items - i - 1)
        pillars[destination_column].insert(0, crane)
        print(pillars)
    return pillars


def day_05(input_name):
    into_moves = False
    pillars = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    with open(input_name) as f:
        lines = f.readlines()
    for i in lines:
        line = i.strip('\n')
        if line == "":
            into_moves = True
            pillars = clean_pillars(pillars)
        elif into_moves:
            move = ingest_move(line)
            pillars = make_move(move, pillars)
        else:
            pillars = ingest_crates(line, pillars)
    top = read_top(pillars)
    return top


def day_05_part2(input_name):
    into_moves = False
    pillars = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    with open(input_name) as f:
        lines = f.readlines()
    for i in lines:
        line = i.strip('\n')
        if line == "":
            into_moves = True
            pillars = clean_pillars(pillars)
        elif into_moves:
            move = ingest_move(line)
            pillars = make_move_part2(move, pillars)
        else:
            pillars = ingest_crates(line, pillars)
    top = read_top(pillars)
    return top


if __name__ == '__main__':
    print(f"Running main")
    top_crates = day_05_part2(input_name="day05_input.txt")
    print(top_crates)

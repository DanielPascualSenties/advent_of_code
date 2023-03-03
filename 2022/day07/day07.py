def process_line(line, current, folders):
    if line == "$ cd ..":
        current.pop()
    elif line == "$ cd /":
        current.append("/")
        folders["/"] = 0
    elif line.split(" ")[0].isnumeric():
        for i in current:
            folders[i] += int(line.split(' ')[0])
    elif line.split(" ")[0] == "dir":
        folders[line.split(' ')[1]] = 0
    elif line.split(" ")[1] == "cd":
        current.append(line.split(' ')[2])
    return current, folders


def recursive_dict_value(folders, elem):
    total = 0
    print(folders[elem])
    for i in range(len(folders[elem])):
        if folders[elem][i].isnumeric():
            total += int(folders[elem][i])
        else:
            total += recursive_dict_value(folders, folders[elem][i])
    return total


def process_line_redux(line, current, stack, folders):
    if line == "$ ls":
        pass
    if line == "$ cd ..":
        current = stack.pop()
    elif line.split(" ")[0].isnumeric():
        print(line)
        folders[current].append(line.split(' ')[0])
    elif line.split(" ")[0] == "dir":
        folders[current].append(line.split(" ")[1])
        folders[line.split(" ")[1]] = []
    elif line.split(" ")[1] == "cd":
        stack.append(current)
        current = line.split(' ')[2]

    return current, folders, stack


def count_condition(folders):
    valid_folders = {k: v for k, v in folders.items() if v <= 100000}
    print(f"Valid folders: {valid_folders}")
    return sum(valid_folders.values())


def day_07(input_name):
    current = []
    folders = {"/": []}
    stack = []
    with open(input_name) as f:
        lines = f.readlines()
    for line in lines:
        current, folders, stack = process_line_redux(line=line.strip(), current=current, stack=stack, folders=folders)
    folders_numbers = {}
    for i in folders:
        folders_numbers[i] = recursive_dict_value(folders, i)
    print(folders_numbers)
    return count_condition(folders_numbers)


if __name__ == '__main__':
    print(f"Running main")
    res = day_07(input_name="day07_input.txt")
    print(res)

def ingest_message(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
    return lines


def process_line(line):
    preprocessed = line.split(" ")
    return check_safe(preprocessed)


def check_safe(preprocessed):
    asc = False
    desc = False
    safe = True
    for i in range(1, len(preprocessed)):
        dif = int(preprocessed[i - 1]) - int(preprocessed[i])
        if dif > 3:
            safe = False
            break
        elif dif > 0:
            asc = True
        elif dif == 0:
            safe = False
            break
        elif dif > -4:
            desc = True
        else:
            safe = False
            break
    if (asc and desc) or not safe:
        return 0
    else:
        return 1


def process_line_part_2(line):
    preprocessed = line.split(" ")
    already_safe = check_safe(preprocessed)
    if already_safe == 1:
        return 1
    for i in range(len(preprocessed)):
        new_list = list(preprocessed)
        del new_list[i]
        if check_safe(new_list) == 1:
            return 1
    return 0


def day_02(input_name):
    lines = ingest_message(input_name=input_name)
    total = 0
    for line in lines:
        total += process_line(line)
    return total


def day_02_part_2(input_name):
    lines = ingest_message(input_name=input_name)
    total = 0
    for line in lines:
        total += process_line_part_2(line)
    return total


if __name__ == '__main__':
    print("Running main")
    result = day_02_part_2(input_name="day02_input.txt")
    print(result)

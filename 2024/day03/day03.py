import re

def ingest_message(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
    return lines

def evaluate(elem):
    print(elem)
    x, y = elem[0], elem[1]
    if int(x) > 999 or int(y) > 999:
        return 0
    return int(x) * int(y)

def day_03(input_name):
    lines = ingest_message(input_name=input_name)
    total = 0
    for line in lines:
        x = re.findall(r"mul\(([0-9]+?),([0-9]+?)\)", line)
        print(x)
        for elem in x:
            total += evaluate(elem)
    return total

def substring_after(s, delim):
    return s.partition(delim)[2]

def day_03_part2(input_name):
    lines = ingest_message(input_name=input_name)
    total = 0
    long_line = "do()"
    for line in lines:
        long_line += line
    sep_by_donts = long_line.split("don't()")
    print(sep_by_donts)
    for line in sep_by_donts:
        after_do =substring_after(line, "do()")
        print(after_do)
        x = re.findall(r"mul\(([0-9]+?),([0-9]+?)\)", after_do)
        print(x)
        for elem in x:
            total += evaluate(elem)
    return total


if __name__ == '__main__':
    print("Running main")
    result = day_03_part2(input_name="day03_input.txt")
    print(result)

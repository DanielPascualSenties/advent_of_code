def ingest_message(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
    return lines

def process_line(left, right, line):
    preprocessed = line.split(" ")
    first = int(preprocessed[0])
    second = int(preprocessed[3])
    left.append(first)
    right.append(second)
    return left, right

def get_difference(left, right):
    total = 0
    for index in range(len(left)):
        difference = left[index] - right[index]
        if difference < 0:
            difference = 0 - difference
        total += difference
    return total

def get_similarity(left, right):
    total = 0
    for element in left:
        ocurrences = right.count(element)
        score = element * ocurrences
        total += score
    return total

def day_01(input_name):
    lines = ingest_message(input_name=input_name)
    left = []
    right = []
    for line in lines:
        left, right = process_line(left, right, line)
    left.sort()
    right.sort()
    res = get_difference(left, right)
    return res

def day_01_part_2(input_name):
    lines = ingest_message(input_name=input_name)
    left = []
    right = []
    for line in lines:
        left, right = process_line(left, right, line)
    res = get_similarity(left, right)
    return res



if __name__ == '__main__':
    print("Running main")
    result = day_01_part_2(input_name="day01_input.txt")
    print(result)

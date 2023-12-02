
def ingest_message(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
    return lines


def get_calibration_value(line):
    digits = [x for x in line if x.isdigit()]
    value = int(digits[0] + digits[-1])
    return value


def get_calibration_value_part2(line):
    dictionary = {"one": "on1e",
                  "two": "tw2o",
                  "three": "th3ree",
                  "four": "fo4ur",
                  "five": "fi5ve",
                  "six": "s6ix",
                  "seven": "se7ven",
                  "eight": "eig8ht",
                  "nine": "ni9ne"}
    for k in dictionary:
        line = line.replace(k, dictionary[k])
    digits = [x for x in line if x.isdigit()]
    print(digits)
    value = int(digits[0] + digits[-1])
    return value


def day_01(input_name):
    lines = ingest_message(input_name=input_name)
    total = 0
    for line in lines:
        total += get_calibration_value(line)
        print(get_calibration_value(line))
    return total


def day_01_part2(input_name):
    lines = ingest_message(input_name=input_name)
    total = 0
    for line in lines:
        total += get_calibration_value_part2(line)
    return total

if __name__ == '__main__':
    print("Running main")
    message = day_01_part2(input_name="day01_input.txt")
    print(message)

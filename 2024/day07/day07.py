def ingest_message(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
    return lines

def evaluate_part_2(equation):
    elements = equation.split(" ")
    target = int(elements[0].replace(":", ""))
    possible_results = [int(elements[1])]
    for i in elements[2:]:
        new_values = []
        for elem in possible_results:
            clean = int(str(i).replace("\n", ""))
            new_values.append(int(elem) + int(clean))
            new_values.append(int(elem) * int(clean))
            new_values.append(int(str(elem)+str(clean)))
        possible_results = new_values
    print(possible_results)
    if target in possible_results:
        print(f"Match! {target} in {possible_results}")
        return target
    return 0


def evaluate(equation):
    elements = equation.split(" ")
    print(elements)
    target = int(elements[0].replace(":", ""))
    possible_results = [int(elements[1])]
    print(possible_results)
    for i in elements[2:]:
        new_values = []
        for elem in possible_results:
            new_values.append(int(i) + int(elem))
            new_values.append(int(i) * int(elem))
        possible_results = new_values
    print(possible_results)
    if target in possible_results:
        print(f"Match! {target} in {possible_results}")
        return target
    return 0


def day_07(input_name):
    equations = ingest_message(input_name=input_name)
    total = 0
    for equation in equations:
        total += evaluate(equation)
        print(equation)
    return total


def day_07_part_2(input_name):
    equations = ingest_message(input_name=input_name)
    total = 0
    for equation in equations:
        total += evaluate_part_2(equation)
        print(equation)
    return total



if __name__ == '__main__':
    print("Running main")
    result = day_07_part_2(input_name="day07_input.txt")
    print(result)

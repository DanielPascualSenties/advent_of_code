def ingest_message(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
        for line in range(len(lines)):
            lines[line]=lines[line].replace("\n", "")

    return lines

def format_tokens(button_a, button_b, prize):
    button_a_x = int(button_a.split(" ")[2][2:4])
    button_a_y = int(button_a.split(" ")[3][2:4])
    button_b_x = int(button_b.split(" ")[2][2:4])
    button_b_y = int(button_b.split(" ")[3][2:4])
    prize_x = int(prize.split(" ")[1][2:-1])
    prize_y = int(prize.split(" ")[2][2:])
    print(f"Button A = {button_a_x, button_a_y}")
    print(f"Button B = {button_b_x, button_b_y}")
    print(f"Prize = {prize_x, prize_y}")

    return button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y


def calculate_tokens_nr(button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y):
    solutions = []
    for a in range(101):
        for b in range(101):
            current_x = a * button_a_x + b * button_b_x
            current_y = a * button_a_y + b * button_b_y
            if current_x == prize_x and current_y == prize_y:
                print(f"Found a solution with button a clicked {a} times and button b clicked {b} times")
                solutions.append(3 * a + b)
    print(solutions)
    if solutions == []:
        return 0
    if len(solutions)>1:
        print("Found multiple solutions")
    result = min(solutions)
    return result


def day_13(input_name):
    total = 0
    lines = ingest_message(input_name)
    arcades = len(lines) // 4
    for i in range(arcades):
        button_a = lines[i*4]
        button_b = lines[i*4 + 1]
        prize = lines[i*4 + 2]
        button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y = format_tokens(button_a, button_b, prize)
        min_tokens = calculate_tokens_nr(button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y)
        total += min_tokens

    return total


def day_13_part_2(input_name):
    total = 0
    return total


if __name__ == '__main__':
    print("Running main")
    result = day_13(input_name="day13_example_2.txt")
    print(result)

import numpy as np


def ingest_message(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
        for line in range(len(lines)):
            lines[line] = lines[line].replace("\n", "")

    return lines


def format_tokens(button_a, button_b, prize):
    button_a_x = int(button_a.split(" ")[2][2:4])
    button_a_y = int(button_a.split(" ")[3][2:4])
    button_b_x = int(button_b.split(" ")[2][2:4])
    button_b_y = int(button_b.split(" ")[3][2:4])
    prize_x = int(prize.split(" ")[1][2:-1]) + 10000000000000
    prize_y = int(prize.split(" ")[2][2:]) + 10000000000000
    print(f"Button A = {button_a_x, button_a_y}")
    print(f"Button B = {button_b_x, button_b_y}")
    print(f"Prize = {prize_x, prize_y}")

    return button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y


def calculate_tokens_nr(button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y):
    buttons_matrix = np.array([[button_a_x, button_b_x], [button_a_y, button_b_y]])
    prize_matrix = np.array([prize_x, prize_y])
    inverse = np.linalg.inv(buttons_matrix)
    solution = np.dot(inverse, prize_matrix)
    button_cost = np.array([3, 1])
    cost = np.dot(solution, button_cost)
    if np.round(solution[0]) * button_a_x + np.round(solution[1]) * button_b_x == prize_x and  np.round(solution[0]) * button_a_y + np.round(solution[1]) * button_b_y == prize_y:
        print("Solution found!")
        int_cost = np.round(cost)
        return int(int_cost)
    return 0


def day_13_part_2(input_name):
    total = 0
    lines = ingest_message(input_name)
    arcades = len(lines) // 4
    for i in range(arcades):
        button_a = lines[i * 4]
        button_b = lines[i * 4 + 1]
        prize = lines[i * 4 + 2]
        button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y = format_tokens(button_a, button_b, prize)
        min_tokens = calculate_tokens_nr(button_a_x, button_a_y, button_b_x, button_b_y, prize_x, prize_y)
        total += min_tokens

    return total


if __name__ == '__main__':
    print("Running main")
    result = day_13_part_2(input_name="day13_input.txt")
    print(result)

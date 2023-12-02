"""
DAY 12
"""
from copy import copy


def read_board(input_file):
    """
    :param input_file: name of the input file
    :return: two matrixes (the heights as numbers, and visited as booleans) and the coordinates of the start location
    """
    board = []
    visited = []
    initial = (-1, -1)
    with open(input_file, encoding='utf8') as file:
        lines = file.readlines()
    for line in lines:
        row = [*line.strip()]
        row_numeric = []
        row_visited = []

        for location in row:
            if location == 'S':
                initial = (len(board), len(row_numeric))
                row_numeric.append(0)
                row_visited.append(True)
            elif location == 'E':
                row_numeric.append(27)
                row_visited.append(False)
            else:
                num = ord(location) - 96
                row_numeric.append(num)
                row_visited.append(False)
        board.append(row_numeric)
        visited.append(row_visited)
    return board, visited, initial


def is_valid(board, visited, to_validate):
    """
    :param board: the board
    :param visited: the visited positions
    :param to_validate: position to be validated
    :return: True if the postion is valid
    """
    if to_validate[0] < 0 or to_validate[1] < 0:
        return False
    if to_validate[0] >= len(board) or to_validate[1] >= len(board[0]):
        return False
    if visited[to_validate[0]][to_validate[1]]:
        return False
    return True


def possible_moves(board, visited, current):
    """
    :param board: The board
    :param visited: Visited locations
    :param current: Current positions
    :return: A list of possible next steps
    """
    valid_moves = []
    if is_valid(board, visited, to_validate=(current[0]+1, current[1])):
        if board[current[0] + 1][current[1]] - board[current[0]][current[1]] <= 1:
            valid_moves.append((current[0]+1, current[1]))
    if is_valid(board, visited, to_validate=(current[0]-1, current[1])):
        if board[current[0] - 1][current[1]] - board[current[0]][current[1]] <= 1:
            valid_moves.append((current[0]-1, current[1]))
    if is_valid(board, visited, to_validate=(current[0], current[1]+1)):
        if board[current[0]][current[1] + 1] - board[current[0]][current[1]] <= 1:
            valid_moves.append((current[0], current[1]+1))
    if is_valid(board, visited, to_validate=(current[0], current[1]-1)):
        if board[current[0]][current[1] - 1] - board[current[0]][current[1]] <= 1:
            valid_moves.append((current[0], current[1]-1))
    return valid_moves


def find_route(board, visited, current, count):
    """
    :param count: how deep have we gone so far
    :param board: The board
    :param visited: Visited locations
    :param current: coordinates for the current location
    :return: boolean for the solution, visited matrix for the solution
    """
    visited_to_pass = copy(visited)
    visited_to_pass[current[0]][current[1]] = True
    if board[current[0]][current[1]] == 27:
        print("We have found the solution!!!")
        print(visited_to_pass)
        return count
    next_moves = possible_moves(board, visited_to_pass, current)
    solutions = [100000]
    for move in next_moves:
        solution = find_route(board, visited_to_pass, move, count + 1)
        solutions.append(solution)
    return min(solutions)


def day12(input_file):
    """
    :param input_file: name of the input file
    :return: result for the exercise
    """
    board, visited, initial = read_board(input_file=input_file)
    found = find_route(board, visited, initial, 0)
    return found


if __name__ == "__main__":
    print(day12("day12_example.txt"))

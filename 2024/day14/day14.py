NUM_ROWS = 103
NUM_COLUMNS = 101
SECONDS = 1
import csv


def ingest_robots(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
    return lines


def position_after_n_seconds(position_x, position_y, velocity_x, velocity_y, seconds):
    position_x = (position_x + seconds * velocity_x) % NUM_COLUMNS
    position_y = (position_y + seconds * velocity_y) % NUM_ROWS
    return position_x, position_y


def get_robot_movement(robot):
    position, velocity = robot.split(" ")
    position = position.split("=")[1]
    velocity = velocity.split("=")[1]
    position_x, position_y = position.split(",")
    velocity_x, velocity_y = velocity.split(",")
    velocity_y = velocity_y.replace("\n", "")
    return int(position_x), int(position_y), int(velocity_x), int(velocity_y)


def get_quadrant(position_x, position_y):
    horizontal_half = (NUM_ROWS - 1) // 2
    vertical_half = (NUM_COLUMNS - 1) // 2
    if position_x == vertical_half or position_y == horizontal_half:
        return 0
    if position_x < vertical_half and position_y < horizontal_half:
        return 1
    if position_x > vertical_half and position_y < horizontal_half:
        return 2
    if position_x < vertical_half and position_y > horizontal_half:
        return 3
    if position_x > vertical_half and position_y > horizontal_half:
        return 4
    raise Exception


def day_14(input_name):
    robots = ingest_robots(input_name)
    print(robots)
    quadrants = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
    for robot in robots:
        position_x, position_y, velocity_x, velocity_y = get_robot_movement(robot)
        position_x, position_y = position_after_n_seconds(position_x, position_y, velocity_x, velocity_y, SECONDS)
        quadrant = get_quadrant(position_x, position_y)
        quadrants[quadrant] += 1
        if quadrant != 0:
            print(position_x, position_y)
    print(quadrants)
    total = quadrants[1] * quadrants[2] * quadrants[3] * quadrants[4]
    return total


def day_14_part_2(input_name):
    robots = ingest_robots(input_name)

    for seconds in range(101*103):
        picture = [[0 for x in range(103)] for y in range(101)]
        for robot in robots:
            position_x, position_y, velocity_x, velocity_y = get_robot_movement(robot)
            position_x, position_y = position_after_n_seconds(position_x, position_y, velocity_x, velocity_y, seconds)
            picture[position_x][position_y] += 1
        max_ocurrences = max(map(max, picture))
        if max_ocurrences == 1:
            print(f" no overlaps in {seconds}")
            with open(f'images/picture{seconds}.txt', 'w') as f:
                csv.writer(f, delimiter=' ').writerows(picture)


if __name__ == '__main__':
    print("Running main")
    result = day_14_part_2(input_name="day14_input.txt")

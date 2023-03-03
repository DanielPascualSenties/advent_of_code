"""
DAY 4
"""


def split_into_tuples(pair_of_assignments):
    """
    :param pair_of_assignments: gets a pair of assignments
    :return: returns one and the other
    """
    assignment_a, assignment_b = pair_of_assignments.split(",")
    tuple_a = tuple(assignment_a.split("-"))
    tuple_b = tuple(assignment_b.split("-"))
    return tuple_a, tuple_b


def check_overlapping(elf1, elf2):
    """
    :param elf1: elf one
    :param elf2: elf two
    :return: true if one elf is a subset of the other
    """
    # elf 2 contains elf 1 OR elf 1 contains elf 2
    return (int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1])) or \
           (int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]))


def check_strict_overlapping(elf1, elf2):
    """
    :param elf1: elf one
    :param elf2: elf 2
    :return: true if the overlap at all
    """
    return (int(elf2[1]) >= int(elf1[0]) >= int(elf2[0])) or \
           (int(elf2[1]) >= int(elf1[1]) >= int(elf2[0])) or \
           (int(elf1[1]) >= int(elf2[0]) >= int(elf1[0])) or \
           (int(elf1[1]) >= int(elf2[1]) >= int(elf1[0]))


def day04(input_name):
    """
    :param input_name: name of the input file
    :return: the result of the exercise
    """
    total = 0
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
    for i in lines:
        elf1, elf2 = split_into_tuples(i.strip())
        if check_overlapping(elf1=elf1, elf2=elf2):
            total += 1
    return total


def day04_part2(input_name):
    """
    :param input_name: name of the input file
    :return: the result of the exercise
    """
    total = 0
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
    for i in lines:
        elf1, elf2 = split_into_tuples(i.strip())
        if check_strict_overlapping(elf1=elf1, elf2=elf2):
            total += 1
    return total


if __name__ == '__main__':
    RESULT = day04_part2("input_day04.txt")
    print(f"The final result is {RESULT}")

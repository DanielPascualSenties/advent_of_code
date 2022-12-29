"""
DAY 3
"""


def numeric_value(item):
    """
    :param item: gets a character
    :return: returns a numeric value for that character
    """
    if item.islower():
        return ord(item) - 96
    return ord(item) - 38


def split_string_half(bag):
    """
    :param bag: the list of items
    :return: a list of lists, first element is the
            first half of the bag, and same for
            the second.
    """
    length = len(bag)
    half = int(length / 2)
    first_half = bag[:half]
    second_half = bag[half:]
    return [first_half, second_half]


def find_coincidences(small_bag, big_bag):
    """
    :param small_bag: items in the small pocket
    :param big_bag: items in the big pocket
    :return: all the elemts in both bags
    """
    small_bag_list = list(small_bag)
    big_bag_list = list(big_bag)
    return set(small_bag_list).intersection(big_bag_list)


def day03(input_name):
    """
    :param input_name: name of the input file
    :return: result for the exercise
    """
    total = 0
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
    for i in lines:
        backpack = split_string_half(i.strip())
        intersection = find_coincidences(backpack[0], backpack[1])
        for item in intersection:
            total += numeric_value(item)
    return total


def day03_part2(input_name):
    """
    :param input_name: name of the input file
    :return: result of the exercise part 2
    """
    total = 0
    with open(input_name, encoding='utf8') as file:
        while True:
            line1 = file.readline().strip()
            if not line1:
                return total
            line2 = file.readline().strip()
            line3 = file.readline().strip()
            intersection = find_coincidences(find_coincidences(line1, line2), line3)
            for item in intersection:
                total += numeric_value(item)


if __name__ == '__main__':
    RESULT = day03_part2("input_day03.txt")
    print(f"The final result is {RESULT}")

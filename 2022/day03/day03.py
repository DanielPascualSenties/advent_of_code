def numeric_value(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38


def split_string_half(bag):
    length = len(bag)
    half = int(length / 2)
    first_half = bag[:half]
    second_half = bag[half:]
    return [first_half, second_half]


def find_coincidences(small_bag, big_bag):
    small_bag_list = list(small_bag)
    big_bag_list = list(big_bag)
    return set(small_bag_list).intersection(big_bag_list)


def day03(input_name):
    total = 0
    with open(input_name) as f:
        lines = f.readlines()
    for i in lines:
        backpack = split_string_half(i.strip())
        intersection = find_coincidences(backpack[0], backpack[1])
        for item in intersection:
            total += numeric_value(item)
    return total


def day03_part2(input_name):
    total = 0
    with open(input_name) as f:
        while True:
            line1 = f.readline().strip()
            if not line1:
                return total
            line2 = f.readline().strip()
            line3 = f.readline().strip()
            intersection = find_coincidences(find_coincidences(line1, line2), line3)
            for item in intersection:
                total += numeric_value(item)


if __name__ == '__main__':
    result = day03_part2("input_day03.txt")
    print(f"The final result is {result}")

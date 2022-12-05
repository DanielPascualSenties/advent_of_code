def split_into_tuples(pair_of_assignments):
    a, b = pair_of_assignments.split(",")
    tuple_a = tuple(a.split("-"))
    tuple_b = tuple(b.split("-"))
    return tuple_a, tuple_b


def check_overlapping(elf1, elf2):
    # elf 2 contains elf 1 OR elf 1 contains elf 2
    return (int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1])) or \
           (int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]))


def check_strict_overlapping(elf1, elf2):
    return (int(elf2[1]) >= int(elf1[0]) >= int(elf2[0])) or \
           (int(elf2[1]) >= int(elf1[1]) >= int(elf2[0])) or \
           (int(elf1[1]) >= int(elf2[0]) >= int(elf1[0])) or \
           (int(elf1[1]) >= int(elf2[1]) >= int(elf1[0]))


def day04(input_name):
    total = 0
    with open(input_name) as f:
        lines = f.readlines()
    for i in lines:
        elf1, elf2 = split_into_tuples(i.strip())
        if check_overlapping(elf1=elf1, elf2=elf2):
            total += 1
    return total


def day04_part2(input_name):
    total = 0
    with open(input_name) as f:
        lines = f.readlines()
    for i in lines:
        elf1, elf2 = split_into_tuples(i.strip())
        if check_strict_overlapping(elf1=elf1, elf2=elf2):
            total += 1
    return total


if __name__ == '__main__':
    result = day04_part2("input_day04.txt")
    # result = day04("day04_example.txt")
    print(f"The final result is {result}")

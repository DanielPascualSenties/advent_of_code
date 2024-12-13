SIZE = 140


def ingest_message(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
        for line in range(len(lines)):
            lines[line] = list(lines[line])
            if "\n" in lines[line]:
                lines[line].remove("\n")
    return lines


def tag_element(garden, regions, row, column, tag):
    element = garden[row][column]
    regions[row][column] = tag
    if row > 0:
        if garden[row - 1][column] == element and regions[row - 1][column] == ".":
            regions = tag_element(garden, regions, row - 1, column, tag)
    if row < SIZE - 1:
        if garden[row + 1][column] == element and regions[row + 1][column] == ".":
            regions = tag_element(garden, regions, row + 1, column, tag)
    if column > 0:
        if garden[row][column - 1] == element and regions[row][column - 1] == ".":
            regions = tag_element(garden, regions, row, column - 1, tag)
    if column < SIZE - 1:
        if garden[row][column + 1] == element and regions[row][column + 1] == ".":
            regions = tag_element(garden, regions, row, column + 1, tag)
    return regions


def tag_regions(garden):
    regions = [["." for i in range(SIZE)] for j in range(SIZE)]

    tag = 0
    for row in range(len(garden)):
        for column in range(len(garden[row])):
            if regions[row][column] == ".":
                regions = tag_element(garden, regions, row, column, tag)
                tag += 1
    return regions


def tag_regions_old(garden):
    regions = [["." for i in range(SIZE)] for j in range(SIZE)]

    counter = 0
    for row in range(len(garden)):
        for column in range(len(garden[row])):
            elem = garden[row][column]
            if row < 1 and column < 1:
                regions[row][column] = str(counter)
                counter += 1
            elif column < 1:
                if garden[row - 1][column] == elem:
                    regions[row][column] = regions[row - 1][column]
                else:
                    regions[row][column] = str(counter)
                    counter += 1
            elif row < 1:
                if garden[row][column - 1] == elem:
                    regions[row][column] = regions[row][column - 1]
                else:
                    regions[row][column] = str(counter)
                    counter += 1
            else:
                if garden[row - 1][column] == elem:
                    regions[row][column] = regions[row - 1][column]
                elif garden[row][column - 1] == elem:
                    regions[row][column] = regions[row][column - 1]
                else:
                    regions[row][column] = str(counter)
                    counter += 1

    return regions


def get_perimeter(garden, row, column):
    elem = garden[row][column]
    perimeter = 0
    if row < 1:
        perimeter += 1
    else:
        if garden[row - 1][column] != elem:
            perimeter += 1
    if row > SIZE - 2:
        perimeter += 1
    else:
        if garden[row + 1][column] != elem:
            perimeter += 1
    if column < 1:
        perimeter += 1
    else:
        if garden[row][column - 1] != elem:
            perimeter += 1
    if column > SIZE - 2:
        perimeter += 1
    else:
        if garden[row][column + 1] != elem:
            perimeter += 1
    return perimeter


def get_perimeters(garden):
    perimeters = [[0 for i in range(SIZE)] for j in range(SIZE)]
    for row in range(len(garden)):
        for column in range(len(garden[row])):
            perimeters[row][column] = get_perimeter(garden, row, column)
    return perimeters


def day_12(input_name):
    garden = ingest_message(input_name=input_name)
    print("Garden")
    print(garden)
    regions = tag_regions(garden)
    print("Regions")
    print(regions)
    perimeters = get_perimeters(garden)
    print("Perimeters")
    print(perimeters)
    region_areas = dict()
    for row in range(len(regions)):
        for column in range(len(regions[row])):
            elem = regions[row][column]
            region_areas[elem] = region_areas.get(elem, 0) + 1
    print("Region areas")
    print(region_areas)
    cost = dict()
    for row in range(len(garden)):
        for column in range(len(garden[row])):
            elem = regions[row][column]
            cost[elem] = cost.get(elem, 0) + perimeters[row][column] * region_areas[elem]
    print("Cost")
    print(cost)
    total = 0
    for key in cost:
        total += cost[key]
    return total


def day_12_part_2(input_name):
    garden = ingest_message(input_name=input_name)
    print("Garden")
    print(garden)
    regions = tag_regions(garden)
    print("Regions")
    print(regions)
    perimeters = get_perimeters(garden)
    print("Perimeters")
    print(perimeters)
    region_areas = dict()
    for row in range(len(regions)):
        for column in range(len(regions[row])):
            elem = regions[row][column]
            region_areas[elem] = region_areas.get(elem, 0) + 1
    print("Region areas")
    print(region_areas)
    cost = dict()
    for row in range(len(garden)):
        for column in range(len(garden[row])):
            elem = regions[row][column]
            cost[elem] = cost.get(elem, 0) + perimeters[row][column] * region_areas[elem]
    print("Cost")
    print(cost)
    total = 0
    for key in cost:
        total += cost[key]
    return total


if __name__ == '__main__':
    print("Running main")
    result = day_12_part_2(input_name="day12_input.txt")
    print(result)

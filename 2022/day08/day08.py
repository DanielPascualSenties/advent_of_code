import pandas as pd


def get_input(file):
    return pd.read_csv(file, header=None)


def element(location_row, location_col, dataframe):
    return int(str(dataframe.iloc[location_row][0])[location_col])


def count_trees_north(elem, location_row, location_col, dataframe):
    if location_row == 0:
        return 0
    this_tree = element(location_row - 1, location_col, dataframe)
    if this_tree >= elem:
        return 1
    else:
        return 1 + count_trees_north(elem, location_row - 1, location_col, dataframe)


def count_trees_south(elem, location_row, location_col, dataframe):
    if location_row == len(dataframe) - 1:
        return 0
    this_tree = element(location_row + 1, location_col, dataframe)
    if this_tree >= elem:
        return 1
    else:
        return 1 + count_trees_south(elem, location_row + 1, location_col, dataframe)


def count_trees_east(elem, location_row, location_col, dataframe):
    if location_col == len(str(dataframe.iloc[0][0])) - 1:
        return 0
    this_tree = element(location_row, location_col + 1, dataframe)
    if this_tree >= elem:
        return 1
    else:
        return 1 + count_trees_east(elem, location_row, location_col + 1, dataframe)



def count_trees_west(elem, location_row, location_col, dataframe):
    if location_col == 0:
        return 0
    this_tree = element(location_row, location_col - 1, dataframe)
    if this_tree >= elem:
        return 1
    else:
        return 1 + count_trees_west(elem, location_row, location_col - 1, dataframe)


def get_scenic_score(location_row, location_col, dataframe):
    elem = element(location_row, location_col, dataframe)
    north = count_trees_north(elem, location_row, location_col, dataframe)
    south = count_trees_south(elem, location_row, location_col, dataframe)
    east = count_trees_east(elem, location_row, location_col, dataframe)
    west = count_trees_west(elem, location_row, location_col, dataframe)
    return  north * south * east * west


def is_it_visible_north(elem, location_row, location_col, dataframe):
    for i in range(0, location_row):
        if element(location_row=i, location_col=location_col, dataframe=dataframe) >= elem:
            return False
    return True


def is_it_visible_south(elem, location_row, location_col, dataframe):
    for i in range(location_row + 1, len(dataframe)):
        if element(location_row=i, location_col=location_col, dataframe=dataframe) >= elem:
            return False
    return True


def is_it_visible_east(elem, location_row, location_col, dataframe):
    for i in range(location_col + 1, len(str(dataframe.iloc[0][0]))):
        tree = element(location_row=location_row, location_col=i, dataframe=dataframe)
        if tree >= elem:
            return False
    return True


def is_it_visible_west(elem, location_row, location_col, dataframe):
    for i in range(0, location_col):
        tree = element(location_row=location_row, location_col=i, dataframe=dataframe)
        if tree >= elem:
            return False
    return True


def is_it_visible(location_row, location_col, dataframe):
    elem = element(location_row=location_row, location_col=location_col, dataframe=dataframe)
    return is_it_visible_north(elem, location_row=location_row, location_col=location_col, dataframe=dataframe) or \
           is_it_visible_south(elem, location_row=location_row, location_col=location_col, dataframe=dataframe) or \
           is_it_visible_east(elem, location_row=location_row, location_col=location_col, dataframe=dataframe) or \
           is_it_visible_west(elem, location_row=location_row, location_col=location_col, dataframe=dataframe)


def day_08(input_value):
    df = get_input(input_value)
    rows = len(df)
    columns = len(str(df.iloc[0][0]))
    total = 2 * rows + 2 * columns - 4
    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            if is_it_visible(location_row=i, location_col=j, dataframe=df):
                total += 1
    return total


def day_08_part2(input_value):
    df = get_input(input_value)
    rows = len(df)
    columns = len(str(df.iloc[0][0]))
    best = 0
    for i in range(1, rows - 1):
        for j in range(1, columns - 1):
            local = get_scenic_score(location_row=i, location_col=j, dataframe=df)
            if local > best:
                best = local
    return best


if __name__ == '__main__':
    print(f"Running main")
    res = day_08_part2("day08_input.txt")
    print(res)

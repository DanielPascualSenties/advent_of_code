#Found 79701802 ways to build towel ruurbrwgrurubwrurugubgurgruurwgugwgrwuwbrww
cached_results = {}
def ingest_towels(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
    available_towels = lines[0].split(",")
    for i in range(len(available_towels)):
        available_towels[i] = available_towels[i].replace(" ", "").replace("\n", "")
    desired_towels = lines[2:]
    print(desired_towels)
    for i in range(len(desired_towels)):
        desired_towels[i] = desired_towels[i].replace("\n", "")
    return available_towels, desired_towels

def can_make(towel, available_towels):
    if len(towel) == 0:
        return 1
    elif towel in cached_results:
        return cached_results[towel]
    initial = towel[0]
    relevant_towels = [x for x in available_towels if x.startswith(initial)]
    count = 0
    for available_towel in relevant_towels:
        if towel.startswith(available_towel):
            num_rows = len(available_towel)
            new_towel = towel[num_rows:]
            posibilities = can_make(new_towel, available_towels)
            count += posibilities
            cached_results[new_towel] = posibilities

    return count

def optimize_available_towels(available_towels):
    return available_towels



def day_19_part_2(input_name):
    available_towels, desired_towels = ingest_towels(input_name)
    available_towels = optimize_available_towels(available_towels)
    total = 0
    for towel in desired_towels:
        print(f"Checking {towel}")
        options = can_make(towel, available_towels)
        print(f"Found {options} ways to build towel {towel}")
        total += can_make(towel, available_towels)
    return total


if __name__ == '__main__':
    print("Running main")
    result = day_19_part_2(input_name="day19_input.txt")
    print(result)

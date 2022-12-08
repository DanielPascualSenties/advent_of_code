def has_duplicates(chain):
    return len(chain) != len(set(chain))


def ingest_message(input_name, position=0):
    with open(input_name) as f:
        lines = f.readlines()
    return lines[position].strip()


def day_06(input_name, position, size):
    mess = ingest_message(input_name, position).strip().replace("\n", "")
    position = size
    for i in range(size, len(mess)):
        if not has_duplicates(mess[i-size: i]):
            return i


if __name__ == '__main__':
    print(f"Running main")
    message = day_06(input_name="day06_input.txt", position=0, size=14)
    print(message)

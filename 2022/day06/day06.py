"""
DAY 7
"""


def has_duplicates(chain):
    """
    :param chain: a chain of characters
    :return: true if there are duplicates
    """
    return len(chain) != len(set(chain))


def ingest_message(input_name, position=0):
    """
    :param input_name: name of the input file
    :param position: position in the input file
    :return: a message
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
    return lines[position].strip()


def day_06(input_name, position, size):
    """
    :param input_name: name of the input file
    :param position: starting position
    :param size: window size
    :return: result for the exercise
    """
    mess = ingest_message(input_name, position).strip().replace("\n", "")
    for i in range(size, len(mess)):
        if not has_duplicates(mess[i-size: i]):
            return i
    return 0


if __name__ == '__main__':
    print("Running main")
    message = day_06(input_name="day06_input.txt", position=0, size=14)
    print(message)

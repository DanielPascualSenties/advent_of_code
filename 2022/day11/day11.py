"""
DAY 11
monkey time, revenge of the apes, serial apist ft Penny
"""
from math import floor


class Monkey:
    """
    The monkey that throws your stuff around
    """
    def __init__(self, name, items, operation, test, targets, inspections = 0):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.targets = targets
        self.inspections = inspections

    def __str__(self):
        return f"{self.name} : {self.items}"

    def catch_item(self, item):
        self.items.append(item)

    def inspect_item(self, item):
        self.inspections += 1
        if self.operation[0] == 'old':
            operand_1 = item
        else:
            operand_1 = int(self.operation[0])
        if self.operation[2] == 'old':
            operand_2 = item
        else:
            operand_2 = int(self.operation[2])
        if self.operation[1] == '*':
            return floor(operand_1 * operand_2 / 3)
        return floor((operand_1 + operand_2) / 3)

    def decide_monkey(self, item):
        if item % self.test == 0:
            return int(self.targets[0])
        return int(self.targets[1])

    def monkey_turn(self, monkeys):
        while self.items:
            item = int(self.items.pop(0))
            inspected_item = self.inspect_item(item=item)
            monkey = self.decide_monkey(item=inspected_item)
            monkeys[monkey].catch_item(inspected_item)
        return monkeys


def load_monkeys(input_file):
    """
    :param input_file: name of the input file
    :return: a list of monkey objects
    """
    monkeys = []
    with open(input_file, encoding='utf8') as file:
        while True:
            targets = []
            name = file.readline()
            if not name:
                break
            clean_name = name.split("=")[0].strip()[:-1]
            items = file.readline().split(":")[1].strip().split(",")
            operation = file.readline().strip().split("=")[1].strip().split(" ")
            test = int(file.readline().split(" ")[-1])
            targets.append(file.readline().strip().split(" ")[-1])
            targets.append(file.readline().strip().split(" ")[-1])
            _ = file.readline()
            monkey = Monkey(name=clean_name, items=items, operation=operation, test=test, targets=targets)
            monkeys.append(monkey)
    return monkeys


def day11(input_file):
    """
    :param input_file: name of the input file
    :return: the result of the day
    """
    monkeys = load_monkeys(input_file)
    print("--------------")
    print("Initial State")
    print("--------------")
    for monkey in monkeys:
        print(monkey)

    turn = 1
    while turn <= 20:
        print("--------------")
        print(f"|   Turn {turn}   |")
        print("--------------")
        for monkey in monkeys:
            monkey.monkey_turn(monkeys=monkeys)
        for monkey in monkeys:
            print(monkey)
        turn += 1
    moves = []
    for monkey in monkeys:
        print(f"{monkey.name} inspected items {monkey.inspections} times")
        moves.append(monkey.inspections)
    moves.sort(reverse=True)
    return moves[0]*moves[1]


if __name__ == "__main__":
    RESULT = day11("day11_input.txt")
    print(RESULT)

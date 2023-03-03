"""
DAY 11
monkey time, revenge of the apes, serial apist ft Penny
"""
import math

class Monkey:
    def __init__(self, name, starting_items,operation, test, targets):
        self.name = name
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.targets = targets
        self.inspections = 0

    def __str__(self):
        return f"{self.name} : {self.items}"

    def catch_item(self, item):
        self.items.append(item)

    def inspect_item(self, item, module):
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
            return (operand_1 * operand_2) % module
        else:
            return (operand_1 + operand_2) % module

    def decide_monkey(self, item):
        if item % self.test == 0:
            return int(self.targets[0])
        else:
            return int(self.targets[1])

    def monkey_turn(self, monkeys, module):
        while self.items:
            item = int(self.items.pop(0))
            inspected_item = self.inspect_item(item=item, module=module)
            monkey = self.decide_monkey(item=inspected_item)
            monkeys[monkey].catch_item(inspected_item)
        return monkeys


def load_monkeys(input_file):
    monkeys = []
    with open(input_file) as file:
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
            monkey = Monkey(name=clean_name, starting_items=items, operation=operation, test=test, targets=targets)
            monkeys.append(monkey)
    return monkeys


def monkey_lcm(monkeys):
    module = 1
    for monkey in monkeys:
        if module % monkey.test == 0:
            pass
        else:
            module *= monkey.test
    return module


def day11(input_file):
    monkeys = load_monkeys(input_file)
    modules = monkey_lcm(monkeys=monkeys)
    print(modules)
    print("--------------")
    print("Initial State")
    print("--------------")
    for monkey in monkeys:
        print(monkey)

    turn = 1
    while turn <= 10000:
        for monkey in monkeys:
            monkey.monkey_turn(monkeys=monkeys, module=modules)
        turn += 1
    moves = []
    for monkey in monkeys:
        moves.append(monkey.inspections)
    moves.sort(reverse=True)
    return moves[0]*moves[1]

if __name__ == "__main__":
    RESULT = day11("day11_input.txt")
    print(RESULT)



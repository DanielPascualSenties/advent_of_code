import math

NUM_RULES = 1176
def ingest_message(input_name):
    """
    :param input_name: name of the input file
    :return: list of lines
    """
    with open(input_name, encoding='utf8') as file:
        lines = file.readlines()
    return lines

def split_rules_updates(lines):
    rules = lines[:NUM_RULES]
    updates = lines[NUM_RULES+1:]
    return rules, updates


def check_follows_rule(first, second, pages):
    if first in pages and second in pages:
        print(f"Both {first} and {second} are in {pages}")
        first_location = pages.index(first)
        second_location = pages.index(second)
        return first_location < second_location
    else:
        return True

def force_follow_rule(first, second, pages):
    modified = False
    if first in pages and second in pages:
        print(f"Both {first} and {second} are in {pages}")
        first_location = pages.index(first)
        second_location = pages.index(second)
        if first_location > second_location:
            print(f"Rule {first}|{second} broken in {pages}")
            pages[first_location]=second
            pages[second_location]=first
            print(f"Changing to {pages}")
            modified = True

    return pages, modified



def force_follow_rules(rules, pages):
    for i in range(len(pages)):
        # Converts each element to an integer
        pages[i] = int(pages[i])
    print(pages)
    one_modified = False
    for rule in rules:
        rule = rule.split(sep="|")
        first = int(rule[0])
        second = int(rule[1])
        pages, modified = force_follow_rule(first, second, pages)
        if modified:
            one_modified = True
    if one_modified:
        return force_follow_rules(rules, pages)
    return pages



def check_follows_rules(rules, pages):
    for i in range(len(pages)):
        # Converts each element to an integer
        pages[i] = int(pages[i])
    print(pages)

    for rule in rules:
        rule = rule.split(sep="|")
        first = int(rule[0])
        second = int(rule[1])
        if not check_follows_rule(first, second, pages):
            return False
    return True

def get_middle_value(rules,update):
    print(update)
    pages = update.split(sep=',')
    middle_element = 0
    if check_follows_rules(rules, pages):
        elements = len(pages)
        mid = int((elements-1) / 2)
        middle_element = int(pages[mid])
    return middle_element

def get_middle_value_part_2(rules,update):
    print(update)
    pages = update.split(sep=',')
    if not check_follows_rules(rules, pages):
        pages = force_follow_rules(rules, pages)
        elements = len(pages)
        mid = int((elements-1) / 2)
        middle_element = int(pages[mid])
        return middle_element
    return 0


def day_05(input_name):
    lines = ingest_message(input_name=input_name)
    rules, updates = split_rules_updates(lines)
    total = 0
    for update in updates:
        total += get_middle_value(rules, update)
    return total

def day_05_part_2(input_name):
    lines = ingest_message(input_name=input_name)
    rules, updates = split_rules_updates(lines)
    total = 0
    for update in updates:
        total += get_middle_value_part_2(rules, update)
    return total



if __name__ == '__main__':
    print("Running main")
    result = day_05_part_2(input_name="day05_input.txt")
    print(result)

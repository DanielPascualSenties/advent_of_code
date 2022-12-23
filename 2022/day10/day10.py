def is_relevant(n):
    return (n - 20) % 40 == 0


def generate_stack(input_file):
    stack = []
    with open(input_file) as f:
        lines = f.readlines()
    for i in lines:
        if i.strip() == "noop":
            stack.append("noop")
        else:
            stack.append("Operating")
            stack.append(i.split()[1])
    return stack


def day10(input_file):
    stack = generate_stack(input_file)
    total = 1
    cycle = 1
    relevant = 0
    for i in stack:
        if is_relevant(cycle):
            relevant += total * cycle
            print(f"At turn {cycle} we update the relevant to {relevant} by adding {total} * {cycle}")
        if i.strip() == "noop" or i.strip() == "Operating":
            pass
        else:
            total += int(i)
        cycle += 1
    return relevant

def day10_part2(input_file):
    stack = generate_stack(input_file)
    total = 1
    cycle = 1
    relevant = 0
    screen = [""]
    row = 0
    column = 0
    for i in stack:
        print(f"Start cycle {cycle}: begin executing {i}")
        print(f"During cycle {i} ")
        valid = [total - 1, total, total + 1]
        if column in valid:
            screen[row] += "#"
        else:
            screen[row] += " "
        if cycle % 40 == 0:
            row += 1
            column = -1
            screen.append("")
        if i.strip() == "noop" or i.strip() == "Operating":
            pass
        else:
            total += int(i)
        cycle += 1
        column += 1
    for i in screen:
        print(i)
    return screen



if __name__ == '__main__':
    result = day10_part2("day10_input.txt")
    print(f"The final result is {result}")

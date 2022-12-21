def pull_old(head, tail):
    if head[0] - tail[0] > 1:
        return tail[0] + 1, head[1]
    if tail[0] - head[0] > 1:
        return tail[0] - 1, head[1]
    if head[1] - tail[1] > 1:
        return head[0], tail[1] + 1
    if tail[1] - head[1] > 1:
        return head[0], tail[1] - 1
    return tail


def pull(head, tail):
    if (head[0] - tail[0] > 1) and (head[1] - tail[1] > 1):
        return tail[0] + 1, tail[1] + 1
    if (head[0] - tail[0] > 1) and (tail[1] - head[1] > 1):
        return tail[0] + 1, tail[1] - 1
    if (tail[0] - head[0] > 1) and (head[1] - tail[1] > 1):
        return tail[0] - 1, tail[1] + 1
    if (tail[0] - head[0] > 1) and (tail[1] - head[1] > 1):
        return tail[0] - 1, tail[1] - 1
    if head[0] - tail[0] > 1:
        return tail[0] + 1, head[1]
    if tail[0] - head[0] > 1:
        return tail[0] - 1, head[1]
    if head[1] - tail[1] > 1:
        return head[0], tail[1] + 1
    if tail[1] - head[1] > 1:
        return head[0], tail[1] - 1
    return tail


def move(head, tail, direction):
    if direction == 'U':
        head = (head[0] + 1, head[1])
    elif direction == 'D':
        head = (head[0] - 1, head[1])
    elif direction == 'L':
        head = (head[0], head[1] - 1)
    elif direction == 'R':
        head = (head[0], head[1] + 1)
    tail = pull(head, tail)
    return head, tail


def move_p2(head, tail, direction):
    if direction == 'U':
        head = (head[0] + 1, head[1])
    elif direction == 'D':
        head = (head[0] - 1, head[1])
    elif direction == 'L':
        head = (head[0], head[1] - 1)
    elif direction == 'R':
        head = (head[0], head[1] + 1)
    tail[0] = pull(head, tail[0])
    tail[1] = pull(tail[0], tail[1])
    tail[2] = pull(tail[1], tail[2])
    tail[3] = pull(tail[2], tail[3])
    tail[4] = pull(tail[3], tail[4])
    tail[5] = pull(tail[4], tail[5])
    tail[6] = pull(tail[5], tail[6])
    tail[7] = pull(tail[6], tail[7])
    tail[8] = pull(tail[7], tail[8])
    return head, tail


def day09(input_file):
    head = (0, 0)
    tail = (0, 0)
    visited = set()
    with open(input_file) as f:
        lines = f.readlines()
    for i in lines:
        direction = i.strip().split()[0]
        steps = int(i.strip().split()[1])
        for j in range(steps):
            head, tail = move(head=head, tail=tail, direction=direction)
            visited.add(tail)
    return len(visited)


def day09_part2(input_file):
    head = (0, 0)
    tail = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
    visited = set()
    with open(input_file) as f:
        lines = f.readlines()
    for i in lines:
        direction = i.strip().split()[0]
        steps = int(i.strip().split()[1])
        for j in range(steps):
            head, tail = move_p2(head=head, tail=tail, direction=direction)
            visited.add(tail[-1])
    return len(visited)


if __name__ == '__main__':
    result = day09_part2("day09_input.txt")
    print(f"The final result is {result}")

def update_tail(head, tail):
    dist_x = abs(head[0] - tail[0])
    dist_y = abs(head[1] - tail[1])
    assert dist_x <= 2 and dist_y <= 2, "error"

    if dist_x < 2 and dist_y < 2:
        return tail

    if dist_x == 2 and dist_y == 2:
        # ..T
        # ...
        # H..
        return ((head[0] + tail[0]) / 2, (head[1] + tail[1]) / 2)

    # ..T
    # H.T
    # ..T
    if tail[0] - head[0] == 2:
        return (head[0] + 1, head[1])
    # T..
    # T.H
    # T..
    if tail[0] - head[0] == -2:
        return (head[0] - 1, head[1])
    # .H.
    # ...
    # TTT
    if tail[1] - head[1] == 2:
        return (head[0], head[1] + 1)
    # TTT
    # ...
    # .H.
    if tail[1] - head[1] == -2:
        return (head[0], head[1] - 1)

    assert False, 'error'

def do_step(pos, dir):
    if dir == 'U':
        pos = (pos[0], pos[1] - 1)
    elif dir == 'D':
        pos = (pos[0], pos[1] + 1)
    elif dir == 'L':
        pos = (pos[0] - 1, pos[1])
    elif dir == 'R':
        pos = (pos[0] + 1, pos[1])
    return pos

with open('09.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

    visited = set()
    head = (0, 0)
    tail = (0, 0)

    for line in lines:
        dir = line.split(' ')[0]
        repeat = int(line.split(' ')[1])

        for step in range(repeat):
            head = do_step(head, dir)
            tail = update_tail(head, tail)
            visited.add(tail)

    print(f'cells = {len(visited)}')

    # part two
    visited = set()
    knots = [(0, 0) for i in range(10)]

    for line in lines:
        dir = line.split(' ')[0]
        repeat = int(line.split(' ')[1])

        for step in range(repeat):
            knots[0] = do_step(knots[0], dir)
            for k in range(1, 10):
                knots[k] = update_tail(knots[k - 1], knots[k])
            visited.add(knots[9])

    print(f'last knot cells = {len(visited)}')

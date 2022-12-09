# 179712 < x
def scenic_score(input_x, input_y):
    tree = lines[input_y][input_x]
    score = 1

    # north
    offset = 0
    for y in range(input_y - 1, -1, -1):
        offset = input_y - y
        if lines[y][input_x] >= tree:
            break
    score *= offset

    # south
    offset = 0
    for y in range(input_y + 1, h):
        offset = y - input_y
        if lines[y][input_x] >= tree:
            break
    score *= offset

    # west
    offset = 0
    for x in range(input_x - 1, -1, -1):
        offset = input_x - x
        if lines[input_y][x] >= tree:
            break
    score *= offset

    # east
    offset = 0
    for x in range(input_x + 1, w):
        offset = x - input_x
        if lines[input_y][x] >= tree:
            break
    score *= offset

    return score

with open('08.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    lines = list(map(lambda x: list(x), lines))

    w = len(lines[0])
    h = len(lines)
    for y in range(h):
        for x in range(w):
            lines[y][x] = ord(lines[y][x]) - ord('0')
    
    # border trees
    visible = w * 2 + h * 2 - 4

    visible_set = set()

    # from north
    for x in range(1, w - 1):
        local_max = lines[0][x]
        for y in range(1, h - 1):
            curr = lines[y][x]
            if curr > local_max:
                local_max = max(local_max, curr)
                visible_set.add((x, y))

    # from south
    for x in range(1, w - 1):
        local_max = lines[h - 1][x]
        for y in range(h - 2, 1, -1):
            curr = lines[y][x]
            if curr > local_max:
                local_max = max(local_max, curr)
                visible_set.add((x, y))

    # from west
    for y in range(1, h - 1):
        local_max = lines[y][0]
        for x in range(1, w - 1):
            curr = lines[y][x]
            if curr > local_max:
                local_max = max(local_max, curr)
                visible_set.add((x, y))

    # from east
    for y in range(1, h - 1):
        local_max = lines[y][w - 1]
        for x in range(w - 2, 1, -1):
            curr = lines[y][x]
            if curr > local_max:
                local_max = max(local_max, curr)
                visible_set.add((x, y))

    print(f'visible trees = {visible + len(visible_set)}')

    max_score = 0
    for y in range(h):
        for x in range(w):
            max_score = max(max_score, scenic_score(x, y))

    print(f'maximum score = {max_score}')

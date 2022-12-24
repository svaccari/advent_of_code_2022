import copy

map_input = [
    '#.####################################################################################################',
    '#>^<.v^^v>>^>vv..<><v.<^<^<v.^>>^<>>><><<>^v^>.^<>><<^vv><^<>>vv^v.<.^v><<<>.<v><<^v<v^<>.<vv<>vv<<v>#',
    '#<v<vv><^>v<><.<<^^<>^>v<^vvvv^<<v<<^.^.^>.<><^><<^v<^><<v>vv<<>>>^.^<>>>^vvv^><^v^^>>><<vvv>><<><><.#',
    '#>.vv^^^<^>v>vvv>^.<v<>...v^<>v<><<..vvv<^<<v>^>^<^v^>><^^v.v>>><^.^>vv^^v>v<^^.vv<v<v<>>^^>v>vvv^v><#',
    '#.<v>^^<^v^^<^>>^>><v>^vv>^<v<v^^<>^v><v<^<>>.v^>^.v^><vvv^.^.>vvv^.v.>.>^<^.<^>><^><v<<v>^^>><><^^^<#',
    '#<^<<v^vvv>>><>^^>>v.v.v^^>^<>><^>>^^><v>v<^.^.v<..>>>.>>.<^<^^^>.<>^^.v^>>>v>v>^^v>^><>><<.^.^>vv^^.#',
    '#<^^>^v><..v^v<^.<vv^v<.<>.<>.^v^>^^>>v^^v.<.^><>^v.^^v>v<^^vv<<^^v<>><>^<v>>^<><v^.>>>>^v.>v.><.>v>>#',
    '#<>.<<v.><^><<>>v><><>^..^v^<v>v<v.<>^<>>^v.^^>>.v^.<v>v>.v.v<>v.<.vv<<^<>^^^^>>.<vv<><<>vv>^>.v^<^>>#',
    '#<.^<vv<><v^^<^v^.<><>v>>>.<<v<<v>>v^..v<<>^>^v>>.<>>v<^>^>^<vvv<><<<..v><<<v>><v<^v^<<^vvv>^>^<v<vv<#',
    '#>^>^v>><<>>.^<>>^.^<v>^>>.<v^>v<<>vv><.v<.^^^>v<v>.v^v^.>>^^^vvvv<^<^<v>^.^<>v<^.^<>v>>vv<>>^^^>v>><#',
    '#>><^<<v<>>^<^>v>v^v><v<v><^v>v>^>^<>>^v>vv^>^v<vv^v>.<^><.vv^^^<^><..<<<>^>^.^>>>^<>.^<^>^<>^^v>v<v>#',
    '#><<><v><v^v>.v>^.<^><^^v><<<<<.^>>.^^<v>v>>^<^<>.^.>>>.>>.^v>v.<^^v^<^<>v<>^^<v^><<^^^<><v^>v>v<^.v<#',
    '#<v>.v<<><vvv^<>^^^<<v<v^v^><v.><<.^^>vvv^>^v>v><><<.v>v<<<><..>>v>>v><^^>^^.^>v.v..>^><^.<>^<<^<<v<<#',
    '#<vv<<vvv<vv>v><<.v<v<><.>^vv.^<<<<<<<v<^<^v^v>.v><vv<v^>^^^.^vv<<v>.<<><>>><^<^.^<>^>^<>v.v.v^><v<<.#',
    '#.>^.>vv<v<><vv^v.^v<.^.v<><>^^>^.>v^<><v<<><vv<<^v>^>v<>^v>v>>v<>^<v.<v^^<<v><<.^<^>.vv.>>^.vv<><v><#',
    '#>>v>>>.v<v<^^>><^^v^>>v>v^>>^<v^^^^.vv.^vv<vv><v^v<>^v<>>>>^^v>^<v<v^<>><>.v>>v..^>..<v<<>.v<<.<^>v<#',
    '#<><^>>v^<^^vv>v<v.>.v.<^v.^>vvv<^>v><^>v><><.v>>.^^>><<>.v^<<^.<.^^.<v><v.^.v<^^^^<^<^>vv<v<.v<<v<^>#',
    '#<<^^<<^vvv<<<<.^vv^.><<vv>v^><>..^.^^v>v>^^<<v>^v.v>^v><>>^v><<.v>v<>^v<v<>v<^v^.^<vv>>^>v>^><<v><.<#',
    '#<<>v.v>...^^.<<^>>.<>^^^v>^<^><v<<<><<vv^.v^>.v^.>>^<v>>^<v^^<v>>vv<<>.>>.v^v><.^v.>^>^><^^v^^v<v>^<#',
    '#<^vv^<><<<v^^<^>>v><^<<v^^v^>>^>v<>.<>>v>v<><v.>v<><<<<.<<.<<>>>><><vv><^v<<<^>v<^<^^<v^><^<..v>.vv>#',
    '#><^>>>.^.>v<^^>>vv<v><^<<v.<.>^<^<^v>vv>v^^><.^.^>>.v.>v^.>>^<>^^^>vvv>..v^vv<^v>>v<><><<<^^<<v>^^<>#',
    '#>^<vv>^v<<.<<v>^><><>>v.>.^<>^^vv<<>>>v^<>>><<v.v>>^<<vv<^vvv><><.v><.vv^v^.v.>vv^<><.v^>vv.<<<v<><<#',
    '#>v<^>>.>>v>v>><^>^>^.^>^>vv>^<<><^v.<vvv<^.><>>v>v>^<>><^>^^<>v>v>.<^v^>>>v^>vvv.>.>^<><>.v^vv><>^>>#',
    '#>><>v^>^>>^>^^>^>^<^>>vv>>>>>>vvv.v>.^v<v<vvv<<>.<^v.vv.v>^>>vv<<v^>^^^^>>^v.^v>>v<vvv<.<>^^<^v<<<.<#',
    '#<>vv<^v>v^<v>>^<<>v^>vvvv>v^><^>^v<v^^^>><^><<.^>v^vv.v<<<>..v<^<.vv>.v>^>>>^^v^v^<^v^<^^<<vv>.>.>><#',
    '#<<<v><>v.><v>><v^<^>><>^<vv><<.<<<<.v^v>v>v>.><>.<v><^.<^>^^><v>vv.<v>.v.>>.^>^>v<^vvvv>><>^^v<^>v>.#',
    '#>.^>^>.<v.v<.<>vv<v<>^v<.>^>v<^v^>.>^<^..v<>>v.v>^.v<^>>^^^<v.<>v><v.^v^.>vv<<^<v^<.^^^.^>>.v>.vv.^.#',
    '#<^v><>.<^v<v<^v<vv^^>.>v^^<v>^<.<^^<<.^>vv^^<^>v<v<^<v^^>vv^v>v^^>>..v^>.<v>v>v<v^<>^<^><.>^>>><<v.<#',
    '#>>^<vv.<<>v.<>v.^>>^^vv^<^>vv<^>v.v>>.^.v^.v<v>^<>^.>><^>v>.>>v^<^>.>>^v<<v<<^^<vvvvv><^>^>v^^^^>^v>#',
    '#<^.>^v>^<>>^.^<>.>..><>.<v^v^vv^>v^..v<<><>>^.^><^^<^^<^v<<^<^>.<><^.>^<^vv^>>>>^^>>><v<<<<^><.>^>.<#',
    '#.v<>><^^vv^<<v^v><<<v<<<v><>><>>v^>v>^^^v<<<<<<>.^v<>.^<><<^vv<^>>v.^><v>v<^v>^v><v>>v<^^>vv.^<^>.>.#',
    '#>^<.>v^^^><<v><>^.>vvv>v^<^>v><<<><><.^>>.>vv.^<<<<<^<^>^>v<^^<^<><v<.<>v<<><<v<^>>v>>>^<>>>.<<^<^<<#',
    '#>^^>.vv^><.>v<vv>^><>v><^<v.<v^>.^><v<v>v^>^<v^v>v<<v^^<^>.^<v<vv<.>>v>v^v.<vv^^^^><v>^<>^v^>vv>>vv>#',
    '#><>^<^^>^>v<^^<vv^<<^>v<>>v^>^v.v.v>^^><^<<<<>v>vv<v>^^<v>>.v<><<^><^^<<>>>>^>v>^>><><^>v><^^><v^^>>#',
    '#><<<v<v><>^vv.^<>^>><v>vv^v^v<<v.v<v^>>vvvv^v<^<v^.><^^v><><v<^^<>><<>v^vv<^>v><>><<<^>>^^<^>><>v<v<#',
    '#>^v><>v<>>^v>^<v^<vv><>^^>>>>v><v^v^>>>v<^<<<<<v<^<>>v><^<<^^^<^<>v<>^<v><^.>>><<^v.<>v^^.>>^^.^>^v<#',
    '####################################################################################################.#'
]

map_input_example = [
    '#.######',
    '#>>.<^<#',
    '#.<..<<#',
    '#>v.><>#',
    '#<^v^^>#',
    '######.#',
]

w = len(map_input[0])
h = len(map_input)

map_current = {}
for y in range(1, h - 1):
    for x in range(1, w - 1):
        c = map_input[y][x]
        if c == '.':
            continue
        map_current[(x, y)] = [c]

def add_to_map(input, k, v):
    if not k in input.keys():
        input[k] = [v]
    else:
        input[k].append(v)

def wind(map_current):
    new_map = {}
    for k in map_current.keys():
        x = k[0]
        y = k[1]
        v = map_current[k]
        for dir in v:
            if dir == '^':
                if y == 1:
                    add_to_map(new_map, (x, h - 2), dir)
                else:
                    add_to_map(new_map, (x, y - 1), dir)

            if dir == 'v':
                if y == h - 2:
                    add_to_map(new_map, (x, 1), dir)
                else:
                    add_to_map(new_map, (x, y + 1), dir)

            if dir == '<':
                if x == 1:
                    add_to_map(new_map, (w - 2, y), dir)
                else:
                    add_to_map(new_map, (x - 1, y), dir)

            if dir == '>':
                if x == w - 2:
                    add_to_map(new_map, (1, y), dir)
                else:
                    add_to_map(new_map, (x + 1, y), dir)
    return new_map

goal = (w - 2, h - 1)

def move(map_current, paths):
    new_paths = []
    for p in paths:
        next = []
        curr = p[len(p) - 1]
        x = curr[0]
        y = curr[1]
        # down
        if y < h - 2 or (y < h - 1 and x == w - 2):
            next.append((x, y + 1))
        # up
        if y > 1:
            next.append((x, y - 1))
        # left
        if x > 1 and y > 0:
            next.append((x - 1, y))
        # right
        if x < w - 2 and y > 0:
            next.append((x + 1, y))
        # sort by distance to goal, keep best
        min_dist = 9999
        for n in next:
            dist = abs(goal[0] - n[0]) + abs(goal[1] - n[1])
            min_dist = min(min_dist, dist)
        # create paths
        for n in next:
            dist = abs(goal[0] - n[0]) + abs(goal[1] - n[1])
            if dist != min_dist:
                continue
            new_path = p.copy()
            if n not in map_current and n not in new_path:
                new_path.append(n)
            if not new_path in new_paths:
                new_paths.append(new_path)

    return new_paths

paths = [[(1, 0)]]
step_count = 1
while True:
    map_current = wind(map_current)
    step_count += 1
    print(f'number of steps = {step_count}...')
    paths = move(map_current, paths)
    stop = False
    for p in paths:
        if goal in p:
            stop = True
            break
    if stop:
        break

print(f'number of steps = {step_count}')
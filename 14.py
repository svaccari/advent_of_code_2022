rock = {''}

with open('14.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

def parse_input():
    maxy = 0
    for line in lines:
        tokens = line.split(' -> ')
        first = None
        for token in tokens:
            x = int(token.split(',')[0])
            y = int(token.split(',')[1])
            maxy = max(maxy, y)
            if first is None:
                first = (x, y)
                continue
            if x == first[0]:
                yy = first[1]
                for it in range(min(y, yy), max(y, yy) + 1):
                    rock.add((x, it))
            elif y == first[1]:
                xx = first[0]
                for it in range(min(x, xx), max(x, xx) + 1):
                    rock.add((it, y))
            else:
                assert False
            first = (x, y)

    return maxy

def step():
    sand = [500, 0]
    abyss = 100000
    while abyss > 0:
        down = sand[1] + 1
        if (sand[0], down) not in rock:
            # down
            sand[1] += 1
        elif (sand[0] - 1, down) not in rock:
            # down/left
            sand[0] -= 1
            sand[1] += 1
        elif (sand[0] + 1, down) not in rock:
            # down/right
            sand[0] += 1
            sand[1] += 1
        else:
            rock.add((sand[0], sand[1]))
            break
        abyss -= 1

    if abyss == 0:
        return "abyss"

    return None

def step_part_two(maxy):
    sand = [500, 0]
    last = (0, 0)
    while True:
        down = sand[1] + 1
        if (sand[0], down) not in rock and down < maxy:
            # down
            sand[1] += 1
        elif (sand[0] - 1, down) not in rock and down < maxy:
            # down/left
            sand[0] -= 1
            sand[1] += 1
        elif (sand[0] + 1, down) not in rock and down < maxy:
            # down/right
            sand[0] += 1
            sand[1] += 1
        else:
            last = (sand[0], sand[1])
            rock.add(last)
            break

    if last == (500, 0):
        return "stop"

    return None

rock = {''}
parse_input()

units_of_sand = 0
while step() != "abyss":
    units_of_sand += 1

print(f'units_of_sand = {units_of_sand}')

rock = {''}
maxy = parse_input()

units_of_sand = 0
while step_part_two(maxy + 2) != "stop":
    units_of_sand += 1

print(f'units_of_sand part two = {units_of_sand + 1}')
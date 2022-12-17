import datetime

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def merge_intervals(list):
    list = sorted(list)
    index = 0
    while index < len(list) - 1:
        a = list[index]
        b = list[index + 1]
        if b[0] > a[1] + 1:
            index += 1
            continue
        # merge
        list[index] = (a[0], max(a[1], b[1]))
        list.pop(index + 1)
    return list


input = [
    (1943362, 12808, 1861152, -42022),
    (906633, 3319637, 2096195, 3402757),
    (2358896, 2158796, 2331052, 2934800),
    (1787606, 3963631, 2096195, 3402757),
    (2282542, 3116014, 2331052, 2934800),
    (173912, 1873897, 429790, 2000000),
    (3391153, 3437167, 3720655, 3880705),
    (3834843, 2463103, 2971569, 2563051),
    (3917316, 3981011, 3720655, 3880705),
    (1466100, 1389028, 429790, 2000000),
    (226600, 3967233, 85598, 4102832),
    (1757926, 2834180, 2331052, 2934800),
    (2176953, 3240563, 2096195, 3402757),
    (2883909, 2533883, 2971569, 2563051),
    (376161, 2533578, 429790, 2000000),
    (3015271, 3913673, 3720655, 3880705),
    (490678, 388548, 429790, 2000000),
    (2725765, 2852933, 2331052, 2934800),
    (86373, 2839828, 429790, 2000000),
    (1802070, 14830, 1861152, -42022),
    (19628, 1589839, 429790, 2000000),
    (2713787, 3381887, 2096195, 3402757),
    (2148471, 3729393, 2096195, 3402757),
    (3999318, 3263346, 3720655, 3880705),
    (575700, 1390576, 429790, 2000000),
    (273266, 2050976, 429790, 2000000),
    (3008012, 993590, 2971569, 2563051),
    (3306379, 2782128, 2971569, 2563051),
    (44975, 3820788, 85598, 4102832),
    (2941700, 2536797, 2971569, 2563051),
    (2040164, 102115, 1861152, -42022),
    (3928008, 3692684, 3720655, 3880705),
    (3905950, 222812, 4759853, -796703)
]

row = 2_000_000

example_input = [
    (2, 18, -2, 15),
    (9, 16, 10, 16),
    (13, 2, 15, 3),
    (12, 14, 10, 16),
    (10, 20, 10, 16),
    (14, 17, 10, 16),
    (8, 7, 2, 10),
    (2, 0, 2, 10),
    (0, 11, 2, 10),
    (20, 14, 25, 17),
    (17, 20, 21, 22),
    (16, 7, 15, 3),
    (14, 3, 15, 3),
    (20, 1, 15, 3)
]

example_row = 10

excluded = set()

# part one

for pair in input:
    sensor = (pair[0], pair[1])
    beacon = (pair[2], pair[3])
    max_distance = manhattan_distance(sensor, beacon)
    for x in range(pair[0] - max_distance, pair[0] + max_distance):
        curr = (x, row)
        if manhattan_distance((pair[0], pair[1]), curr) <= max_distance:
            excluded.add(curr)

for pair in input:
    beacon = (pair[2], pair[3])
    if beacon in excluded:
        excluded.remove(beacon)

print(f'excluded = {len(excluded)}')

# part two

excluded = {}

for pair in input:
    sensor = (pair[0], pair[1])
    beacon = (pair[2], pair[3])
    print('calculating', datetime.datetime.now().isoformat(), sensor, beacon)
    max_distance = manhattan_distance(sensor, beacon)
    for y in range(sensor[1] - max_distance, sensor[1] + max_distance + 1):
        if y not in excluded.keys():
            excluded[y] = []
        y_distance = abs(y - sensor[1])
        excluded[y].append((pair[0] - (max_distance - y_distance), pair[0] + (max_distance - y_distance)))

for k in excluded.keys():
    if k < 0 or k > 4_000_000:
        continue
    excluded[k] = merge_intervals(excluded[k])
    if len(excluded[k]) > 1:
        print('found:', k, excluded[k])
        # found: 3042458 [(-894242, 3012820), (3012822, 4674452)]
        # tuning frequency = {x * 4000000 + y} = 3012821 * 4000000 + 3042458
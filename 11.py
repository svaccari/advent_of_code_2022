items = [
    [74, 73, 57, 77, 74],
    [99, 77, 79],
    [64, 67, 50, 96, 89, 82, 82],
    [88],
    [80, 66, 98, 83, 70, 63, 57, 66],
    [81, 93, 90, 61, 62, 64],
    [69, 97, 88, 93],
    [59, 80],
    # [79, 98], [54, 65, 75, 74], [79, 60, 97], [74] # example
]

divider = 1
total_rounds = 10000

class Monkey:
    def __init__(self, index, operation, test):
        self.index = index
        self.operation = operation
        self.test = test
        self.inspected = 0

    def turn(self):
        while len(items[self.index]) != 0:
            item = items[self.index].pop(0)
            item = self.operation(item)
            item = item // divider
            item %= (17 * 13 * 19 * 11 * 5 * 7 * 3 * 2)
            new_monkey = self.test(item)
            items[new_monkey].append(item)
            self.inspected += 1

monkeys = [
    Monkey(0, lambda item: item * 11, lambda item: 6 if item % 19 == 0 else 7),
    Monkey(1, lambda item: item +  8, lambda item: 6 if item %  2 == 0 else 0),
    Monkey(2, lambda item: item +  1, lambda item: 5 if item %  3 == 0 else 3),
    Monkey(3, lambda item: item *  7, lambda item: 5 if item % 17 == 0 else 4),
    Monkey(4, lambda item: item +  4, lambda item: 0 if item % 13 == 0 else 1),
    Monkey(5, lambda item: item +  7, lambda item: 1 if item %  7 == 0 else 4),
    Monkey(6, lambda item: item * item, lambda item: 7 if item % 5 == 0 else 2),
    Monkey(7, lambda item: item +  6 , lambda item: 2 if item % 11 == 0 else 3),
    # Monkey(0, lambda item: item * 19, lambda item: 2 if item % 23 == 0 else 3),
    # Monkey(1, lambda item: item +  6, lambda item: 2 if item % 19 == 0 else 0),
    # Monkey(2, lambda item: item * item, lambda item: 1 if item % 13 == 0 else 3),
    # Monkey(3, lambda item: item + 3, lambda item: 0 if item % 17 == 0 else 1)
]

for round in range(total_rounds):
    if round % 100 == 0:
        print(round)
    for monkey in monkeys:
        monkey.turn()

for monkey in monkeys:
    print(f'inspected = {monkey.inspected}')

# part 1
# inspected = 163
# inspected = 258
# inspected = 51
# inspected = 247
# inspected = 271
# inspected = 22
# inspected = 105
# inspected = 229
# 271 * 258 = 69918

# part 2
# inspected = 80160
# inspected = 139887
# inspected = 99585
# inspected = 139923
# inspected = 119975
# inspected = 19972
# inspected = 99605
# inspected = 40344
# 139887 * 139923 = 19573408701

########## example

# Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1




########## input

# Monkey 0:
#   Starting items: [74, 73, 57, 77, 74]
#   Operation: new = old * 11
#   Test: divisible by 19
#     If true: throw to monkey 6
#     If false: throw to monkey 7

# Monkey 1:
#   Starting items: [99, 77, 79]
#   Operation: new = old + 8
#   Test: divisible by 2
#     If true: throw to monkey 6
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: [64, 67, 50, 96, 89, 82, 82]
#   Operation: new = old + 1
#   Test: divisible by 3
#     If true: throw to monkey 5
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: [88]
#   Operation: new = old * 7
#   Test: divisible by 17
#     If true: throw to monkey 5
#     If false: throw to monkey 4

# Monkey 4:
#   Starting items: [80, 66, 98, 83, 70, 63, 57, 66]
#   Operation: new = old + 4
#   Test: divisible by 13
#     If true: throw to monkey 0
#     If false: throw to monkey 1

# Monkey 5:
#   Starting items: [81, 93, 90, 61, 62, 64]
#   Operation: new = old + 7
#   Test: divisible by 7
#     If true: throw to monkey 1
#     If false: throw to monkey 4

# Monkey 6:
#   Starting items: [69, 97, 88, 93]
#   Operation: new = old * old
#   Test: divisible by 5
#     If true: throw to monkey 7
#     If false: throw to monkey 2

# Monkey 7:
#   Starting items: [59, 80]
#   Operation: new = old + 6
#   Test: divisible by 11
#     If true: throw to monkey 2
#     If false: throw to monkey 3
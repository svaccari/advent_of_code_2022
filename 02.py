# part 1
combinations = {
    'A X': 4,
    'B Y': 5,
    'C Z': 6,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
}

with open('02.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

    sum = 0
    for line in lines:
        sum += combinations[line]

    print(f"sum = {sum}")

# part 2
combinations = {
    'A X': 3,
    'B Y': 5,
    'C Z': 7,
    'A Y': 4,
    'A Z': 8,
    'B X': 1,
    'B Z': 9,
    'C X': 2,
    'C Y': 6,
}

with open('02.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

    sum = 0
    for line in lines:
        sum += combinations[line]

    print(f"sum part two = {sum}")

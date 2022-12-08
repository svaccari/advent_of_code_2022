# part 1
def get_priority(c):
    if 'a' <= c and c <= 'z':
        return ord(c) - ord('a') + 1
    return ord(c) - ord('A') + 27

with open('03.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

    sum = 0
    for s in lines:
        first_half  = s[:len(s)//2]
        second_half = s[len(s)//2:]

        first_set = set(list(first_half))
        second_set = set(list(second_half))
        for c in first_set:
            if c in second_set:
                sum += get_priority(c)

    print(f"sum = {sum}")

# part 2
with open('03.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

    sum = 0
    group = []
    for s in lines:
        group.append(s)
        if len(group) < 3:
            continue
        set1 = set(list(group[0]))
        set2 = set(list(group[1]))
        set3 = set(list(group[2]))
        group = []
        count = {}
        for c in set1:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        for c in set2:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        for c in set3:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        # find the one with count == 3
        for key in count:
            if count[key] == 3:
                sum += get_priority(key)

    print(f"sum part two = {sum}")

def split(s):
    t = s.split(',')
    n12 = [int(x) for x in t[0].split('-')]
    n34 = [int(x) for x in t[1].split('-')]
    n1 = n12[0]
    n2 = n12[1]
    n3 = n34[0]
    n4 = n34[1]
    return n1, n2, n3, n4

with open('04.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

    sum = 0
    for s in lines:
        n1, n2, n3, n4 = split(s)
        if n1 <= n3 and n2 >= n4:
            sum += 1
        elif n3 <= n1 and n4 >= n2:
            sum += 1

    print(f"completely contained = {sum}")

    # part 2
    #         n1------n2
    # n3--n4              n3--n4
    sum = 0
    for s in lines:
        n1, n2, n3, n4 = split(s)
        if n4 < n1 or n3 > n2:
            sum += 1

    print(f"some overlap = {len(lines) - sum}")

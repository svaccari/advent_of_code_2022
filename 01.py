# part 1
with open('01.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

    sum = 0
    maxsum = 0
    for line in lines:
        if len(line) == 0:
            if sum > maxsum:
                maxsum = sum
            sum = 0
        else:
            sum += int(line)

    print(f"maxsum = {maxsum}")

    # part 2
    sum = [0]
    for line in lines:
        if len(line) == 0:
            sum.append(0)
        else:
            sum[len(sum) - 1] += int(line)

    sum.sort(reverse=True)
    print(f"max 3 = {sum[0]}, {sum[1]}, {sum[2]}, sum = {sum[0] + sum[1] + sum[2]}")
def part1():
    crates = [
        list('QMGCL'),
        list('RDLCTFHG'),
        list('VJFNMTWR'),
        list('JFDVQP'),
        list('NFMSLBT'),
        list('RNVHCDP'),
        list('HCT'),
        list('GSJVZNHP'),
        list('ZFHG')
    ]

    with open('05.txt', 'r') as f:
        lines = [line.strip().split(' ') for line in f.readlines()]

        for tokens in lines:
            mv = int(tokens[0])
            fr = int(tokens[1]) - 1
            to = int(tokens[2]) - 1

            for i in range(mv):
                crates[to].append(crates[fr].pop())

        for c in crates:
            print(c[-1])

        # VCTFTJQCG

def part2():
    crates = [
        'QMGCL',
        'RDLCTFHG',
        'VJFNMTWR',
        'JFDVQP',
        'NFMSLBT',
        'RNVHCDP',
        'HCT',
        'GSJVZNHP',
        'ZFHG'
    ]

    with open('05.txt', 'r') as f:
        lines = [line.strip().split(' ') for line in f.readlines()]

        for tokens in lines:
            mv = int(tokens[0])
            fr = int(tokens[1]) - 1
            to = int(tokens[2]) - 1

            cut = crates[fr][-mv:]
            crates[fr] = crates[fr][:-mv]
            crates[to] += cut

        for c in crates:
            print(c[-1])

        # GCFGLDNJZ

part1()
print('---')
part2()
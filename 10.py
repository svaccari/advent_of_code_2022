with open('10.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

    for i in range(100):
        lines.append('noop')

    X = 1
    cycle = 1
    pipeline = []
    total = 0
    screen = ''

    for line in lines:
        pipeline.append(0)
        if line.startswith('add'):
            addx = int(line.split(' ')[1])
            pipeline.append(addx)
        X += pipeline.pop(0)
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            total += cycle * X

        cursor = (cycle - 1) % 40
        if X - 1 <= cursor and cursor <= X + 1:
            screen += '#'
        else:
            screen += '.'
        if cursor == 39:
            screen += '\n'

    print(f'total = {total}')
    print(screen) # EFGERURE

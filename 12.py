class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

    def __eq__(self, other):
        return self.position == other.position

def get_next(data, current, visited):
    curr_height = ord(data[current.position[1]][current.position[0]])

    up =    Node(current, (current.position[0]    , current.position[1] - 1))
    down =  Node(current, (current.position[0]    , current.position[1] + 1))
    left =  Node(current, (current.position[0] - 1, current.position[1]))
    right = Node(current, (current.position[0] + 1, current.position[1]))

    h = len(data)
    w = len(data[0])
    next = []
    if 0 <= up.position[1] and up.position[1] < h and up not in visited and ord(data[up.position[1]][up.position[0]]) - curr_height <= 1:
        next.append(up)
    if 0 <= down.position[1] and down.position[1] < h and down not in visited and ord(data[down.position[1]][down.position[0]]) - curr_height <= 1:
        next.append(down)
    if 0 <= left.position[0] and left.position[0] < w and left not in visited and ord(data[left.position[1]][left.position[0]]) - curr_height <= 1:
        next.append(left)
    if 0 <= right.position[0] and right.position[0] < w and right not in visited and ord(data[right.position[1]][right.position[0]]) - curr_height <= 1:
        next.append(right)
    return next

with open('12.txt', 'r') as f:
    lines = [list(line.strip()) for line in f.readlines()]

    h = len(lines)
    w = len(lines[0])
    for y in range(h):
        for x in range(w):
            if lines[y][x] == 'S':
                start = (x, y)
            if lines[y][x] == 'E':
                end = (x, y)

    # Fix height
    lines[start[1]][start[0]] = 'a'
    lines[end[1]][end[0]] = 'z'

    lowest = []
    for y in range(h):
        for x in range(w):
            if lines[y][x] == 'a':
                lowest.append((x, y))

    for low in lowest:
        # Create start and end node
        start_node = Node(None, low)
        end_node = Node(None, end)

        open_list = [start_node]
        closed_list = []

        while len(open_list) > 0:
            current_node = open_list[0]
            current_index = 0

            # Found the goal
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    #print(current.position[0] + 1, current.position[1] + 1, lines[current.position[1]][current.position[0]])
                    path.append(current.position)
                    current = current.parent
                print(f'path length = {len(path) - 1}') # part 1 = 425, part 2 = 418

            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Generate children
            children = get_next(lines, current_node, closed_list)

            for c in children:
                if c in closed_list:
                    children = children

            # Loop through children
            for child in children:
                if child in open_list:
                    continue

                # Add the child to the open list
                open_list.append(child)

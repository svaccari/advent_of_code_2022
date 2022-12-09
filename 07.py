
dirstack = []
folders = {
    "/": []
}

def get_dir_hash(dir=None):
    if dir is None:
        return ','.join(dirstack)
    return ','.join(dirstack) + ',' + dir

with open('07.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()

        if line.startswith('$ ls'):
            continue

        if line == '$ cd ..':
            dirstack.pop()
            continue

        if line.startswith('$ cd '):
            dirstack.append(line[5:])
            continue

        if line.startswith('dir '):
            folders[get_dir_hash(line.split(' ')[1])] = []

        if line[0].isdigit():
            folders[get_dir_hash()].append(int(line.split(' ')[0]))

# sum folder contents
folder_sum = {}
for folder in folders:
    total = sum(folders[folder])
    for f in folders:
        if f == folder:
            continue
        if f.startswith(folder):
            total += sum(folders[f])
    folder_sum[folder] = total

# sum folders < 100000
total = 0
for k in folder_sum:
    if folder_sum[k] < 100000:
        total += folder_sum[k]

print(f'total < 100000 = {total}')

# part 2
free_space = 70000000 - folder_sum['/']
space_needed = 30000000 - free_space

for v in sorted(folder_sum.values()):
    if v >= space_needed:
        print(f'folder to delete = {v}')
        break
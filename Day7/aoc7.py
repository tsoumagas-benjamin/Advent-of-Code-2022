# Count directories of size <= 100000 and sum these values
# TODO: Give size from subdirectories
# Consider directory as a stack

def create_path(l):
    return '/'.join(l).replace("//", "/")

dir_space = {}
pwd = []
part1 = 0
total_space = 70000000

file = open('aoc7.txt', 'r')

for line in file:
    line = line.strip()
    if line.startswith('$ cd '):
        if line[5:] == "..":
            pwd.pop()
        else:
            pwd.append(line[5:])
        dir_space.setdefault(create_path(pwd), 0)
    elif line.startswith('$ ls') or line.startswith('dir'):
        continue
    else:
        size, file = line.split(' ')
        dir_space[create_path(pwd)] += int(size)
    
for item in dir_space:
    for item2 in dir_space:
        if item != item2 and item2.startswith(item):
            dir_space[item] += dir_space[item2]
    if dir_space[item] <= 100000:
        part1 += dir_space[item]

print(part1)

used_space = dir_space['/']
free_space = total_space - used_space
trim_space = 30000000 - free_space

threshold = {k:v for (k, v) in dir_space.items() if v > trim_space}

key_min = min(threshold.keys(), key=(lambda k: threshold[k]))

print(threshold[key_min])
# stack1 = ['B', 'W', 'N']
# stack2 = ['L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B']
# stack3 = ['Q', 'H', 'Z', 'W', 'R']
# stack4 = ['W', 'D', 'V', 'J', 'Z', 'R']
# stack5 = ['S', 'H', 'M', 'B']
# stack6 = ['L', 'G', 'N', 'J', 'H', 'V', 'P', 'B']
# stack7 = ['J', 'Q', 'Z', 'F', 'H', 'D', 'L', 'S']
# stack8 = ['W', 'S', 'F', 'J', 'G', 'Q', 'B']
# stack9 = ['Z', 'W', 'M', 'S', 'C', 'D', 'J']

stacks = [
    ['B', 'W', 'N'],
    ['L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B'],
    ['Q', 'H', 'Z', 'W', 'R'],
    ['W', 'D', 'V', 'J', 'Z', 'R'],
    ['S', 'H', 'M', 'B'],
    ['L', 'G', 'N', 'J', 'H', 'V', 'P', 'B'],
    ['J', 'Q', 'Z', 'F', 'H', 'D', 'L', 'S'],
    ['W', 'S', 'F', 'J', 'G', 'Q', 'B'],
    ['Z', 'W', 'M', 'S', 'C', 'D', 'J'],
]

file = open('aoc5.txt', 'r')

# Part 1

# for line in file:
#     if line.startswith('move'):
#         line = line[5:]
#         line = line.replace(' from ', ',')
#         line = line.replace(' to ', ',')
#         line = list(map(int, line.strip('\n').split(',')))
#         for i in range(line[0]):
#             stacks[line[2]-1].append(stacks[line[1]-1].pop())

# Part 2

for line in file:
    if line.startswith('move'):
        line = line[5:]
        line = line.replace(' from ', ',')
        line = line.replace(' to ', ',')
        line = list(map(int, line.strip('\n').split(',')))
        temp = []
        for i in range(line[0]):
            temp.append(stacks[line[1]-1].pop())
        temp.reverse()
        stacks[line[2]-1].extend(temp)

for x in stacks:
    print(x)
        
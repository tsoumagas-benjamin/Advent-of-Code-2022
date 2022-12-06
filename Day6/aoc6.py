from collections import Counter

def is_unique(str):
    return (len(Counter(str)) == len(str))

def get_value(str, end):
    start = 0
    while not is_unique(str[start:end]):
        start += 1
        end += 1
    else:
        print(end)

file = open('aoc6.txt', 'r')

# Part 1

# for line in file:
#     line = line.strip()
#     get_value(line, 4)

# Part 2

for line in file:
    line = line.strip()
    get_value(line, 14)

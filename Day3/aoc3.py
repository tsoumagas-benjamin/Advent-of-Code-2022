# Each line is a rucksack
# Compartments are first and last half

def rucksack_split(rucksack):
    first = rucksack[:len(rucksack)//2]
    second = rucksack[len(rucksack)//2:]
    return first, second

def get_priority(comp1, comp2):
    item = list(set(comp1).intersection(set(comp2)))[0]
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96
    
def group_compare(g1, g2, g3):
    g1, g2, g3 = set(g1), set(g2), set(g3)
    item = list(set.intersection(g1, g2, g3))[0]
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96

file = open("aoc3.txt", "r")

priority_sum = 0

# Part 1

# for line in file:
#     first, second = rucksack_split(line)
#     priority_sum += get_priority(first, second)

# Part 2

members = []

for line in file: 
    line = line.strip()
    members.append(line)
    if len(members) == 3:
        priority_sum += group_compare(members[0], members[1], members[2])
        print(members)
        members = []

print(priority_sum)
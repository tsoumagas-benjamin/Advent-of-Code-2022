# Each line is a pair of elves
# Each range is the section they must clean
# See how many times one elves' section is contained by their partners'

file = open("aoc4.txt", "r")

overlaps = 0

# Part 1

# for line in file:
#     elf1, elf2 = line.split(",")
#     elf1min, elf1max = elf1.split("-")
#     elf2min, elf2max = elf2.split("-")
#     elf1min, elf1max = int(elf1min), int(elf1max)
#     elf2min, elf2max = int(elf2min), int(elf2max)
#     if elf2min >= elf1min and elf2max <= elf1max:
#         overlaps += 1
#     elif elf1min >= elf2min and elf1max <= elf2max:
#         overlaps += 1

# Part 2

for line in file:
    elf1, elf2 = line.split(",")
    elf1min, elf1max = elf1.split("-")
    elf2min, elf2max = elf2.split("-")
    elf1min, elf1max = int(elf1min), int(elf1max)
    elf2min, elf2max = int(elf2min), int(elf2max)
    if max(elf1min, elf2min) <= min(elf1max, elf2max):
        overlaps += 1

print(overlaps)
file = open("aoc1input.txt", "r")
# Part 1
current_max = 0
current = 0
# for line in file:
#     if line != "\n":
#         current += int(line)
#     else:
#         if current > current_max:
#             current_max = current
#         current = 0
# print(current_max)

# Part 2
top_three = [0, 0, 0]
for line in file:
    if line != "\n":
        current += int(line)
    else:
        top_three.append(current)
        top_three = sorted(top_three, reverse=True)[:3]
        current = 0
print(sum(top_three))
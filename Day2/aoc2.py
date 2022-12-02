# A = Rock, B = Paper, C = Scissors
# X = Rock, Y = Paper, Z = Scissors
# 1pt Rock, 2pt Paper, 3pt Scissors
# 0pt loss, 3pt draw, 6pt win

file = open("aoc2.txt", "r")

matchups = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3,
    }

score = 0

# Part 1
# for line in file:
#     if line[2] == "X":
#         score += 1
#     if line[2] == "Y":
#         score += 2
#     if line[2] == "Z":
#         score += 3
#     score += matchups[line[0:3]]

# print(score)

# Part 2    

outcomes = {
    "A X": 3,
    "A Y": 1,
    "A Z": 2,
    "B X": 1,
    "B Y": 2,
    "B Z": 3,
    "C X": 2,
    "C Y": 3,
    "C Z": 1,
    }

for line in file:
    if line[2] == "X":
        score += 0
    if line[2] == "Y":
        score += 3
    if line[2] == "Z":
        score += 6
    score += outcomes[line[0:3]]

print(score)
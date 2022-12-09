import numpy as np

file = open('aoc8.txt', 'r')

def distance(line, tree):
    i = 0
    for i, x in enumerate(line, 1):
        if x >= tree:
            break
    return i

rows = []
visible_trees = 0
score = 0

for line in file:
    rows.append(list(map(int, line.strip())))

grid = np.array(rows)

# Part 1
for row, col in np.ndindex(grid.shape):
    if row == 0 or row == len(rows) - 1 or col == 0 or col == len(rows) - 1:
        visible_trees += 1
    elif all(grid[row, col] > grid[row, :col]):
        visible_trees += 1
    elif all(grid[row, col] > grid[row, col + 1:]):
        visible_trees += 1
    elif all(grid[row, col] > grid[row + 1:, col]):
        visible_trees += 1
    elif all(grid[row, col] > grid[:row, col]):
        visible_trees += 1
    # Part 2
    score = max((distance(reversed(grid[row, :col]), grid[row, col]) *
            distance(grid[row, col + 1:], grid[row, col]) * 
            distance(reversed(grid[:row, col]), grid[row, col]) * 
            distance(grid[row + 1:, col], grid[row, col])), score)

print(visible_trees)

print(score)
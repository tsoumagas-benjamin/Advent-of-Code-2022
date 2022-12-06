file = open('signals.txt', 'r')

signals = [
    "", "", "", "", "", "", "", ""
]

for line in file:
    line = line.strip()
    for x in range(len(line)):
        signals[x] += line[x]

# Part 1

# for signal in signals:
#     print(max(set(signal), key=signal.count))

# Part 2

for signal in signals:
    print(min(set(signal), key=signal.count))
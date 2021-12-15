import sys

prev_depth = -1
n_increases = -1


readings = []

for line in sys.stdin:
    sline = line.strip()
    reading = int(sline, base=2)

    for i in range(len(sline)):
        if i >= len(readings):
            readings.append(0)
        readings[i] += 1 if reading & 1 == 1 else -1
        reading >>= 1

    print(readings)

gamma = 0
epsilon = 0

for i in reversed(readings):
    gamma   <<= 1
    epsilon <<= 1
    gamma   |= 1 if i > 0 else 0
    epsilon |= 0 if i > 0 else 1

print(f'gamma: {gamma:b}, epsilon: {epsilon:b}')
print(f'{gamma*epsilon}')
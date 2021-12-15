import sys

prev_depth = -1
n_increases = -1

for line in sys.stdin:
    depth = int(line)
    state = ''
    if depth > prev_depth:
        n_increases += 1
        state = 'increased'
    else:
        state = 'decreased'
    prev_depth = depth
    print(f'{depth} ({state})')

print(f'Total increases: {n_increases}')

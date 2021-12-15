import sys

class Buffer:
    data = []
    sum = 0

    def __init__(self, size = 3) -> None:
        self.data = [0] * size
        self.size = size
        self.ptr = 0

    def put(self, number):
        prev = self.data[self.ptr]
        self.sum -= prev
        self.sum += number
        self.data[self.ptr] = number
        self.ptr = (self.ptr + 1) % self.size


prev_depth = -1
n_increases = 0
lines_read = 0
avg_window = 3

buf = Buffer(avg_window)

for line in sys.stdin:    
    depth = int(line)
    buf.put(depth)
    lines_read += 1
    if lines_read <= avg_window:
        print(f'{depth} (ignored)')
        continue

    state = ''
    if buf.sum > prev_depth:
        n_increases += 1
        state = 'increased'
    else:
        state = 'decreased'
    prev_depth = buf.sum
    print(f'{depth} ({prev_depth}) ({state})')

print(f'Total increases: {n_increases}')

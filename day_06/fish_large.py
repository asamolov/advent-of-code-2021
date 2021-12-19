import sys


if __name__ == "__main__":
    input = []

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            input = f.read().splitlines()

    line = input.pop(0)
    p0 = list(map(int, line.strip().split(',')))

    print(f'initial state: {p0}')

    # optimization idea is to store just count of fishes of each age
    p1 = [0] * 9 # max 0-8 days
    for f in p0:
        p1[f] += 1

    print(f'initial state: {p1}')

    for i in range(256):
        new = p1[0]
        for k in range(1, 9):
            p1[k-1] = p1[k]

        p1[6] += new
        p1[8] = new
        if i < 7:
            print(f'After {i+1} days: {p1}')

    print(f'total fishes: {sum(p1)}')

import sys


if __name__ == "__main__":
    input = []

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            input = f.read().splitlines()

    line = input.pop(0)
    p0 = list(map(int, line.strip().split(',')))

    print(f'initial state: {p0}')
    for i in range(80):
        gen_size = len(p0)
        for k in range(gen_size):
            if p0[k] == 0:
                p0[k] = 6    # reset age
                p0.append(8) # new fish
            else:
                p0[k] -= 1

        if i < 5:
            print(f'After {i+1} days: {p0}')

    print(f'total fishes: {len(p0)}')

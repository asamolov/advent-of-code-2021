import sys

def calc_fuel_spent(histo, pos):
    fuel = 0
    for crab, n in histo.items():
        fuel += abs(crab - pos)*n

    return fuel

def calc_fuel_spent_on_dist(histo, pos):
    fuel = 0
    for crab, n in histo.items():
        len = abs(crab - pos)
        spent_fuel = len*(len + 1)/2 # sum of all ints from 1 till len
        fuel += spent_fuel*n

    return fuel


if __name__ == "__main__":
    input = []

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            input = f.read().splitlines()

    line = input.pop(0)
    crabs = list(map(int, line.strip().split(',')))

    histo = {}

    for crab in crabs:
        val = histo.setdefault(crab, 0)
        histo[crab] = val + 1

    max_crab = max(list(histo))        

    print(f'histo: {histo.items()}')
    print(f'max_crab: {max_crab}')

    # calc iter
    prev_fuel = sys.maxsize
    optimal_position = -1
    for i in range(max_crab + 1):
        fuel = calc_fuel_spent(histo, i)
        if fuel > prev_fuel:
            optimal_position = i - 1
            break
        else:
            prev_fuel = fuel

    
    print(f'optimal_position: {optimal_position}, spent fuel: {prev_fuel}')

    # calc iter
    prev_fuel = sys.maxsize
    optimal_position = -1
    for i in range(max_crab + 1):
        fuel = calc_fuel_spent_on_dist(histo, i)
        if fuel > prev_fuel:
            optimal_position = i - 1
            break
        else:
            prev_fuel = fuel
    print(f'CORRECT optimal_position: {optimal_position}, spent fuel: {prev_fuel}')


    

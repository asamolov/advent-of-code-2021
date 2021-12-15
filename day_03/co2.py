import sys

readings = []

def step_oxy(readings, pos):
    ones = []
    zeroes = []

    if len(readings) == 1:
        return readings[0]

    for r in readings:
        if r[pos] == '1':
            ones.append(r)
        else:
            zeroes.append(r)

    if len(ones) >= len(zeroes):
        return step_oxy(ones, pos + 1)
    else:
        return step_oxy(zeroes, pos + 1)

def step_co2(readings, pos):
    ones = []
    zeroes = []

    if len(readings) == 1:
        return readings[0]

    for r in readings:
        if r[pos] == '1':
            ones.append(r)
        else:
            zeroes.append(r)

    if len(ones) >= len(zeroes):
        return step_co2(zeroes, pos + 1)
    else:
        return step_co2(ones, pos + 1)

for line in sys.stdin:
    sline = line.strip()
    readings.append(sline)

oxy = step_oxy(readings, 0)
co2 = step_co2(readings, 0)

print(f'oxy: {oxy}, co2: {co2}')
print(f'{int(oxy, 2) * int(co2, 2)}')

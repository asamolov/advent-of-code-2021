import sys


class Cmd:
    def parse(line):
        cols = line.split()
        if len(cols) != 2:
            raise ValueError(f'Cannot parse "{line}" to command')

        op = cols[0]
        delta = int(cols[1])

        if op == 'forward':
            return Cmd(delta, 0, line)
        if op == 'down':
            return Cmd(0, delta, line)
        if op == 'up':
            return Cmd(0, -delta, line)
        else:
            raise ValueError(f'Unknown operand: "{line}", failed to parse')

    def __init__(self, dx, dAim, raw = 'unknown') -> None:
        self.dx = dx
        self.dAim = dAim
        self.raw = raw

    def __str__(self) -> str:
        return f"C{self.__dict__}"

class Submarine:

    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.aim = 0

    def move(self, cmd):
        self.aim += cmd.dAim
        self.x += cmd.dx
        self.y += cmd.dx * self.aim

    def __str__(self) -> str:
        return f"S{self.__dict__}"

sub = Submarine()

print(sub)

for line in sys.stdin:
    cmd = Cmd.parse(line.strip())
    sub.move(cmd)
    print(f'{sub} <= {cmd}')

print(f'Final: {sub}, result: {sub.x * sub.y}')

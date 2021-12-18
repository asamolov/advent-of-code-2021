import sys
import re
import matplotlib.pyplot as plt
import numpy as np

class Line:
    # 0,9 -> 5,9
    p = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')

    def __repr__(self) -> str:
        return f"L{self.__dict__}"

    def __init__(self, str) -> None:
        match = self.p.match(str)
        if match == None:
            raise ValueError(f'Cannot parse "{str}" as {self.p.pattern}')

        self.start = (int(match.group(1)), int(match.group(2)))
        self.end = (int(match.group(3)), int(match.group(4)))

    def straight(self):
        (x0, y0) = self.start
        (x1, y1) = self.end
        return x0 == x1 or y0 == y1

    def diag(self):
        (x0, y0) = self.start
        (x1, y1) = self.end
        return abs(x0 - x1) == abs(y0 - y1)

    def plot(self, arr):
        def plot(x, y):
            arr[x, y] += 1

        def plotLineLow(x0, y0, x1, y1):
            dx = x1 - x0
            dy = y1 - y0
            yi = 1
            if dy < 0:
                yi = -1
                dy = -dy
                
            D = (2 * dy) - dx
            y = y0

            for x in range(x0, x1 + 1):
                plot(x, y)
                if D > 0:
                    y = y + yi
                    D = D + (2 * (dy - dx))
                else:
                    D = D + 2*dy

        def plotLineHigh(x0, y0, x1, y1):
            dx = x1 - x0
            dy = y1 - y0
            xi = 1
            if dx < 0:
                xi = -1
                dx = -dx
                
            D = (2 * dx) - dy
            x = x0

            for y in range(y0, y1 + 1):
                plot(x, y)
                if D > 0:
                    x = x + xi
                    D = D + (2 * (dx - dy))
                else:
                    D = D + 2*dx

        (x0, y0) = self.start
        (x1, y1) = self.end

        if abs(y1 - y0) < abs(x1 - x0):
            if x0 > x1:
                plotLineLow(x1, y1, x0, y0)
            else:
                plotLineLow(x0, y0, x1, y1)
        else:
            if y0 > y1:
                plotLineHigh(x1, y1, x0, y0)
            else:
                plotLineHigh(x0, y0, x1, y1)


def maxX(l):
    (x1, _) = l.start
    (x2, _) = l.end

    return max(x1, x2)

def maxY(l):
    (_, y1) = l.start
    (_, y2) = l.end

    return max(y1, y2)


if __name__ == "__main__":
    input = []

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            input = f.read().splitlines()

    lines = []

    for line in input:
        lines.append(Line(line))

    shape = (max(maxX(l) for l in lines) + 1, max(maxY(l) for l in lines) + 1)

    a = np.zeros(shape)
    
    for l in lines:
        if l.straight() or l.diag():
            l.plot(a)

    n_hot = 0
    for x in np.nditer(a):
        if x >= 2:
            n_hot += 1

    print(f'hot points: {n_hot}')
        
    plt.imshow(a,cmap='cool', interpolation='nearest')
    plt.colorbar()
    plt.show()

    print(lines)
    print(shape)


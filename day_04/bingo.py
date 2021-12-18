import sys

class Bingo:
    def __repr__(self) -> str:
        return f"B{self.__dict__}"

    def __init__(self, lines) -> None:
        self.size = len(lines)
        self.raw = lines
        self.rows = [[0]*self.size for i in range(self.size)]
        self.cols = [[0]*self.size for i in range(self.size)]
        self.numbers = {}
        self.won = False        

        for row in range(self.size):
            cols = lines[row].split()
            if len(cols) != self.size:
                raise ValueError(f'Bingo card is not square! Odd line: "{lines[row]}"')

            for col in range(self.size):
                v = int(cols[col])
                self.rows[row][col] = v
                self.cols[col][row] = v
                if v in self.numbers:
                    raise ValueError(f'Value [{row},{col}]={v} is non-unique! Please check the bingo card! lines: {lines}')

                self.numbers[v] = (row, col)


    def draw(self, number):
        if not self.won:
            if number in self.numbers:
                (row, col) = self.numbers.pop(number)
                self.rows[row][col] = 0
                self.cols[col][row] = 0

                if (sum(self.rows[row]) == 0 or
                    sum(self.cols[col]) == 0):
                    self.won = True
        
        return self.won


def game(draw, bingos):
    for n in draw:
        print(f'draw: {n}')
        for b in bingos:
            if b.draw(n):
                print('Bingo!')
                s = sum(list(b.numbers))
                print(f'sum remaining is: {s}')
                print(f'result: {s*n}')
                return


def game_last(draw, bingos):
    remaining_bingos = bingos
    won = {}
    last_won = ()
    for n in draw:
        print(f'draw: {n}')
        for b in remaining_bingos:
            if b.draw(n):
                s = sum(list(b.numbers))
                won[b] = s*n
                last_won = (b, s*n)

        remaining_bingos = [b for b in remaining_bingos if b not in won]        
    
    print(f'last won: {last_won}')

# header - draw line

if __name__ == "__main__":
    input = []

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            input = f.read().splitlines()

    draw_line = input.pop(0)

    draw = list(map(int, draw_line.strip().split(',')))
    lines = [] 
    bingos = []


    for line in input:
        if len(line.strip()) == 0:
            if len(lines) !=0:
                bingos.append(Bingo(lines))
                lines = []
        else:
            lines.append(line)

    if len(lines) !=0:
        bingos.append(Bingo(lines))

    print(f'draw: {draw}')
    print(f'bingos: {bingos}')

    game(draw, bingos)
    game_last(draw, bingos)


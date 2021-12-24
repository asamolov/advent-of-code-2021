import sys

class Cmd:
    op = None

    def __init__(self, *args) -> None:
        if self.op != args[0]:
            raise AssertionError(f'op {args[0]} does not match {self.op}')

    def __repr__(self) -> str:
        return f"{self.op} {self.__dict__}"
        
    def execute(self, regfile, input):
        pass

class Inp(Cmd):
    op = 'inp'
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.a = args[1]

    def execute(self, regfile, input):
        regfile[self.a] = int(next(input))

class Add(Cmd):
    op = 'add'
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.a = args[1]
        self.b = args[2]

    def execute(self, regfile, input):
        if type(self.b) == int:
            val = self.b
        else:
            val = regfile[self.b]

        regfile[self.a] = self.a + val

class Mul(Cmd):
    op = 'mul'
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.a = args[1]
        self.b = args[2]

    def execute(self, regfile, input):
        if type(self.b) == int:
            val = self.b
        else:
            val = regfile[self.b]

        regfile[self.a] = self.a * val

class Div(Cmd):
    op = 'div'
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.a = args[1]
        self.b = args[2]

    def execute(self, regfile, input):
        if type(self.b) == int:
            val = self.b
        else:
            val = regfile[self.b]

        regfile[self.a] = self.a / val

class Mod(Cmd):
    op = 'mod'
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.a = args[1]
        self.b = args[2]

    def execute(self, regfile, input):
        if type(self.b) == int:
            val = self.b
        else:
            val = regfile[self.b]

        regfile[self.a] = self.a % val

class Eql(Cmd):
    op = 'eql'
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.a = args[1]
        self.b = args[2]

    def execute(self, regfile, input):
        if type(self.b) == int:
            val = self.b
        else:
            val = regfile[self.b]

        if self.a == val:
            regfile[self.a] = 1
        else:
            regfile[self.a] = 0

class CmdParser:

    def __init__(self) -> None:
        self.ops = {cls.op : cls for cls in Cmd.__subclasses__()}
        

    def parse(self, line):
        cols = line.split()
        if len(cols) < 2:
            raise ValueError(f'Cannot parse "{line}" to command')
        op = cols[0]

        return self.ops[op](*cols)

if __name__ == "__main__":
    input = []

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            input = f.read().splitlines()

    parser = CmdParser()

    cmds = []
    for line in input:
        cmds.append(parser.parse(line))

    print(cmds)

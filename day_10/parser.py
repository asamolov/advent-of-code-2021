import sys
import math

class NavParser:
    closing = {')', ']', '}', '>'}
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }

    def is_pair(self, o, c):
        return    ((o == '(' and c == ')')
                or (o == '[' and c == ']')
                or (o == '{' and c == '}')
                or (o == '<' and c == '>'))

    def is_closing(self, ch):
        return ch in NavParser.closing

    def __repr__(self) -> str:
        return f"P{self.__dict__}"

    def __init__(self, line) -> None:
        stack = []
        
        #self.raw = line
        self.corrupted = False
        self.where = -1
        self.bogus_ch = None
        self.score = 0
        for idx, ch in enumerate(line):
            if self.is_closing(ch):
                # check can pop
                top = stack.pop()
                if not self.is_pair(top, ch):
                    self.where = idx
                    self.corrupted = True
                    self.bogus_ch = ch                    
                    self.score = self.points[self.bogus_ch]
                    break
            else:
                stack.append(ch)

        self.is_complete = len(stack) == 0

        self.completion_score = 0
        while stack:
            ch = stack.pop()
            self.completion_score = self.completion_score * 5 + self.points[ch]
        
if __name__ == "__main__":
    input = []

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            input = f.read().splitlines()

    score = 0
    completion_scores = []
    for idx, line in enumerate(input):
        p = NavParser(line)
        print(f'Line {idx+1}: {p}')
        score += p.score
        if not p.corrupted:
            completion_scores.append(p.completion_score)

    completion_scores.sort()
    completion_score = completion_scores[math.floor(len(completion_scores) / 2)]
    print(f'Total score: {score}')
    print(f'Middle completion score: {completion_score}')

import sys


if __name__ == "__main__":
    input = []

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            input = f.read().splitlines()


    total = 0
    for line in input:
        parts = line.split('|')
        out = parts[1]

        for digit in out.split():
            len_digit = len(digit)
            if (len_digit == 2      # 1
                or len_digit == 3   # 7
                or len_digit == 4   # 4
                or len_digit == 7   # 8
                ):
                total += 1


    print(f'answer: {total}')

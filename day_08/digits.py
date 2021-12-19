import sys
from typing import List


#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

def decoder(coded: List):
    # to set      

    decoded = {}

    one = set()
    four = set()
    seven = set()
    eight = set()

    not_decoded = set()

    for coded_d in coded:
        coded_set = frozenset(coded_d)
        if len(coded_set) == 2:      # 1
            one = coded_set
            decoded[coded_set] = 1
        elif len(coded_set) == 3:      # 7
            seven = coded_set
            decoded[coded_set] = 7
        elif len(coded_set) == 4:      # 4
            four = coded_set
            decoded[coded_set] = 4
        elif len(coded_set) == 7:      # 8
            eight = coded_set
            decoded[coded_set] = 8
        else:
            not_decoded.add(coded_set)
            decoded[coded_set] = -1

    b_d = four - seven # segments b & d, in 4 but not in 7

    # with b_d: 5, 6, 9 len(9, 6) == 6, len(5) == 5
    five = set()
    with_b_d = [x for x in not_decoded if x.issuperset(b_d)]
    for d in with_b_d:
        if len(d) == 5:
            five = d
            not_decoded.remove(five)
            decoded[five] = 5
        else:
            if d.issuperset(one):
                nine = d
                not_decoded.remove(nine)
                decoded[nine] = 9
            else:
                six = d
                not_decoded.remove(six)
                decoded[six] = 6

    # 7 is not fully in 2
    for d in not_decoded:
        if not d.issuperset(seven):
            decoded[d] = 2
        elif len(d) == 5:
            decoded[d] = 3
        elif len(d) == 6:
            decoded[d] = 0
    return decoded


if __name__ == "__main__":
    input = []

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            input = f.read().splitlines()


    total = 0
    for line in input:
        parts = line.split('|')
        coded = parts[0].split()
        out = parts[1].split()

        code = decoder(coded)

        number = 0
        for d in out:
            digit = code[frozenset(d)]
            number = number * 10 + digit

        print(f'{out}: {number}')
        total += number

    print(f'answer: {total}')

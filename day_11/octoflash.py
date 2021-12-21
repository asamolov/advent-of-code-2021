import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def bump_cell(data, row, col, flashed, activated):
    data[row][col] += 1
    if data[row][col] > 9 and (row, col) not in flashed:
        activated.add((row, col))

def bump_nearby(data, row, col, flashed, activated):
    max_row = len(data)
    max_col = len(data[row])
    if row > 0:
        if col > 0:
            bump_cell(data, row - 1, col - 1, flashed, activated)

        bump_cell(data, row - 1, col, flashed, activated)

        if col < max_col - 1:
            bump_cell(data, row - 1, col + 1, flashed, activated)

    if col > 0:
        bump_cell(data, row, col - 1, flashed, activated)

    if col < max_col - 1:
        bump_cell(data, row, col + 1, flashed, activated)

    if row < max_row - 1:
        if col > 0:
            bump_cell(data, row + 1, col - 1, flashed, activated)

        bump_cell(data, row + 1, col, flashed, activated)

        if col < max_col - 1:
            bump_cell(data, row + 1, col + 1, flashed, activated)


if __name__ == "__main__":
    input = []

    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            input = f.read().splitlines()

    shape = (len(input[0]), len(input))

    arr = []
    for idx, line in enumerate(input):
        num_line = [int(x) for x in list(line)]
        arr.append(num_line)
        print(f'{num_line}')

    fig, ax = plt.subplots()

    ims = []
    total_flashes = 0
    # show an initial one first
    #im = ax.imshow(np.array(arr),cmap='jet', interpolation='nearest', animated=True) 
    #ims.append([im])
    ax.imshow(np.array(arr)) 
    
    # iteration

    for i in range(1, 101):
        print(f'Step {i}')

        flashed = set()
        max_energy = set()
        # increase all energy level
        for row in range(len(arr)):
            for col in range(len(arr[row])):
                bump_cell(arr, row, col, flashed, max_energy)

        # flash
        while max_energy:
            max_energy_new = set()
            flashed.update(max_energy)
            for row, col in max_energy:
                bump_nearby(arr, row, col, flashed, max_energy_new)

            max_energy = max_energy_new

        # reset
        ax.cla()
        for row, col in flashed:
            ax.text(col, row, 'X',
                ha="center", va="center", color="w")
            arr[row][col] = 0

        total_flashes += len(flashed)
        
        title = f'step# {i} total flashed: {total_flashes}'
        print(title)
        print(arr)
        ax.set_title(title)
        ax.imshow(np.array(arr)) 
        plt.pause(0.2)

    plt.show()
    #    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
    #                                repeat_delay=1000)

import sys
import matplotlib.pyplot as plt
import numpy as np
import math


def is_local_min(data, row, col):
    val = data[row][col]
    # left
    if col > 0 and data[row][col - 1] <= val:
        return False
    # right
    elif col < len(data[row]) - 1 and data[row][col + 1] <= val:
        return False
    # top
    elif row > 0 and data[row - 1][col] <= val:
        return False
    # bottom
    elif row < len(data) - 1 and data[row + 1][col] <= val:
        return False

    return True

def basin_go_up(data, basin_map, basin_idx, row, col):
    val = data[row][col]

    # peak
    if val == 9:
        return 0
    
    # already traversed
    if basin_map[row][col] > 0:
        return 0

    # mark current cell 
    basin_map[row][col] = basin_idx

    area = 1
    # left
    if col > 0 and data[row][col - 1] >= val:
        area += basin_go_up(data, basin_map, basin_idx, row, col - 1)
    # right
    if col < len(data[row]) - 1 and data[row][col + 1] >= val:
        area += basin_go_up(data, basin_map, basin_idx, row, col + 1)
    # top
    if row > 0 and data[row - 1][col] >= val:
        area += basin_go_up(data, basin_map, basin_idx, row - 1, col)
    # bottom
    if row < len(data) - 1 and data[row + 1][col] >= val:
        area += basin_go_up(data, basin_map, basin_idx, row + 1, col)

    return area


# find basin starting from current point
def find_basin_size(data, basin_map, basin_idx, basin):
    row, col = basin

    area = basin_go_up(data, basin_map, basin_idx, row, col)

    return area


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
        pass

    data = np.array(arr)    
    fig, (ax1, ax2) = plt.subplots(1, 2)
    im = ax1.imshow(data,cmap='cool', interpolation='nearest')

    total_risk = 0
    basins = []
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if is_local_min(arr, row, col):
                val = data[row, col]
                basins.append((row, col))
                total_risk += val + 1
                text = ax1.text(col, row, val,
                       ha="center", va="center", color="w")

    basin_map = [[0]*len(arr[0]) for i in range(len(arr))]
    # iterate basins
    basin_sizes = []
    for idx, basin in enumerate(basins):
        basin_sizes.append(find_basin_size(arr, basin_map, idx + 1, basin))

    im = ax2.imshow(np.array(basin_map),cmap='jet', interpolation='nearest')
    for idx, basin in enumerate(basins):
        size = basin_sizes[idx]
        row, col = basin
        text = ax2.text(col, row, size,
                ha="center", va="center", color="w")

    basin_sizes.sort(reverse=True)

    result = 0
    if len(basin_sizes) >= 3:
        top_basins = basin_sizes[0:3]
        print(f'Top 3 basins: {top_basins}')
        result = math.prod(top_basins)

    print(f'Total risk: {total_risk}')
    print(f'Result: {result}')
    ax1.set_title(f'Total risk: {total_risk}')
    ax2.set_title(f'Result: {result}')
    fig.tight_layout()
    plt.show()
    

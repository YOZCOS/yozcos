import random

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# total_accesses 3326017 max_dram_hits 2960149 cur_hits 29601553
def read_log_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split()
            total_accesses = int(parts[1])
            max_dram_hits = int(parts[3])
            yield [max_dram_hits, total_accesses - max_dram_hits]

data_generator = read_log_file('data/hit_rate.txt')

figure, ax = plt.subplots()
labels = ['DRAM hits', 'others']
colors = ['red', 'blue']

def update(num):
    ax.clear()
    ax.set_title('Accesses and Hits')
    try:
        data = next(data_generator)
    except StopIteration:
        return ax,
    bottom = 0
    for i in range(2):
        ax.bar('Accesses and Hits', data[i], color=colors[i], bottom=bottom)
        bottom += data[i]
    ax.legend(labels, loc="upper right")
    return ax,

animation = FuncAnimation(figure, update, repeat=False, save_count=10)

plt.show()

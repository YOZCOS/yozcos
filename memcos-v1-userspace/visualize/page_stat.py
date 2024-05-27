import random

import numpy as np
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Patch

# warm_threshold 4 hot_threshold 8 page_count ...
def read_log_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split()
            warm_threshold = int(parts[1])
            hot_threshold = int(parts[3])
            thresholds = [warm_threshold, hot_threshold]
            data = [int(part) for part in parts[5:]]
            labels = ['Cold' if i < warm_threshold else 'Warm' if i < hot_threshold else 'Hot' for i in range(len(data))]
            yield labels, data, thresholds

data_generator = read_log_file('data/page_stat.txt')

figure, ax = pyplot.subplots()
defined_colors = ['blue', 'orange', 'red']

def update(num):
    ax.clear()
    ax.set_title('Memory Usage: Cold, Warm, and Hot Areas')
    labels, data, thresholds = next(data_generator)
    colors = [defined_colors[0] if label == 'Cold' else defined_colors[1] if label == 'Warm' else defined_colors[2] for label in labels]
    ax.bar(range(15), data, color=colors)
    legend_labels = ['Cold', 'Warm', 'Hot']
    legend_elements = [Patch(facecolor=defined_colors[legend_labels.index(label)], label=label) for label in legend_labels]
    ax.legend(handles=legend_elements, loc='upper right')
    return ax,

animation = FuncAnimation(figure, update, frames=range(10), repeat=True)

pyplot.show()

import random
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

# hot 2205694 warm 5995488 cold 0
def read_log_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split()
            hot = int(parts[1])
            warm = int(parts[3])
            cold = int(parts[5])
            yield [hot, warm, cold]

data_generator = read_log_file('data/hotness_stat.txt')

figure, ax = pyplot.subplots()
labels = ['hot', 'warm', 'cold']
colors = ['red', 'orange', 'blue']

def update(num):
    ax.clear()
    ax.set_title('Memory Usage: Hot, Warm, and Cold Proportions')
    try:
        data = next(data_generator)
    except StopIteration:
        return ax,
    if sum(data) == 0:
        ax.text(0.5, 0.5, 'All values are zero', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
        return ax,
    print(data)
    patches, texts = ax.pie(data, colors=colors, startangle=90)
    ax.legend(patches, labels, loc="best")
    return ax,

animation = FuncAnimation(figure, update, repeat=False, save_count=10)

pyplot.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

import matplotlib
import matplotlib as mpl

df = pd.read_csv("./atom_data_pivot.csv")
array = df.to_numpy()

row_labels = array[:,:1]
row_list = row_labels.tolist()
row_list = [int(item[0]) for item in row_list]

column_labels = ["C", "CA", "CB", "H", "N"]

array = np.delete(array, [0], 1)
array = np.transpose(array)

plots = [[0,59], [59,118], [119,178], [179, 238], [239, 298], [299,351]]

# create colormap
colors = [(1, 0, 0), (1, 1, 0), (0, 1, 0)]  # rot, gelb, grün
n_bins = 100  # Anzahl der Abstufungen im Farbverlauf

# Erstelle den Farbverlauf
colormap = LinearSegmentedColormap.from_list("custom_red_green", colors, N=n_bins)

# create heatmap
fig, ax = plt.subplots(len(plots), 1)

for plot in plots:
    lower_border = plot[0]
    higher_border = plot[1]

    image = ax[plots.index(plot)].imshow(array[:,lower_border:higher_border], cmap=colormap)


    x_ticks = range(0, array[:, lower_border:higher_border].shape[1], 10)  # Alle 10. Ticks auf der x-Achse
    x_labels = row_list[lower_border:higher_border][::10]  # Wähle die Beschriftungen für jeden 10. Punkt
    ax[plots.index(plot)].set_xticks(x_ticks, labels=x_labels)
    ax[plots.index(plot)].set_yticks(range(len(column_labels)), labels=column_labels)

    ax[plots.index(plot)].set_xticks(np.arange(array[:,lower_border:higher_border].shape[1] + 1) - 0.5, minor=True)  # Minor-Ticks für x
    ax[plots.index(plot)].set_yticks(np.arange(array[:,lower_border:higher_border].shape[0] + 1) - 0.5, minor=True)  # Minor-Ticks für y

    # Aktiviere das Gitter für die Minor-Ticks
    ax[plots.index(plot)].grid(True, which='minor', color='w', linestyle='-', linewidth=1)

    ax[plots.index(plot)].tick_params(axis='x', which='minor', length=0)

#fig.colorbar(image, ax=ax, orientation='vertical', fraction=0.02, pad=0.01)
fig.tight_layout()
plt.show()



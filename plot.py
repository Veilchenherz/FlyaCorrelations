import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# sets the amount of amino acids that are shown in each line of the plot
AMINO_ACIDS_PER_LINE = 60

# read csv file that was created by the statistics.py file (contains the pivoted table)
df = pd.read_csv("./atom_data_pivot.csv")

# convert pandas dataframe to numpy array
array = df.to_numpy()

# create list of labels for the amino acid numbers (columns in the figure)
row_labels = array[:,:1]
row_list = row_labels.tolist()
row_list = [int(item[0]) for item in row_list]

# list of labels for the atom types (rows in the figure)
column_labels = ["C", "CA", "CB", "H", "N"]

array = np.delete(array, [0], 1)

#swap columns and rows to put atom types on the y-axis and amino acid numbers on the x-axis
array = np.transpose(array)

# split the array into lines that contain 60 amino acids each
number_of_amino_acids = len(row_list)
number_of_plots = int(number_of_amino_acids / AMINO_ACIDS_PER_LINE)

plots = []
index = 0

for plot in range(number_of_plots):
    new_plot = [index, index + AMINO_ACIDS_PER_LINE - 1]
    plots.append(new_plot)
    index += AMINO_ACIDS_PER_LINE

last_plot = [plots[-1][-1] + 1, number_of_amino_acids]
plots.append(last_plot)

# create colormap
colors = [(1, 0, 0), (1, 1, 0), (0, 1, 0)]  # rot, gelb, grün
n_bins = 100  # Anzahl der Abstufungen im Farbverlauf

# create colors for color bar
colormap = LinearSegmentedColormap.from_list("custom_red_green", colors, N=n_bins)

# create heatmap
fig, ax = plt.subplots(len(plots), 1)

# create plots with the set amount of amino acids
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

# colorbar overlaps with main figure if turned on, so show it separately, cut it out and place it together however you like
#fig.colorbar(image, ax=ax, orientation='vertical', fraction=0.02, pad=0.01)

fig.tight_layout()
plt.show()



from result import dictionary
import pandas

# create csv-list with assignment ratio per atom
atom_result = "residue,atom,ratio_assigned\n"

for residue in dictionary.keys():

    for atom, spectra in dictionary[residue].items():

        spectrum_numbers = []
        for spectrum in spectra:
            spectrum_numbers.append(spectrum[-1])

            ratio_assigned = round(1 - (spectrum_numbers.count(0) / len(spectrum_numbers)),2)

        atom_result += f"{residue},{atom},{ratio_assigned}\n"


# write csv file with an entry for every atom
with open("./atom_list.csv", "w") as atom_csv:
    atom_csv.write(atom_result)

# read written atom list into a pandas dataFrame
atom_data = pandas.read_csv("./atom_list.csv")

# pivot table to create columns for every atom
atom_data_pivot = atom_data.pivot(index="residue", columns="atom", values="ratio_assigned")

# replace NaN with 0
atom_data_pivot.fillna(0, inplace=True)

# write csv containing the pivoted table
atom_data_pivot_csv = atom_data_pivot.to_csv("./atom_data_pivot.csv")


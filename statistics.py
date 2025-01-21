from itertools import count
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



# with open("./atom_list.csv", "a") as atom_csv:
#     atom_csv.write(atom_result)

atom_data = pandas.rea


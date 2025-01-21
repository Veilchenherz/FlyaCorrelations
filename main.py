from functions import *

# file path of the flya.txt file (no modification needed)
input_file_path = "C:/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/FlyaCorrelations/flya_24.txt"


# clean data file
cleaned_file = clean_file(input_file_path)

# create list of heading lines with corresponding spectrum data
list = read_file(cleaned_file)

# create nested dictionary with outer keys being the residue numbers
# for every residue number there is an inner dictionary
# with the atom names (e. g. H, N) as the keys and the spectrum data as values)
dictionary = group_list(list)

#save dictionary to .py file
save_dictionary_to_file(dictionary)
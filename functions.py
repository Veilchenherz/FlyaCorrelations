# joins atom names that are accidentally split in the lists
def join_pairs(list):

    # always append the name of the spectrum as the first item
    new_list = [list[0]]

    # join the two parts of the atom name (e. g. 'H(Val', '351)' -> 'H(Val351)')
    for index in range(1, len(list) - 1, 2):
        new_list.append(list[index] + list[index + 1])

    # if there is a peak assigned in the current spectrum for the specified atom,
    # add the peak number as the last item
    if len(list) % 2 == 0:
        last_item = int(list[-1])

    # if no peak is assigned, add 0 to the list
    else:
        last_item = 0

    # append the last item to the list
    new_list.append(last_item)

    return new_list


# clean beginning and end of the flya.txt file
def clean_file(path):

    start_found = False

    # everything below the start_text and above the end_text is used
    start_text = "If expected peak has been assigned, peak ID is given."
    end_text = "Residue clashes (at least 4 atoms)"

    clean_file = []

    # open the raw data
    with open(path) as file:
        flya_file = file.readlines()

    # iterate over lines in the raw data file
    for line in flya_file:

        # if the start_text is found, the line below is the first one that is taken into account
        if start_text in line:
            start_found = True
            continue

        # stop adding lines if the end_text is found
        if end_text in line:
            break

        # add lines to cleaned list after finding the start_text
        if start_found:
            clean_file.append(line)

    return clean_file


def read_file(file):

    # split lines into lists with spaces as delimiters
    flya_file = [element.split() for element in file]

    # create result list
    new_list = []

    for list in flya_file:

        # identify heading lines (e.g. ['H', '351', 'VAL']
        if len(list) == 3:

            # define index to add spectrum data
            # start with the first line after heading
            index = flya_file.index(list) + 1

            length = 4

            # change residue number to integer
            list[1] = int(list[1])

            spectra_list = []

            # iterate over every line following the current heading
            # stop when next heading is found (which has a length of 3 again)
            while(length > 3):

                # join accidentally split names of atoms
                # this is necessary due to the splitting with spaces as delimiter
                # at the beginning of this function
                spectrum = flya_file[index]
                new_spectrum = join_pairs(spectrum)

                # append spectrum data to the list of spectra for the specified atom
                spectra_list.append(new_spectrum)

                # change to next line for the next iteration
                index += 1

                # assign length of next line to length variable if index still in the list
                if index < len(flya_file):
                    length = len(flya_file[index])

                # stop loop at the end of the file
                else:
                    break

            # append the heading line and the list with the data lines for each spectrum to the result list
            new_list.append([list, spectra_list])

    return new_list


# creates a dictionary with the residue numbers as keys and a list of the data lines for spectra as the value
def group_list(list):

    new_dictionary = {}

    # iterate over heading lines
    for item in list:

        # create key from residue number
        new_key = item[0][1]

        # check if the residue already exists
        if new_key not in new_dictionary:
            new_value = {}

            # add spectrum from the line, where the residue number appears first to the inner dictionary
            # the inner key is the atom name (e.g. H, N, CA, CB, C)
            new_value[item[0][0]] = item[1]

            # get index of the current line in the list
            index = list.index(item)

            # check if the index is still defined in the list
            # and check if the next line has the same residue number than the previous
            while index < len(list) and list[index][0][1] == new_key:

                # add the next lines spectrum data to the current residue number with the atom name as the key
                new_value[list[index][0][0]] = list[index][1]

                # change to next line in the next iteration
                index += 1

            # add the dictionary entry for the current residue to the outer dictionary
            new_dictionary[new_key] = new_value

    return new_dictionary


# save dictionary in python file
# input must be dictionary
# optional inputs are the dictionary name and the file name
def save_dictionary_to_file(dictionary, name="dictionary", file_name="result"):

    with open(f"./{file_name}.py", "w") as result_file:
        result_file.write(f"{name} = " + str(dictionary))
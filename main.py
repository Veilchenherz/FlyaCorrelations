input_file_path = "C:/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/FlyaCorrelations/flya_24 - FlyaCorrelations.txt"

def join_pairs(list):

    new_list = [list[0]]

    for index in range(1, len(list) - 1, 2):
        new_list.append(list[index] + list[index + 1])

    if len(list) % 2 == 0:
        last_item = int(list[-1])
    else:
        last_item = 0

    new_list.append(last_item)

    return new_list


def read_file():

    with open(input_file_path) as file:
        flya_file = file.readlines()

    flya_file = [item.split() for item in flya_file]

    new_dictionary = {}
    new_list = []

    for list in flya_file:
        if len(list) == 3:
            index = flya_file.index(list) + 1
            length = 4

            list[1] = int(list[1])

            spectra_list = []

            while(length > 3):

                spectrum = flya_file[index]
                new_spectrum = join_pairs(spectrum)
                spectra_list.append(new_spectrum)

                index += 1
                length = len(flya_file[index])

            #new_dictionary["".join(list)] = spectra_list
            new_list.append([list, spectra_list])

    #print(new_dictionary)
    #print(new_dictionary["N33GLY"])

    return new_list


def group_list(list):

    new_dictionary = {}

    for item in list:

        new_key = item[0][1]

        if new_key not in new_dictionary:
            new_value = {}






list = read_file()
print(list)
#group_list(list)
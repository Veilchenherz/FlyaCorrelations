input_file_path = "C:/Userdata_Laurin/Masterarbeit/p38_solidassignments_Laurin/FlyaCorrelations/flya_24 - FlyaCorrelations.txt"

def read_file ():

    with open(input_file_path) as file:
        flya_file = file.readlines()

        print(flya_file)


read_file()
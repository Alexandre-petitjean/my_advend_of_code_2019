from Utils.tools import open_file_line_by_line


def exercice_4():
    print("Exercice 4")
    filename = "jour4/jour4.txt"
    my_list = open_file_line_by_line(filename)
    result = treatment(my_list)
    print(result)


def treatment(my_list):
    result_list = []
    borne = my_list[0].split("-")
    borne_min = borne[0]
    borne_max = borne[1]
    i = int(borne_min)
    while i <= int(borne_max):
        if same_adj_digit(i) and digit_never_decrease(i):
            result_list.append(i)
        i = i + 1
    return result_list.__len__()


def same_adj_digit(i):
    result = False
    string = str(i)
    for i in range(string.__len__()):
        if i < string.__len__() - 1:
            if string[i] == string[i + 1]:
                result = True
    return result


def digit_never_decrease(i):
    result = True
    string = str(i)
    i = 1
    while i < string.__len__():
        if string[i] < string[i - 1]:
            result = False
        i = i + 1
    return result

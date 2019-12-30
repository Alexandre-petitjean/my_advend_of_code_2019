from Utils.tools import open_file_line_by_line


def exercice_4():
    print("Exercice 4")
    filename = "jour4/jour4.txt"
    my_list = open_file_line_by_line(filename)
    borne = setup(my_list)
    result = treatment(borne[0], borne[1])
    print(result)


def setup(my_list):
    borne = my_list[0].split("-")
    return borne


def treatment(borne_min, borne_max):
    result_list = []

    number = int(borne_min) + 1
    while number < int(borne_max):
        if same_adj_digit(number) and digit_never_decrease(number):
            result_list.append(number)
        number = number + 1

    return result_list.__len__()


def same_adj_digit(number):
    result = False
    string = str(number)
    i = 0
    j = 0
    while i < string.__len__():
        while j < string.__len__() and string[i] == string[j]:
            j = j + 1
        if j - i == 2:
            result = True
        i = i + j
    return result


def digit_never_decrease(number):
    result = True
    string = str(number)
    i = 1
    while i < string.__len__():
        if string[i] < string[i - 1]:
            result = False
        i = i + 1
    return result

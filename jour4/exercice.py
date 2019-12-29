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

    number = int(borne_min)
    while number <= int(borne_max):
        if same_adj_digit(number) and digit_never_decrease(number):
            result_list.append(number)
        number = number + 1

    return result_list.__len__()


def same_adj_digit(number):
    result = False
    string = str(number)
    for number in range(string.__len__()):
        if number < string.__len__() - 1:
            if string[number] == string[number + 1]:
                result = True
    return result


def digit_never_decrease(number):
    result = True
    string = str(number)
    number = 1
    while number < string.__len__():
        if string[number] < string[number - 1]:
            result = False
        number = number + 1
    return result

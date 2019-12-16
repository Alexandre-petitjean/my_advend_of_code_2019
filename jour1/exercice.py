import math

from Utils.tools import open_file_line_by_line


def exercice_1():
    print("Exercice 1")
    filename = "jour1/exo_1.txt"
    my_list = open_file_line_by_line(filename)
    # print(calculate_part_1(my_list))
    print(calculate_part_2(my_list))


def calculate_part_1(my_list):
    result = 0
    for i in my_list:
        calc = fuel_require(int(i))
        result += calc
    return result


def calculate_part_2(my_list):
    result = 0
    for i in my_list:
        calc = fuel_require(int(i))
        result += calc
        while calc > 0:
            calc = fuel_require(calc)
            result += calc
    return result


def fuel_require(i):
    calc = i / 3
    calc = math.floor(calc)
    calc = calc - 2
    if calc < 0:
        calc = 0
    return calc

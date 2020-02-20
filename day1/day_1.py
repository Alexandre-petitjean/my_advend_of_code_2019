"""
Day 1 of the Advent of code
--- The Tyranny of the Rocket Equation ---
"""
import math

from Utils.tools import open_file_line_by_line

FILENAME = "input_day_1.txt"


def main():
    """
    Main
    Start point of the day.
    """
    print("--- Day 1: The Tyranny of the Rocket Equation ---")

    my_list = open_file_line_by_line(FILENAME)
    print("Part 1 : ")
    print((calculate_part_1(my_list)))
    print("Part 2 : ")
    print((calculate_part_2(my_list)))


def calculate_part_1(my_list):
    """
    Treatment of the part 1.
    :param my_list: list of the mass of each spaceship module.
    :return: the total of the require fuel.
    """
    result = 0
    for i in my_list:
        calc = fuel_require(int(i))
        result += calc
    return result


def calculate_part_2(my_list):
    """
    Treatment of the part 1.
    :param my_list: list of the mass of each spaceship module.
    :return: the total of the require fuel.
    """
    result = 0
    for i in my_list:
        calc = fuel_require(int(i))
        result += calc
        while calc > 0:
            calc = fuel_require(calc)
            result += calc
    return result


def fuel_require(i):
    """
    Calculation of the require fuel for one module.
    :param i: The mass of a module.
    :return: The require fuel for one module.
    """
    calc = i / 3
    calc = math.floor(calc)
    calc = calc - 2
    if calc < 0:
        calc = 0
    return calc


if __name__ == "__main__":
    main()

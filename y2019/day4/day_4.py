"""
Day 4 of the avent of code.
--- Day 4: Secure Container ---
"""
from Utils.tools import open_file_line_by_line

FILENAME = "input_day_4.txt"


def main():
    """
    Main function of the file.
    """
    print("--- Day 4: Secure Container ---")
    my_list = open_file_line_by_line(FILENAME)
    bounds = setup(my_list)
    print("Part 1 : ")
    print(treatment_part1(bounds))
    print("Part 2 : ")
    print(treatment_part2(bounds))


def treatment_part1(bounds):
    """
    Treatment of the first part.
    :param bounds: the max and min number.
    :return: the result.
    """
    result_list = []
    number = int(bounds[0]) + 1
    while number < int(bounds[1]):
        if same_adj_digit_part1(number) and digit_never_decrease(number):
            result_list.append(number)
        number = number + 1

    return result_list.__len__()


def treatment_part2(bounds):
    """
    Treatment of the part 2.
    :param bounds: the max and min number.
    :return:
    """
    result_list = []
    number = int(bounds[0]) + 1
    while number < int(bounds[1]):
        if same_adj_digit_part2(number) and digit_never_decrease(number):
            result_list.append(number)
        number = number + 1

    return result_list.__len__()


def setup(my_list):
    """
    Return a array of int that represent the borne.
    :param my_list: The input.
    :return: An array.
    """
    bounds = my_list[0].split("-")
    return bounds


def same_adj_digit_part1(number):
    """
    Test if the adjacent digit are the same.
    :param number: the number to test.
    :return: True if the test is ok else return False
    """
    result = False
    string = str(number)
    i = 1
    j = 0
    while i < string.__len__():
        if string[i] == string[j]:
            result = True
        i = i + 1
        j = j + 1
    return result


def same_adj_digit_part2(number):
    """
    Test if the same digit are adjacent for the part 2.
    :param number: the number to test.
    :return: True if the test is ok else return False
    """
    result = False
    string = str(number)
    i = 1
    j = 0
    while i < string.__len__() and result is False:
        if string[i] == string[j]:
            count = 0
            while j <= string.__len__() - 1 and string[i] == string[j]:
                j += 1
                count += 1
            if count == 2:
                result = True
            i = j
        else:
            i = i + 1
            j = j + 1
    return result


def digit_never_decrease(number):
    """
    Test if the digit is decreasing in a number.
    :param number: The target number.
    :return: True if the gigit is decreasing, else return False.
    """
    result = True
    string = str(number)
    i = 1
    while i < string.__len__():
        if string[i] < string[i - 1]:
            result = False
        i = i + 1
    return result


if __name__ == "__main__":
    main()

"""
Day 2 of the Advent of code
--- Day 2: 1202 Program Alarm ---
"""
from Utils.tools import open_file_explode_array, list_str_to_int

FILENAME = "input.txt"
RESULT = 19690720

ADD = 1
MULT = 2
STOP = 99


def main():
    """
    Main function of the file.
    """
    print("--- Day 2: 1202 Program Alarm ---")
    my_list = open_file_explode_array(FILENAME)
    list_str_to_int(my_list)
    print("Part 1 : ")
    print(treatment_part_1(my_list[:]))
    print("Part 2 : ")
    print(treatment_part_2(my_list[:]))


def treatment_part_2(my_list):
    """
    Treatment for the part 2 of the day.
    :param my_list: The input list for the intcode computer.
    :return: (100 * noun) + verb
    """

    noun = 0
    my_list[1] = noun
    while noun <= 99:
        verb = 0
        my_list[2] = verb
        while verb <= 99:
            if treatment(my_list[:]) == RESULT:
                return (100 * noun) + verb
            verb = verb + 1
            my_list[2] = verb
        noun = noun + 1
        my_list[1] = noun


def treatment_part_1(my_list):
    """
    Treatment of the part 1 of the day.
    The first two elements of the entry list are exchanged by 12 and 2.
    :param my_list: The input list for the intcode computer.
    :return: the result of the intcode computer get_wires_path.
    """
    my_list[1] = 12
    my_list[2] = 2
    return treatment(my_list)


def treatment(my_list):
    """
    The intcode computer
    :param my_list: The input list.
    :return: the value of index 0 of the list my_list
    """
    i = 0
    result = 0
    while i < my_list.__len__():
        if my_list[i] == ADD:
            my_list[my_list[i + 3]] = my_list[my_list[i + 1]] + my_list[my_list[i + 2]]
        elif my_list[i] == MULT:
            my_list[my_list[i + 3]] = my_list[my_list[i + 1]] * my_list[my_list[i + 2]]
        elif my_list[i] == STOP:
            result = my_list[0]
        i = i + 4
    return result


if __name__ == "__main__":
    main()

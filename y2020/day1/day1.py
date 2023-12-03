from year_2020.tools import open_file_line_by_line, list_str_to_int


def find_sum_2020_part1(input_list):
    """
    Find the two integers whose sum is equal to y2020.
    @param input_list: The list of int.
    @return: The result of multiplying the two integers.
    """
    i = 0
    result = 0
    while i < len(input_list) and result == 0:
        j = 0
        while j < len(input_list) and result == 0:
            if input_list[i] + input_list[j] == 2020:
                result = input_list[i] * input_list[j]
            j += 1
        i += 1
    return result


def find_sum_2020_part2(input_list):
    """
    Find the three integers whose sum is equal to y2020.
    @param input_list: The list of int.
    @return: The result of multiplying the three integers.
    """
    i = 0
    result = 0
    while i < len(input_list) and result == 0:
        j = 0
        while j < len(input_list) and result == 0:
            k = 0
            while k < len(input_list) and result == 0:
                if input_list[i] + input_list[j] + input_list[k] == 2020:
                    result = input_list[i] * input_list[j] * input_list[k]
                k += 1
            j += 1
        i += 1
    return result


def main():
    print("Advent of code day 1")
    input_list = open_file_line_by_line("./input.txt")
    input_list = list(map(int, input_list))
    print("Part 1 : " + str(find_sum_2020_part1(input_list)))
    print("Part 2 : " + str(find_sum_2020_part2(input_list)))


if __name__ == '__main__':
    main()

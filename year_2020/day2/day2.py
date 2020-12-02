from year_2020.tools import open_file_line_by_line


def is_valid_part1(condition, pwd):
    mini, string = condition.split("-")
    maxi = string.split(" ")[0]
    char = condition[-1]
    result = False
    i = 0
    char_nb = 0
    while i < len(pwd):
        if pwd[i] == char:
            char_nb += 1
        i += 1
    if int(mini) <= char_nb <= int(maxi):
        result = True
    return result


def is_valid_part2(condition, pwd):
    pos1, string = condition.split("-")
    pos2 = string.split(" ")[0]
    char = condition[-1]
    result = False

    if pwd[int(pos1)] == char:
        result = True
    if pwd[int(pos2)] == char:
        if result:
            result = False
        else:
            result = True
    return result


def nb_of_valid_pwd(input_list, part):
    result = 0
    for line in input_list:
        element = line.split(":")
        if part == 1:
            if is_valid_part1(element[0], element[1]):
                result += 1
        else:
            if is_valid_part2(element[0], element[1]):
                result += 1
    return result


def main():
    print("Advent of code day 2")
    input_list = open_file_line_by_line("./input.txt")
    print("Part 1: " + str(nb_of_valid_pwd(input_list, 1)))
    print("Part 2: " + str(nb_of_valid_pwd(input_list, 2)))


if __name__ == '__main__':
    main()

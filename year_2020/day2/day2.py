from year_2020.tools import open_file_line_by_line


def is_valid_part1(condition, pwd):
    """
    Test is a password is valid followed the specified conditions.
    @param condition: "min - max char" Min and Max iteration of the char.
    @param pwd: The password to test.
    @return: A bool. True if the password is valid or False if not.
    """
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
    """
    Test is a password is valid followed the specified conditions.
    @param condition: "pos1-pos2 char" Possible position of the char, the char can only be in one position.
    @param pwd: The password to test.
    @return: A bool. True if the password is valid or False if not.
    """
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
    """
    Get the number of valid password.
    @param input_list: each element are "number-number char: string"
    @param part: 1 or 2. The part of the day.
    @return: The number of valid password
    """
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

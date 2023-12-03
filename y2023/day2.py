import re

from y2023.tools import open_file_line_by_line

MAX_VALUES = {'red': 12, 'blue': 14, 'green': 13}

def get_sum_of_possible_game(lines):
    res = 0
    for line in lines:
        game_input = re.split(';|:', line)
        game_id = game_input.pop(0).split()[-1]
        if is_game_possible(game_input):
            res += int(game_id)
    return res


def is_game_possible(cubes: list[str]):
    for cube in cubes:
        c_dict = {}
        c_entries = cube.split(',')
        for entry in c_entries:
            v, k = entry.strip().split()
            if c_dict.get(k):
                c_dict[k] += int(v)
            else:
                c_dict[k] = int(v)

        for k, v in c_dict.items():
            if v > MAX_VALUES[k]:
                return False
    return True


def calc_power(cubes: list[str]):
    c_dict = {}
    for cube in cubes:
        c_entries = cube.split(',')
        for entry in c_entries:
            v, k = entry.strip().split()
            old = c_dict.get(k)
            if old is None or old and old < int(v):
                c_dict[k] = int(v)
    power = 1
    for i in c_dict.values():
        power = power * i
    return power

def get_sum_of_power(lines):
    res = 0
    for line in lines:
        game_input = re.split(';|:', line)
        res += calc_power(game_input[1:])
    return res

def main():
    inputs = open_file_line_by_line('input.txt')
    print(get_sum_of_possible_game(inputs))
    print(get_sum_of_power(inputs))


if __name__ == '__main__':
    main()

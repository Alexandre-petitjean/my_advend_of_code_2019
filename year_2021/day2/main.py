from year_2021.tools import open_file_line_by_line


def main():
    submarine_cmds = open_file_line_by_line('input.txt')
    print(calc_location_part1(submarine_cmds))  # 1938402
    print(calc_location_part2(submarine_cmds))  # 1947878632


def calc_location_part1(submarine_cmds):
    horizontal, depth = 0, 0

    for submarine_cmd in submarine_cmds:
        value = int(submarine_cmd[-1])
        if 'forward' in submarine_cmd:
            horizontal += value
        elif 'down' in submarine_cmd:
            depth += value
        elif 'up' in submarine_cmd:
            depth -= value

    return horizontal * depth


def calc_location_part2(submarine_cmds):
    horizontal, depth, aim = 0, 0, 0

    for submarine_cmd in submarine_cmds:
        value = int(submarine_cmd[-1])
        if 'forward' in submarine_cmd:
            horizontal += value
            depth += aim * value
        elif 'down' in submarine_cmd:
            aim += value
        elif 'up' in submarine_cmd:
            aim -= value

    return horizontal * depth


if __name__ == '__main__':
    main()

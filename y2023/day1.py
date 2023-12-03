from y2023.tools import open_file_line_by_line

VALID_DIGIT = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}


def get_sum(lines):
    res = 0
    for line in lines:
        digits = [int(s) for s in line if s.isdigit()]
        res += int(f'{digits[0]}{digits[-1]}')
    return res


def get_sum_2(lines: list[str]):
    res = 0
    for line in lines:
        digits = []
        i = 0
        while i < len(line):
            if line[i].isdigit():
                digits.append(line[i])
            else:
                j = i + 1
                while j < len(line) and not line[j].isdigit() and not line[i:j] in VALID_DIGIT.values():
                    j += 1
                digit = [k for k, v in VALID_DIGIT.items() if line[i:j] == v]
                if len(digit):
                    digits.append(digit[0])
            i += 1
        res += int(f'{digits[0]}{digits[-1]}')
    return res


def main():
    inputs = open_file_line_by_line('input.txt')
    print(get_sum(inputs))
    print(get_sum_2(inputs))


if __name__ == '__main__':
    main()

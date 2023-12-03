import re

from y2023.tools import open_file_line_by_line

def get_digit_from_index(chunk: str, indexs: list[int]):
    res = []
    indices = [(match.start(), match.end()) for match in re.finditer(r'\d+', chunk)]
    for indice in indices:
        for index in indexs:
            if indice[0] <= index <= indice[1]:
                res.append(chunk[indice[0]:indice[1]])
    return res



def get_pn_in_chunk(chunk: list[str]):
    targets = [m.start() for m in re.finditer(r"[^\w\d.]", chunk[1])]

    if len(targets) > 0:
        digits = []
        for target in targets:
            for i in [0,2]:
                digits.extend(get_digit_from_index(chunk[i], [target - 1, target, target + 1]))
        print(digits)

    return 0


def get_sum_of_pn(lines: list[str]):
    res = 0
    for i in range(1, len(lines) - 1):
        res += get_pn_in_chunk(lines[i - 1:i + 2])
    return res


def main():
    inputs = open_file_line_by_line('ref.txt')
    print(get_sum_of_pn(inputs))


if __name__ == '__main__':
    main()

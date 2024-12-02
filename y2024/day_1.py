from y2024.tools import get_lines_in_file


def main() -> None:
    lines: list[str] = get_lines_in_file('./input.txt')

    left_numbers: list[int] = []
    right_numbers: list[int] = []

    for line in lines:
        left, right = line.split('   ')
        left_numbers.append(int(left))
        right_numbers.append(int(right))

    left_numbers.sort()
    right_numbers.sort()

    total = sum([abs(left_numbers[i] - right_numbers[i]) for i in range(len(left_numbers))])

    print(total)


if __name__ == '__main__':
    main()
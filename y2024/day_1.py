from y2024.tools import get_lines_in_file

def build_lists(lines: list[str]) -> tuple[list[int], list[int]]:
    """
    Function that builds two lists of integers from the lines passed as a parameter.
    The lists are sorted.
    Args:
        lines: list[str]: The lines from the input.

    Returns: tuple[list[int], list[int]]: The two lists of integers.

    """

    left_numbers, right_numbers = zip(*[(int(left), int(right)) for left, right in (line.split() for line in lines)])
    left_numbers, right_numbers = list(left_numbers), list(right_numbers)

    left_numbers.sort()
    right_numbers.sort()

    return left_numbers, right_numbers

def part_1(left_numbers: list[int], right_numbers: list[int]) -> None:
    print(sum([abs(left_numbers[i] - right_numbers[i]) for i in range(len(left_numbers))]))

def part_2(left_numbers: list[int], right_numbers: list[int]) -> None:
    print(sum([number * right_numbers.count(number) for number in left_numbers]))

def main() -> None:
    lines: list[str] = get_lines_in_file('./input.txt')
    left_numbers, right_numbers = build_lists(lines)

    part_1(left_numbers, right_numbers)
    part_2(left_numbers, right_numbers)


if __name__ == '__main__':
    main()
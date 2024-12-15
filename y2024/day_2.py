from y2024.tools import get_lines_in_file

def is_safe_report(report: list[int]) -> bool:
    is_increasing = report[0] <= report[1]

    for i in range(len(report) - 1):
        if (
                (is_increasing and report[i] >= report[i + 1] or not is_increasing and report[i] <= report[i + 1])
                or abs(report[i] - report[i + 1]) > 3):
            return False
    return True


def part_1(reports: list[str]) -> int:
    safe_report = 0

    for report in reports:
        safe_report += 1 if is_safe_report([int(level) for level in report.split()]) else 0

    return safe_report

def part_2(reports: list[str]) -> int:
    pass

def main() -> None:
    lines: list[str] = get_lines_in_file('./input.txt')

    print(part_1(lines))
    print(part_2(lines))


if __name__ == '__main__':
    main()
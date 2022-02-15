from year_2021.tools import open_file_line_by_line, list_str_to_int


def findBestPos(crabs):
    pos_max = max(crabs)
    pos_min = min(crabs)
    min_fuel = 100000000000
    for i in range(pos_min, pos_max):
        fuel_spend = 0
        for crab in crabs:
            fuel_spend += abs(crab - i)
        if min_fuel > fuel_spend:
            min_fuel = fuel_spend
    return min_fuel


def main():
    #  open file and parse list.
    crabs = open_file_line_by_line('./input.txt')
    crabs = crabs[0].split(',')
    list_str_to_int(crabs)

    print(f"Part 1 {findBestPos(crabs)} min fuel !")


if __name__ == '__main__':
    main()

from year_2021.tools import open_file_line_by_line, list_str_to_int


def findBestPosPart1(crabs):
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

# TODO optimization
def findBestPosPart2(crabs):
    pos_max = max(crabs)
    pos_min = min(crabs)
    min_fuel = 100000000000
    for i in range(pos_min, pos_max):
        fuel_spend = 0
        for crab in crabs:
            fuel = 0
            for j in range(abs(crab - i)):
                fuel += j + 1
            fuel_spend += fuel
        if min_fuel > fuel_spend:
            min_fuel = fuel_spend
    return min_fuel


def main():
    #  open file and parse list.
    crabs = open_file_line_by_line('./input.txt')
    crabs = crabs[0].split(',')
    list_str_to_int(crabs)

    print(f"Part 1 {findBestPosPart1(crabs)} min fuel !")
    print(f"Part 2 {findBestPosPart2(crabs)} min fuel !")


if __name__ == '__main__':
    main()

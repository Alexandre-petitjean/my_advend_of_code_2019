import copy

from year_2021.tools import open_file_line_by_line, list_str_to_int


def get_lantern_fish_dict(lignes):
    lantern_fish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for ligne in lignes:
        lantern_fish_dict[ligne] += 1
    return lantern_fish_dict


def spawn_lanternfish(lantern_fish_dict, day):

    for i in range(day):
        # start of day
        cmpt = lantern_fish_dict[0]
        # end of day
        for j in range(1, len(lantern_fish_dict)):
            lantern_fish_dict[j - 1] = lantern_fish_dict[j]
        lantern_fish_dict[6] += cmpt
        lantern_fish_dict[8] = cmpt

    return sum(lantern_fish_dict.values())


def main():
    lignes = open_file_line_by_line('input.txt')
    lignes = lignes[0].split(',')
    list_str_to_int(lignes)

    lantern_fish_dict = get_lantern_fish_dict(lignes)

    print(f"Part 1 : {spawn_lanternfish(copy.deepcopy(lantern_fish_dict), 80)}")
    print(f"Part 2 : {spawn_lanternfish(copy.deepcopy(lantern_fish_dict), 256)}")


def status_lantern_fish(i, lantern_fish_list):
    list_day = []
    for lantern_fish in lantern_fish_list:
        list_day.append(lantern_fish.day_until_new)
    print(f"{i} {list_day}")


if __name__ == '__main__':
    main()

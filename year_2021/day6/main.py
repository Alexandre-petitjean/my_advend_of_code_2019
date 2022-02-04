from year_2021.tools import open_file_line_by_line, list_str_to_int


class LanternFish:

    def __init__(self, day_until_new=None) -> None:
        super().__init__()
        if not day_until_new:
            day_until_new = 8
        self.day_until_new = day_until_new
        self.ready = False

    def day_pass(self):
        if self.day_until_new > 0:
            self.day_until_new -= 1
        return self.is_ready()

    def is_ready(self):
        if self.day_until_new == 0:
            if not self.ready:
                self.ready = True
                return 'W'  # Waiting for the next day.
            else:
                self.day_until_new = 6
                self.ready = False
                return 'Y'  # Yes
        return 'N'  # No

    def __str__(self) -> str:
        return self.day_until_new


def get_lantern_fish_list(lignes):
    lantern_fish_list = []

    for ligne in lignes:
        lantern_fish_list.append(LanternFish(ligne))

    return lantern_fish_list


def spawn_lanternfish(lantern_fish_list, day):
    for i in range(day):
        cmpt = 0
        for lantern_fish in lantern_fish_list:
            status = lantern_fish.day_pass()
            if status == 'Y':
                cmpt += 1
        for j in range(cmpt):
            lantern_fish_list.append(LanternFish())
        # status_lantern_fish(i + 1, lantern_fish_list)
    return len(lantern_fish_list)


def main():
    lignes = open_file_line_by_line('input.txt')
    lignes = lignes[0].split(',')
    list_str_to_int(lignes)

    lantern_fish_list = get_lantern_fish_list(lignes)

    status_lantern_fish(0, lantern_fish_list)

    print(spawn_lanternfish(lantern_fish_list, 80))


def status_lantern_fish(i, lantern_fish_list):
    list_day = []
    for lantern_fish in lantern_fish_list:
        list_day.append(lantern_fish.day_until_new)
    print(f"{i} {list_day}")


if __name__ == '__main__':
    main()

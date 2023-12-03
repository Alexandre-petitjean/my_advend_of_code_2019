from year_2021.tools import open_file_line_by_line


def calc_power_comp(diags):
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(12):
        nb_zero = 0
        nb_one = 0
        for diag in diags:
            if diag[i] == '0':
                nb_zero += 1
            else:
                nb_one += 1

        if nb_one > nb_zero:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)
    return gamma_rate * epsilon_rate


def get_nb_zero_un(binarys_list, index):
    nb_zero = 0
    nb_one = 0
    list_zero = []
    list_one = []
    for binary in binarys_list:
        if binary[index] == '0':
            nb_zero += 1
            list_zero.append(binary)
        else:
            nb_one += 1
            list_one.append(binary)
    return [nb_zero, nb_one, list_zero, list_one]


def calc_oxy_co2(binarys_list, type):

    while len(binarys_list) != 1:
        for i in range(12):
            if len(binarys_list) != 1:
                list_zero_un = get_nb_zero_un(binarys_list, i)

            if type == 'oxy':
                if list_zero_un[0] > list_zero_un[1]:
                    binarys_list = list_zero_un[2]
                else:
                    binarys_list = list_zero_un[3]
            else:
                if list_zero_un[0] > list_zero_un[1]:
                    binarys_list = list_zero_un[3]
                else:
                    if list_zero_un[2]:
                        binarys_list = list_zero_un[2]
                    else:
                        binarys_list = list_zero_un[3]
    return binarys_list[0]


def calc_life_support(diags):
    oxygen = int(calc_oxy_co2(diags[:], 'oxy'), 2)
    co2 = int(calc_oxy_co2(diags[:], 'co2'), 2)
    return oxygen * co2


def main():
    diags = open_file_line_by_line('input.txt')
    print(calc_power_comp(diags))
    print(calc_life_support(diags))


if __name__ == '__main__':
    main()

from Utils.tools import open_file_explode_array


def exercice_2():
    print("Exercice 2")
    filename = "jour2/exo_2.txt"
    my_list = open_file_explode_array(filename)
    list_str_to_int(my_list)
    # print(treatment_part_1(my_list))
    print(treatment_part_2(my_list))


def list_str_to_int(my_list):
    for i in range(0, len(my_list)):
        my_list[i] = int(my_list[i])


def get_index(i, my_list):
    return [my_list[i + 1], my_list[i + 2], my_list[i + 3]]


def treatment_part_2(my_list):

    resultat = 19690720
    noun = 0
    my_list[1] = noun
    while noun <= 99:
        verb = 0
        my_list[2] = verb
        while verb <= 99:
            if treatment(my_list[:]) == resultat:
                return (100 * noun) + verb
            verb = verb + 1
            my_list[2] = verb
        noun = noun + 1
        my_list[1] = noun


def treatment_part_1(my_list):
    my_list[1] = 12
    my_list[2] = 2
    return treatment(my_list)


def treatment(my_list):
    i = 0
    result = 0
    while i < my_list.__len__():
        if my_list[i] == 1:
            index = get_index(i, my_list)
            calc = my_list[index[0]] + my_list[index[1]]
            my_list[index[2]] = calc
        elif my_list[i] == 2:
            index = get_index(i, my_list)
            calc = my_list[index[0]] * my_list[index[1]]
            my_list[index[2]] = calc
        else:
            result = my_list[0]
        i = i + 4
    return result

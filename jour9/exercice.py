from Utils.tools import open_file_explode_array, list_str_to_int

# Déclaration de constante, c'est plus facile pour la lecture du code.
ADD = '1'
MULT = '2'
IN = '3'
OUT = '4'
JUMPT = '5'
JUMPF = '6'
LESS = '7'
EQUALS = '8'
STOP = 99


def exercice_9():
    """
    Fonction start du jour.
    """
    print("Jour 9")
    filename = "jour9/jour9.txt"
    my_list = open_file_explode_array(filename)
    list_str_to_int(my_list)
    # treatment_part_1(my_list)
    treatment_part_2(my_list)


def get_index(i, my_list):
    """
    Retourne un tableau de string, qui correspond a la valeur des 3 prochaines itération de la liste a partir de i.
    :param i: La position dans le tableau.
    :param my_list: La liste de int.
    :return: Un tableau de int.
    """
    return [my_list[i + 1], my_list[i + 2], my_list[i + 3]]


def treatment_part_1(my_list):
    """
    Traitement de la partie 1 du jour.
    :param my_list:
    :return:
    """
    my_input = 1
    return treatment(my_list, my_input)


def treatment_part_2(my_list):
    """
    Traitement de la partie 2 du jour.
    :param my_list:
    :return:
    """
    my_input = 5
    return treatment(my_list, my_input)

def treatment_day_7(software, input):
    """
    Traitement le jour 7 qui fonctionne via le intcode computer.
    """
    return treatment(software, input)


def treatment(my_list, my_input):
    """
    Traitement pour effectuer la résolution de l'exercice.
    :param my_list: La liste de int.
    :param my_input: L'input demandé pour le opcode 3.
    """
    i = 0
    result = 0
    while i < my_list.__len__() and my_list[i] != STOP:
        number = str(my_list[i])
        # Tous les opcodes doivent être des nombres à 5 chiffres.
        while len(number) < 5:
            number = '0' + number

        mode2 = number[1]
        mode1 = number[2]
        opcode = number[4]

        if opcode == ADD or opcode == MULT:
            op_code_add_mult(mode1, mode2, opcode, i, my_list)
            i = i + 4
        elif opcode == LESS or opcode == EQUALS:
            op_code_less_equals(mode1, mode2, opcode, i, my_list)
            i = i + 4
        elif opcode == IN or opcode == OUT:
            if opcode == IN:
                op_code_in(i, my_list, my_input[0])
                my_input.remove(my_input[0])
            elif opcode == OUT:
                result = op_code_out(i, my_list)
            i = i + 2
        elif opcode == JUMPT or opcode == JUMPF:
            i = op_code_jumpt_jumf(mode1, mode2, opcode, i, my_list)

    return result


def op_code_add_mult(mode1, mode2, opcode, i, my_list):
    index = get_index(i, my_list)

    if mode1 == '1':
        param1 = index[0]
    else:
        param1 = my_list[index[0]]
    if mode2 == '1':
        param2 = index[1]
    else:
        param2 = my_list[index[1]]

    if opcode == '1':
        calc = param1 + param2
    else:
        calc = param1 * param2

    my_list[index[2]] = calc


def op_code_in(i, my_list, my_input):
    """
    Fonction pour le opcode 3
    :param i: L'index dans la liste.
    :param my_list: La liste de int.
    :param my_input: l'input demandé.
    """
    target = my_list[i + 1]
    my_list[target] = my_input


def op_code_out(i, my_list):
    """
    Fonction pour le opcode 4
    :param i: L'index dans la liste.
    :param my_list: La liste de int.
    """
    target = my_list[i + 1]
    return my_list[target]


def op_code_jumpt_jumf(mode1, mode2,opcode, i, my_list):
    index = get_index(i, my_list)
    if mode1 == '1':
        param1 = index[0]
    else:
        param1 = my_list[index[0]]
    if mode2 == '1':
        param2 = index[1]
    else:
        param2 = my_list[index[1]]

    if opcode == JUMPT:
        if param1 != 0:
            i = param2
        else:
            i = i + 3
    else:
        if param1 == 0:
            i = param2
        else:
            i = i + 3
    return i


def op_code_less_equals(mode1, mode2, opcode, i, my_list):
    index = get_index(i, my_list)
    result = 0

    if mode1 == '1':
        param1 = index[0]
    else:
        param1 = my_list[index[0]]
    if mode2 == '1':
        param2 = index[1]
    else:
        param2 = my_list[index[1]]

    if opcode == LESS:
        if param1 < param2:
            result = 1
    else:
        if param1 == param2:
            result = 1

    my_list[index[2]] = result

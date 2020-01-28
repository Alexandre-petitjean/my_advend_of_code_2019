from Utils.tools import open_file_explode_array

# Déclaration de constante, c'est plus facile pour la lecture du code.
ADD = '1'
MULT = '2'
IN = '3'
OUT = '4'
JUMPT = '5'
JUMPF = '6'
LESS = '7'
EQUALS = '8'


def exercice_5():
    """
    Fonction start du jour.
    """
    print("Jour 5")
    filename = "jour5/jour5.txt"
    my_list = open_file_explode_array(filename)
    list_str_to_int(my_list)
    treatment_part_1(my_list)


def list_str_to_int(my_list):
    """
    Transforme la liste de str en liste de int.
    :rtype: object
    """
    for i in range(0, len(my_list)):
        my_list[i] = int(my_list[i])


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


def op_code_parametrer_mode(mode1, mode2, opcode, i, my_list):
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


def treatment(my_list, my_input):
    """
    Traitement pour effectuer la résolution de l'exercice.
    :param my_list: La liste de int.
    :param my_input: L'input demandé pour le opcode 3.
    """
    i = 0
    while i < my_list.__len__():
        number = str(my_list[i])
        # Tous les opcode doivent être des nombre à 5 chiffres.
        while len(number) < 5:
            number = '0' + number
        mode2 = number[1]
        mode1 = number[2]
        opcode = number[4]

        if opcode == ADD or opcode == MULT:
            op_code_parametrer_mode(mode1, mode2, opcode, i, my_list)
            i = i + 4
        elif opcode == IN or opcode == OUT:
            if opcode == IN:
                op_code_in(i, my_list, my_input)
            elif opcode == OUT:
                op_code_out(i, my_list)
            i = i + 2


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
    print(str(i) + " - " + str(my_list[target]))

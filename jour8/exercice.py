from textwrap import wrap

import Utils.tools


def exercice_8():
    """
    Fonction start du jour.
    """
    print("Jour 8")
    filename = "jour8/jour8.txt"
    my_list = Utils.tools.open_file_line_by_line(filename)
    treatment_part_1(my_list)


def explode_size(my_list, size):
    """
    Fonction qui prend un liste et qui la explose sont contenu grace a la taille passé en parametre.
    :param my_list: La liste a traiter.
    :param size: La taille des layers à obtenir.
    :return: un tableau avec les layers.
    """
    return wrap(my_list[0], size)


def treatment_part_1(my_list):
    """
    Fonction qui sert au traitement de la partie 1.
    :param my_list: La liste des données à traiter.
    """
    wide = 25
    tall = 6
    size = wide * tall
    my_list = explode_size(my_list, size)
    treatment(my_list)


def treatment(my_list):
    """
    Fonction qui effectue le traitement principale.
    :param my_list: La liste des données à traiter.
    """
    result = my_list[0]
    i = 1
    while i < my_list.__len__():
        nb_zero = count_digit(my_list[i], '0')
        if 0 == count_digit(result, '0') or nb_zero < count_digit(result, '0'):
            result = my_list[i]
        i = i + 1
    nb_one = count_digit(result, '1')
    nb_two = count_digit(result, '2')
    print(nb_one * nb_two)


def count_digit(element, digit):
    """
    Compte Le nombre de 0 qui il y a dans une string.
    :param digit: char du chiffre que l'on recherche dans la string.
    :param element: Une string de la liste my_list.
    :return: Le nombre de char 0 trouvé.
    """
    count = 0
    for char in element:
        if char == digit:
            count = count + 1
    return count

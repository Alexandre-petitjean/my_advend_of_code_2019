from textwrap import wrap
from PIL import Image, ImageColor

import Utils.tools


def exercice_8():
    """
    Fonction start du jour.
    """
    print("Jour 8")
    filename = "jour8/jour8.txt"
    my_list = Utils.tools.open_file_line_by_line(filename)

    wide = 25
    tall = 6
    size = wide * tall
    my_list = explode_size(my_list, size)

    # treatment_part_1(my_list)
    treatment_part_2(my_list)


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


def treatment_part_2(my_list):
    """
    Fonction qui sert au traitement de la partie 1.
    :param my_list: La liste des données à traiter.
    """
    new_layer = []
    i = 0
    while i < len(my_list[0]):
        j = 0
        layer = ""
        while j < my_list.__len__():
            layer += my_list[j][i]
            j = j + 1
        new_layer.append(layer)
        i = i + 1
    layer = decode(new_layer)
    draw(layer)


def decode(new_layer):
    final_layer = ""
    for element in new_layer:
        i = 0
        while element[i] == '2':
            i = i + 1
        final_layer += element[i]
    return final_layer


def draw(layer):
    im = Image.new('1', (25, 6))
    layer = wrap(layer, 25)
    for element in layer:
        for pixel in element:
            if pixel == '1':
                im.putpixel((layer.index(element), element.index(pixel)), ImageColor.getcolor('black', '1'))
            elif pixel == '0':
                im.putpixel((layer.index(element), element.index(pixel)), ImageColor.getcolor('white', '1'))
    im.show()


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

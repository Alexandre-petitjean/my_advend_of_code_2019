import os


def open_file_line_by_line(filename):
    """
    Fonction qui ouvre le fichier passé en parametre.
    Puis rentre toutes les lignes dans un tableau.
    :param filename: Le nom du fichier.
    :return: un tableau des lignes du fichier.
    """
    lines = []
    if os.path.exists(filename):
        with open(filename) as fp:
            lines = fp.read().splitlines()
    return lines


def list_str_to_int(my_list):
    """
    Transforme la liste de str en liste de int.
    :rtype: object
    """
    for i in range(0, len(my_list)):
        my_list[i] = int(my_list[i])
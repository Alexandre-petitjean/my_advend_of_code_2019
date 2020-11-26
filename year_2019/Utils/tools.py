import os


def open_file_line_by_line(filename):
    """
    Fonction qui ouvre le fichier passé en paramtre.
    Puis rentre toutes les ligne dans un tableau.
    :param filename: Le nom du fichier.
    :return: un tableau des lignes du fichier.
    """
    my_list = []
    if os.path.exists(filename):
        with open(filename) as fp:
            line = fp.readline()
            while line:
                my_list.append(line)
                line = fp.readline()
        return my_list


def open_file_explode_array(filename):
    """
    Fonction qui ouvre le fichier passé en paramtre.
    Puis rentre toutes les elements séparé par une virgule dans un tableau.
    :param filename: Le nom du fichier.
    :return: Un tableau des elements du fichier.
    """
    if os.path.exists(filename):
        with open(filename) as fp:
            line = fp.readline()
            my_list = line.split(',')
        return my_list


def open_file_explode_array_line_by_line(filename):
    the_list = []
    if os.path.exists(filename):
        with open(filename) as fp:
            line = fp.readline()
            while line:
                my_list = line.split(',')
                the_list.append(my_list[:])
                line = fp.readline()
        return the_list


def list_str_to_int(my_list):
    """
    Transforme la liste de str en liste de int.
    :rtype: object
    """
    for i in range(0, len(my_list)):
        my_list[i] = int(my_list[i])

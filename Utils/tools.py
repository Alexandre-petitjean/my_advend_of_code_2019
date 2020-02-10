import os
from textwrap import wrap


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

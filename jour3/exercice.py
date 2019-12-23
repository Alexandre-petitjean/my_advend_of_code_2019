
from matplotlib import pyplot as plt

from Utils.tools import open_file_explode_array


def exercice_3():
    print("Exercice 3")
    filename = "jour3/exo_3.txt"
    my_list = open_file_explode_array(filename)
    new_grid()


def new_grid():
    plt.grid()
    plt.show()

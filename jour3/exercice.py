from Utils.tools import open_file_explode_array_line_by_line

import numpy as np
import matplotlib.pyplot as plt


def exercice_3():
    print("Exercice 3")
    filename = "jour3/exo_3.txt"
    my_list = open_file_explode_array_line_by_line(filename)
    new_grid()


def new_grid():
    plt.grid()
    plt.show()

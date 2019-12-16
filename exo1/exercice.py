import math

from Utils.tools import open_file


def exo1():
    print("Exercice 1")
    filename = "exo1/exo_1.txt"
    my_list = open_file(filename)
    print(calcule(my_list))


def calcule(my_list):
    result = 0
    for i in my_list:
        calcul = int(i) / 3
        calcul = math.floor(calcul)
        calcul = calcul - 2
        result += calcul
    return result

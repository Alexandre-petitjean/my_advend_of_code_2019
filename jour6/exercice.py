from Utils.tools import open_file_line_by_line
from jour6.tree.Node import Node
from jour6.tree.Tree import Tree


def exercice_6():
    print("Exercice 6")
    filename = "jour6/jour_6.txt"
    my_list = open_file_line_by_line(filename)
    node_array = []
    treatement(my_list, node_array)


def treatement(my_list, node_array):
    for element in my_list:
        array = element.split()
        parent = Node(array[0], None, None)
        Node(array[1], parent, )

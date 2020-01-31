from Utils.tools import open_file_line_by_line
from anytree import Node, RenderTree, AsciiStyle, findall_by_attr, find
import sys
sys.setrecursionlimit(10000)


def exercice_6():
    print("Exercice 6")
    filename = "jour6/jour_6.txt"
    my_list = open_file_line_by_line(filename)
    sys.setrecursionlimit(10000)
    treatement(my_list, "COM")


def find_next_node(my_list, root):
    for element in my_list:
        element_array = element.split(")")
        node = find(root, lambda node: node.name == element_array[0])
        return element


def create_root(node_str):
    node_array = node_str.split(")")
    node = Node(node_array[0])
    return Node(node_array[1][:-1], node)


def add_child_node(last_node, node_str):
    return Node(node_str, last_node)


def make_tree(my_list, nom_node):
    # On retrouve le root dans la my_list.
    node_str = find_next_node(my_list, nom_node)
    last_node = create_root(node_str)
    root = last_node.parent
    while my_list.__len__() > 0:
        node_str = find_next_node(my_list, root)
        node_array = node_str.split(")")
        last_node = add_child_node(last_node, node_array[1][:-1])
    return root


def count_orbits(node, nb_orbits):
    while node.children.__len__() > 0:
        nb_orbits = nb_orbits + 1
        if node.ancestors.__len__() > 0:
            nb_orbits = nb_orbits + (node.ancestors.__len__() - 1)
        for child in node.children:
            count_orbits(child, nb_orbits)

    return nb_orbits


def treatement(my_list, nom_node):
    root = make_tree(my_list, nom_node)
    nb_orbits = 0
    nb_orbits = count_orbits(root, nb_orbits)
    return nb_orbits

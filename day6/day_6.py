"""
Day 6 of the avent of code.
--- Day 6: Universal Orbit Map ---
"""
from Utils.tools import open_file_line_by_line
from day6.Tree.Node import Node
from day6.Tree.Tree import Tree


def main():
    print("Jour 6")
    filename = "input_day_6.txt"
    my_list = open_file_line_by_line(filename)
    # treatment_part_1(my_list)
    treatment_part_2(my_list)


def treatment_part_1(my_list):
    root_name = "COM"
    tree = make_tree(my_list, root_name)
    tree = treatment(my_list, tree)
    orbit_sum = calcul_orbit(tree.get_root(), 0)
    print(orbit_sum)


def treatment_part_2(my_list):
    root_name = "COM"
    tree = make_tree(my_list, root_name)
    tree = treatment(my_list, tree)
    print(orbital_transfers(tree, "YOU", "SAN"))


def treatment(my_list, tree):
    """
    This is the main get_wires_path of the day.
    @rtype: Tree
    """
    while my_list.__len__() > 0:
        rows = find_rows(my_list, Tree.lastNode.get_name())
        add_nodes(tree, rows)
    return tree


def delete_rows(my_list, result):
    """
    Delete the rows for the list in parameter.
    @param my_list: The input list.
    @param result: the rows to be deleted.
    """
    for element in result:
        my_list.remove(element)


def find_rows(my_list, nom_node):
    """
    Find rows witch containe a specific node name.
    @rtype: A array.
    """
    result = [i for i in my_list if nom_node in i]
    if result.__len__() == 0:
        j = 0
        while j < Tree.node_list.__len__() and result.__len__() == 0:
            result = [i for i in my_list if Tree.node_list[j] in i]
            j = j + 1
    delete_rows(my_list, result)
    return result


def make_tree(my_list, root_name):
    """
    Make the root and the tree
    @param my_list:
    @param root_name:
    @return:
    """
    rows = find_rows(my_list, root_name)
    obj = rows[0].split(")")
    root = Node(obj[0], None)
    Node(obj[1], root)
    tree = Tree(root)
    return tree


def add_nodes(tree, rows):
    """
    Add a node to the tree.
    @param tree: The tree object.
    @param rows: A row in the input file.
    """
    for row in rows:
        obj = row.split(")")
        if obj[0] == tree.lastNode.get_name():
            parent = tree.lastNode
        else:
            parent = tree.find_node_by_name(tree.get_root(), obj[0])
        Node(obj[1], parent)


def calcul_orbit(node, orbit):
    """
    Calculation of the sum of direct and indirect orbits.
    @param node: An Node object.
    @param orbit: The sum of direct and indirect orbits.
    @return: The sum of direct and indirect orbits.
    """
    if node.depth != 0:
        orbit += node.get_depth() - 1
    for child in node.children:
        orbit += 1
        orbit = calcul_orbit(child, orbit)
    return orbit


def orbital_transfers(tree, me_name, santa_name):
    """
    Calculation of the orbital transferes needed for join Santa.
    @rtype: The number of orbital transferes.
    """
    me = tree.find_node_by_name(tree.get_root(), me_name)
    santa = tree.find_node_by_name(tree.get_root(), santa_name)
    distance = tree.get_distance_between_node(me, santa)
    return distance


if __name__ == "__main__":
    main()

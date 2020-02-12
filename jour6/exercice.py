from Utils.tools import open_file_line_by_line
from jour6.Tree.Node import Node
from jour6.Tree.Tree import Tree


def day_6():
    print("Exercise 6")
    filename = "jour6/jour_6.txt"
    my_list = open_file_line_by_line(filename)
    # my_list = ["COM)B", "B)C", "C)D", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "D)E", "K)L"]
    treatment_part_1(my_list)


def treatment_part_1(my_list):
    root_name = "COM"
    tree = make_tree(my_list, root_name)
    print(treatment(my_list, tree))


def delete_rows(my_list, result):
    for element in result:
        my_list.remove(element)


def find_rows(my_list, nom_node):
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
    for row in rows:

        obj = row.split(")")
        if obj[0] == tree.lastNode.get_name():
            parent = tree.lastNode
        else:
            parent = tree.find_node_by_name(tree.get_root(), obj[0])
        Node(obj[1], parent)


def get_row(my_list, tree):
    i = 0
    result = None
    while i < my_list.__len__() and result is None:
        if tree.find_node_by_name(tree.get_root(), my_list[i].split(")")[0]):
            result = my_list[i]
        i = i + 1
    return [result]


def calcul_orbit(node, orbit):
    if node.depth != 0:
        orbit += node.get_depth() - 1
    for child in node.children:
        orbit += 1
        orbit = calcul_orbit(child, orbit)
    return orbit


def treatment(my_list, tree):
    while my_list.__len__() > 0:
        rows = find_rows(my_list, Tree.lastNode.get_name())
        add_nodes(tree, rows)
    print(tree)
    return calcul_orbit(tree.get_root(), 0)

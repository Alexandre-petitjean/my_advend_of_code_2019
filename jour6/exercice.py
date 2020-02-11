from jour6.Tree.Node import Node
from jour6.Tree.Tree import Tree


def exercice_6():
    print("Exercice 6")
    filename = "jour6/jour_6.txt"
    # my_list = open_file_line_by_line(filename)
    my_list = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]
    treatment_part_1(my_list)


def treatment_part_1(my_list):
    root_name = "COM"
    tree = make_tree(my_list, root_name)
    treatment(my_list, tree)


def delete_rows(my_list, result):
    for element in result:
        my_list.remove(element)


def find_rows(my_list, nom_node):
    result = [i for i in my_list if nom_node in i]
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


def get_row(my_list):
    rows = [my_list[0]]
    delete_rows(my_list, rows)
    return rows


def calcul_orbit(tree):
    node = tree.root
    direct_orbit = 0
    indirect_orbit = 0


def treatment(my_list, tree):
    while my_list.__len__() > 0:
        rows = find_rows(my_list, Tree.lastNode.get_name())
        if rows.__len__() == 0:
            rows = get_row(my_list)
        add_nodes(tree, rows)
    print(tree)

from Utils.tools import open_file_explode_array, list_str_to_int
from jour5.exercice import treatment_day_7
from jour7.Numero import Numero
from jour7.Tree.Node import Node
from jour7.Tree.Tree import Tree


def day_7():
    print("Exercise 7")
    filename = "jour7/jour_7.txt"
    my_list = open_file_explode_array(filename)
    list_str_to_int(my_list)

    amplifier_input = get_amplifier_input()
    print(treatment(my_list, amplifier_input))


def create_tree(list_input):
    root_value = ""
    for element in list_input:
        root_value += str(element.value)
    root = Node(root_value, None)
    tree = Tree(root)
    return tree


def make_sub_tree(excep_list, list_input, parent):
    for element in list_input:
        if element.value not in excep_list:
            value = ""
            for number in excep_list:
                value += number
            Node(value + element.value, parent)
    for child in parent.get_children():
        excep_list.append(child.value[child.depth - 1])
        excep_list = make_sub_tree(excep_list, list_input, child)
    return excep_list[:-1]


def make_tree(tree, list_input):
    excep_list = []
    make_sub_tree(excep_list, list_input, tree.root)
    return tree


def get_amplifier_input():
    list_input = [Numero.ZERO, Numero.UN, Numero.DEUX, Numero.TROIS, Numero.QUATRE]
    tree = create_tree(list_input)
    tree = make_tree(tree, list_input)
    return tree.get_list_number_by_depth(5)


def test_amplifier_by_input(software, input_list):
    result = 0
    for input in input_list:
        result = treatment_day_7(software[:], [int(input), result])
    return result


def treatment(software, amplifier_input):
    thrusters_signal = 0
    for input in amplifier_input:
        output_signal = test_amplifier_by_input(software, input)
        if thrusters_signal < output_signal:
            thrusters_signal = output_signal
    return thrusters_signal
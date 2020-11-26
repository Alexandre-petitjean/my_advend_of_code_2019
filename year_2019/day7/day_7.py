from day5.exercice import treatment_day_7

from Utils.tools import open_file_explode_array, list_str_to_int
from day7.Tree.Node import Node
from day7.Tree.Tree import Tree


def main():
    print("Jour 7")
    filename = "input_day_7.txt"
    my_list = open_file_explode_array(filename)
    list_str_to_int(my_list)

    # print(treatment_part_1(my_list, ['0', '1', '2', '3', '4']))
    print(treatment_part_2(my_list, ['5', '6', '7', '8', '9']))


def create_tree(list_input):
    root_value = ""
    for element in list_input:
        root_value += str(element)
    root = Node(root_value, None)
    tree = Tree(root)
    return tree


def make_sub_tree(excep_list, list_input, parent):
    for element in list_input:
        if element not in excep_list:
            value = ""
            for number in excep_list:
                value += number
            Node(value + element, parent)
    for child in parent.get_children():
        excep_list.append(child.value[child.depth - 1])
        excep_list = make_sub_tree(excep_list, list_input, child)
    return excep_list[:-1]


def make_tree(tree, list_input):
    excep_list = []
    make_sub_tree(excep_list, list_input, tree.root)
    return tree


def get_amplifier_input(list_input):
    tree = create_tree(list_input)
    tree = make_tree(tree, list_input)
    return tree.get_list_number_by_depth(5)


def treatment_part_1(software, numbers):
    thrusters_signal = 0
    amplifier_input = get_amplifier_input(numbers)

    for input_list in amplifier_input:
        output_signal = 0
        for input in input_list:
            output_signal = treatment_day_7(software[:], [int(input), output_signal])
        if thrusters_signal < output_signal:
            thrusters_signal = output_signal

    return thrusters_signal


def treatment_part_2(software, numbers):
    thrusters_signal = 0
    amplifier_input = get_amplifier_input(numbers)

    for input_list in amplifier_input:
        output_signal = 0
        for input in input_list:
            output_signal = treatment_day_7(software, [int(input), output_signal])
        if thrusters_signal < output_signal:
            thrusters_signal = output_signal

    return thrusters_signal


if __name__ == "__main__":
    main()

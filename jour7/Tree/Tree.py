class Tree:
    lastNode = None
    node_list = []

    def __init__(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def find_node_by_name(self, node, node_name):
        result = None
        if node.name != node_name:
            i = 0
            while i < node.children.__len__() and result is None:
                result = self.find_node_by_name(node.children[i], node_name)
                i = i + 1
        else:
            result = node
        return result

    def course_tree(self, my_string, node):
        white_space = " "
        i = 0
        while i < node.get_depth():
            white_space += "  "
            i = i + 1
        my_string += white_space + "└" + " " + str(node.value) + "\n"
        for child in node.children:
            my_string = self.course_tree(my_string, child)
        return my_string

    def __str__(self):
        node = self.root
        chaine = "--- Tree ---\n"
        chaine = self.course_tree(chaine, node)
        return chaine

    def get_list_number_by_depth(self, depth):
        result = []
        return self.get_list_number(self.root, depth, result)

    def get_list_number(self, node, depth, result):
        for child in node.children:
            if child.depth != depth:
                result = self.get_list_number(child, depth, result)
            else:
                result.append(child.value)
        return result

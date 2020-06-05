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
        my_string += white_space + "└" + " " + node.name + "\n"
        for child in node.children:
            my_string = self.course_tree(my_string, child)
        return my_string

    @staticmethod
    def get_ancestor_list(ancestor_list, node):
        """
        Get the ancestor list of the node.
        @param ancestor_list: 
        @param node: 
        @return: 
        """
        while node.parent is not None:
            ancestor_list.append(node.parent)
            node = node.parent
        return ancestor_list

    @staticmethod
    def get_first_parent(ancestors_node1, ancestors_node2):
        """
        Get the first commun parent.
        @param ancestors_node1: The list of parents of the node 1.
        @param ancestors_node2: The list of parents of the node 2.
        @return: The first commun parent.
        """
        parent = None
        i = 0
        while i < ancestors_node1.__len__() and parent is None:
            j = 0
            while j < ancestors_node2.__len__() and parent is None:
                if ancestors_node1[i].get_name() == ancestors_node2[j].get_name():
                    parent = ancestors_node1[i]
                j = j + 1
            i = i + 1
        return parent

    @staticmethod
    def get_distance_for_first_parent(parent_list, target_parent):
        result = 0
        i = 0
        while i < parent_list.__len__() and result == 0:
            if parent_list[i] == target_parent:
                result = i
            i = i + 1
        return result

    def get_distance_between_node(self, node1, node2):
        parents_node1 = []
        parents_node2 = []
        parents_node1 = self.get_ancestor_list(parents_node1, node1)
        parents_node2 = self.get_ancestor_list(parents_node2, node2)
        parent = self.get_first_parent(parents_node1, parents_node2)
        distance_node1 = self.get_distance_for_first_parent(parents_node1, parent)
        distance_node2 = self.get_distance_for_first_parent(parents_node2, parent)
        return distance_node1 + distance_node2

    def __str__(self):
        node = self.root
        chaine = "--- Tree ---\n"
        chaine = self.course_tree(chaine, node)
        return chaine

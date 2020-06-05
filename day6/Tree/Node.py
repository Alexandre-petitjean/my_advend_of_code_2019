from day6.Tree.Tree import Tree


class Node:

    def __init__(self, name, parent=None):
        self.name = name
        self.children = []
        self.right_siblings = None
        self.parent = parent
        self.depth = 0
        Tree.node_list.append(self.name)
        if parent is not None:
            self.parent.add_child(self)
            self.depth = self.parent.get_depth() + 1
        Tree.lastNode = self

    def get_name(self):
        return self.name

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def get_right_sibling(self):
        return self.right_siblings

    def get_depth(self):
        return self.depth

    def has_children(self):
        result = False
        if self.children.__len__() > 0:
            result = True
        return result

    def has_sibling(self):
        result = False
        if self.right_siblings is not None:
            result = True
        return result

    def add_child(self, new_child):
        if self.children.__len__() > 0:
            self.children[self.children.__len__() - 1].add_siblings(new_child)
        self.children.append(new_child)

    def add_siblings(self, new_sibling):
        self.right_siblings = new_sibling

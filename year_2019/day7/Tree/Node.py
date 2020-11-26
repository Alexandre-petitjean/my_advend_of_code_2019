from day7.Tree.Tree import Tree


class Node:

    def __init__(self, value, parent=None):
        self.value = value
        self.children = []
        self.parent = parent
        self.depth = 0
        if parent is not None:
            self.parent.add_child(self)
            self.depth = self.parent.get_depth() + 1
        Tree.lastNode = self

    def get_value(self):
        return self.value

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def get_depth(self):
        return self.depth

    def has_children(self):
        result = False
        if self.children.__len__() > 0:
            result = True
        return result

    def add_child(self, new_child):
        self.children.append(new_child)

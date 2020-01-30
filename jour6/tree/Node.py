

class Node:

    left_most_child = None
    right_sibiling = None

    def __init__(self, nom, parent):
        self.nom = nom
        self.parent = parent

    def add_child(self, left_most_child):
        self.left_most_child = left_most_child

    def add_sibiling(self, right_sibiling):
        while self.right_sibiling is not None:
            self.right_sibiling
        if self.right_sibiling is None:
            self.right_sibiling = right_sibiling
        else:
            while

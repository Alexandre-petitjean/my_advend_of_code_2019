class Node:

    right_sibiling = None
    parent = None

    def __init__(self, nom):
        self.parent = parent
        self.nom = nom

    def add_sibiling(self, new_sibiling):
        self.right_sibiling = new_sibiling

    def add_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.child = child

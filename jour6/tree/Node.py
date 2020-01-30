<<<<<<< HEAD
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
=======


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
>>>>>>> 52d0e5c660618e5deb9e81d802087de4e23c18b7

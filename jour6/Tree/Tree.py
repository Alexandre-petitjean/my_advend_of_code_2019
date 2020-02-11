class Tree:

    lastNode = None

    def __init__(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def find_node_by_name(self, node, node_name):
        result = None
        if node.name != node_name:
            if node.has_children():
                node = node.children[0]
                result = self.find_node_by_name(node, node_name)
            if node.has_sibling() and result is None:
                node = node.get_right_sibling()
                result = self.find_node_by_name(node, node_name)
        else:
            result = node
        return result

    def __str__(self):
        node = self.root
        string = "--- Tree ---\n"
        string += node.get_name() + "\n"
        return string

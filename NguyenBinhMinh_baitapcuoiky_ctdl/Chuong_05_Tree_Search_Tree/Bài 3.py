class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = None

    def SoNutLa(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        else:
            return self.SoNutLa(node.left) + self.SoNutLa(node.right)

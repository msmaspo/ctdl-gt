class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = None

    def SoNut(self, node):
        if node is None:
            return 0
        else:
            return self.SoNut(node.left) + 1 + self.SoNut(node.right)

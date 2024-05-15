class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = None

    def SoNutTrungGian(self, node):
        if node is None:
            return 0
        if node.left is not None and node.right is not None:
            return 1 + self.SoNutTrungGian(node.left) + self.SoNutTrungGian(node.right)
        elif node.left is not None:
            return self.SoNutTrungGian(node.left)
        elif node.right is not None:
            return self.SoNutTrungGian(node.right)
        else:
            return 0

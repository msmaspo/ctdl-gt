class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class Cay:
    def __init__(self):
        self.root = None

    def KiemTraBST(self):
        return self._kiemTraBST(self.root, float('-inf'), float('inf'))

    def _kiemTraBST(self, node, min, max):
        if node is None:
            return True
        if node.info < min or node.info > max:
            return False
        return (self._kiemTraBST(node.left, min, node.info - 1) and
                self._kiemTraBST(node.right, node.info + 1, max))

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.height = 1

class Cay:
    def __init__(self):
        self.root = None

    def KiemTraAVL(self):
        return self._kiemTraAVL(self.root)

    def _kiemTraAVL(self, node):
        if node is None:
            return True
        height_left = self._height(node.left)
        height_right = self._height(node.right)
        if abs(height_left - height_right) <= 1 and self._kiemTraAVL(node.left) is True and self._kiemTraAVL(node.right) is True:
            return True
        return False

    def _height(self, node):
        if node is None:
            return 0
        return node.height

class Node:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def SoSanh(self, cay2):
        return self._SoSanh(self.root, cay2.root)

    def _SoSanh(self, node1, node2):
        # Trường hợp cả hai cây đều rỗng
        if node1 is None and node2 is None:
            return True

        # Trường hợp cả hai cây đều không rỗng
        if node1 is not None and node2 is not None:
            return ((node1.info == node2.info) and
                    self._SoSanh(node1.left, node2.left) and
                    self._SoSanh(node1.right, node2.right))

        # Trường hợp một trong hai cây rỗng
        return False

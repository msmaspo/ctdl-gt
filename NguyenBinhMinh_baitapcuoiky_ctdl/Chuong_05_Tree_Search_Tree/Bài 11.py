class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def BSTTuanTu(self):
        return self._check_BST(self.root)

    def _check_BST(self, node):
        if node is None:
            return True

        if node.left and node.right:
            return False

        return self._check_BST(node.left) and self._check_BST(node.right)

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class Cay:
    def __init__(self):
        self.root = None

    def Chep(self):
        return self._chep(self.root)

    def _chep(self, node):
        if node is None:
            return None
        node_new = Node(node.info)
        node_new.left = self._chep(node.left)
        node_new.right = self._chep(node.right)
        return node_new

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def CanBangHoanToan(self):
        return self._check_balance(self.root)[0]

    def _check_balance(self, node):
        if node is None:
            return True, 0  # A null tree is balanced and has height 0

        left_balanced, left_height = self._check_balance(node.left)
        if not left_balanced:
            return False, 0  # If left subtree is not balanced, no need to check right subtree

        right_balanced, right_height = self._check_balance(node.right)
        if not right_balanced:
            return False, 0  # If right subtree is not balanced, no need to check further

        # Tree is balanced if difference between left and right heights is at most 1
        return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1

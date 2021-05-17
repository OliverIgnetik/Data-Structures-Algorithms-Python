import collections
from level_order_traverse import levelOrderPrint


class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


def trimBST(tree, minVal, maxVal):

    if not tree:
        return

    tree.left = trimBST(tree.left, minVal, maxVal)
    tree.right = trimBST(tree.right, minVal, maxVal)

    if minVal <= tree.val <= maxVal:
        return tree

    if tree.val < minVal:
        return tree.right

    if tree.val > maxVal:
        return tree.left


root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(7)
root.right = Node(30)
root.right.right = Node(35)
root.right.left = Node(28)
trimmedBST = trimBST(root, 2, 30)
levelOrderPrint(trimmedBST)

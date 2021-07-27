# BST TREE PROPERTY
# left subtree has all values less then current node
# right subtree has all values greater then current node
class Node:
    def __init__(self, val=None):
        self.left, self.right, self.val = None, None, val


INFINITY = float("infinity")
NEG_INFINITY = float("-infinity")


def isBST(tree, minVal=NEG_INFINITY, maxVal=INFINITY):
    if tree is None:
        return True
    if not minVal <= tree.val <= maxVal:
        return False

    return isBST(tree.left, minVal, tree.val) and isBST(tree.right, tree.val, maxVal)


def isBST2(tree, lastNode=[NEG_INFINITY]):

    # check leaf
    if tree is None:
        return True

    # left
    if not isBST2(tree.left, lastNode):
        return False

    # root
    if tree.val < lastNode[0]:
        return False

    lastNode[0] = tree.val

    # right
    return isBST2(tree.right, lastNode)


tree = Node(6)
tree.left = Node(2)
tree.left.left = Node(1)
tree.left.right = Node(4)
tree.right = Node(9)
tree.right.left = Node(7)
tree.right.right = Node(10)

print(isBST2(tree))

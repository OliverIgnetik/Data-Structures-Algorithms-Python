# approach 1 - inorder traversal vs sort

tree_vals = []


class Node:
    def __init__(self, k, val):
        self.key = k
        self.value = val
        self.left = None
        self.right = None


tree = Node(10, "Hello")
tree.left = Node(5, "Five")
tree.right = Node(30, "Thirty")


def inorder(tree):
    if tree != None:
        inorder(tree.left)
        tree_vals.append(tree.value)
        inorder(tree.right)


def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)


inorder(tree)
sort_check(tree_vals)


# approach 2 tracking valid values for nodes
class Node:
    def __init__(self, k, val):
        self.key = k
        self.value = val
        self.left = None
        self.right = None


def tree_max(node):
    if not node:
        return float("-inf")
    maxleft = tree_max(node.left)
    maxright = tree_max(node.right)
    return max(node.key, maxleft, maxright)


def tree_min(node):
    if not node:
        return float("inf")
    minleft = tree_min(node.left)
    minright = tree_min(node.right)
    return min(node.key, minleft, minright)


def verify(node):
    if not node:
        return True
    if (tree_max(node.left) <= node.key <= tree_min(node.right) and
            verify(node.left) and verify(node.right)):
        return True
    else:
        return False


root = Node(5, "a")
root.left = Node(2, "b")
root.left.left = Node(1, "c")
root.left.right = Node(4, "d")
root.right = Node(8, "e")
root.right.left = Node(6, "f")
root.right.right = Node(10, "g")

print(verify(root))  # prints True, since this tree is valid

root = Node(5, "a")
root.left = Node(2, "b")
root.left.left = Node(3, "c")
root.left.right = Node(4, "d")
root.right = Node(8, "e")
root.right.left = Node(6, "f")
root.right.right = Node(7, "g")

print(verify(root))  # prints False, since 15 is to the left of 10

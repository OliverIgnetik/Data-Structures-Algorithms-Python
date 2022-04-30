# approach 1 - inorder traversal vs sort

class Node:
    def __init__(self, k, val):
        self.key = k
        self.value = val
        self.left = None
        self.right = None


def inorder(tree):
    if tree != None:
        inorder(tree.left)
        tree_vals.append(tree.value)
        inorder(tree.right)


def sort_check(tree_vals):
    return tree_vals == sorted(tree_vals)


tree = Node("Hello", 10)
tree.left = Node("Five", 5)
tree.right = Node("Thirty", 30)

tree_vals = []

inorder(tree)
print('Validation BST : ', sort_check(tree_vals))


# approach 2 tracking valid values for nodes

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


# This solution is probably the easiest
def verify_BFS(node):
    """
    NOTE: this approach won't catch the test case that only the recursive verify function can since
    we are only checking the current node against it's left and right children with no reference to the
    rest of the tree
    """
    queue = []
    queue.append(node)

    while (len(queue) > 0):
        cur = queue.pop(0)
        if (cur.left):
            if (cur.left.key < cur.key):
                queue.append(cur.left)
            else:
                return False
        if (cur.right):
            if (cur.right.key > cur.key):
                queue.append(cur.right)
            else:
                return False
    return True


####################################### TEST #################################
root = Node(5, "a")
root.left = Node(2, "b")
root.left.left = Node(1, "c")
root.left.right = Node(4, "d")
root.right = Node(8, "e")
root.right.left = Node(6, "f")
root.right.right = Node(10, "g")

print(verify(root))  # prints True, since this tree is valid
print(verify_BFS(root))

root = Node(5, "a")
root.left = Node(2, "b")
root.left.left = Node(3, "c")
root.left.right = Node(4, "d")
root.right = Node(8, "e")
root.right.left = Node(6, "f")
root.right.right = Node(7, "g")

print(verify(root))  # prints False
print(verify_BFS(root))

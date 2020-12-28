import collections


class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


def levelOrderPrint(tree):
    if not tree:
        return
    nodes = collections.deque([tree])
    currentCount, nextCount = 1, 0
    while len(nodes) != 0:
        currentNode = nodes.popleft()
        currentCount -= 1
        print(currentNode.val)
        if currentNode.left:
            nodes.append(currentNode.left)
            nextCount += 1
        if currentNode.right:
            nodes.append(currentNode.right)
            nextCount += 1
        if currentCount == 0:
            # finished printing current level
            print('\n')
            currentCount, nextCount = nextCount, currentCount


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
trimmedBST = trimBST(root, 2, 20)
levelOrderPrint(trimmedBST)

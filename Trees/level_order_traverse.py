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
    # there is 1 node at the root level
    currentCount, nextCount = 1, 0
    level = 1
    while len(nodes) != 0:
        currentNode = nodes.popleft()
        currentCount -= 1
        print(f' value : {currentNode.val} level : {level}')
        if currentNode.left:
            nodes.append(currentNode.left)
            # add node to next count
            nextCount += 1
        if currentNode.right:
            nodes.append(currentNode.right)
            # add node to next count
            nextCount += 1
        if currentCount == 0:
            # finished printing current level
            print('\n')
            # eg. after level 1
            # currentCount = 2
            # nextCount = 0 (because the currentCount is zero by this point)
            currentCount, nextCount = nextCount, currentCount
            level += 1


root = Node(10)
root.left = Node(5)
root.left.left = Node(2)
root.left.right = Node(7)
root.right = Node(30)
root.right.right = Node(35)
root.right.left = Node(28)
levelOrderPrint(root)

from tkinter.tix import Tree
from typing import Union, List

Num = Union[int, float]


class TreeNode:
    # Example of forward annotation
    def __init__(self, value: Num, children: List['TreeNode'] = []) -> None:
        self.value = value
        self.children = children

    def add_child(self, childNode: 'TreeNode'):
        self.children.append(childNode)


class Solution:
    """
    Time: O(N)
    Space: O(N)
    """

    def leafSum(self, node: TreeNode):
        if (node == None):
            return 0
        if len(node.children) == 0:
            return node.value
        else:
            total = 0
            for child in node.children:
                total += self.leafSum(child)
            return total


root = TreeNode(1, [TreeNode(3, [TreeNode(4), TreeNode(1)]),
                TreeNode(5, [TreeNode(4), TreeNode(4)])])
root.add_child(TreeNode(-5, [TreeNode(-10, [TreeNode(1)])]))

s = Solution()
print(s.leafSum(root))

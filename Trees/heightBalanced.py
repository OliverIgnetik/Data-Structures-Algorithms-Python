"""
Test If A Binary Tree Is Height Balanced
A binary tree is "height-balanced" if at every node the left and right subtree height do not differ by more than 1.

Given a binary tree, determine if it is height-balanced.

Example 1:
Input:
           1
          / \
         2   3

Output: true
Explanation: The root node has a left subtree height of 1 and a right subtree height of 1. Each leaf node has left & right subtree heights of 0.

Example 2:
Input:
           1
          / \
         2   3
            / \
           4   5

Output: true
Explanation:
| Node{i} | left sub height | right sub height |
|    1    |        1        |         2        |
|    2    |        0        |         0        |
|    3    |        1        |         1        |
|    4    |        0        |         0        |
|    5    |        0        |         0        |

Example 3:
Input:
           1
          / \
         2   3
            / \
           4   5
                \
                 6
Output: false
Explanation: Breaks balance at root, |1 - 3| = 2 > 1.
| Node{i} | left sub height | right sub height |
|    1    |        1        |         3        |
|    2    |        0        |         0        |
|    3    |        1        |         2        |
|    4    |        0        |         0        |
|    5    |        0        |         1        |
|    6    |        0        |         0        |
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        """
        Interface
        ----
        :type root: TreeNode
        :rtype: bool

        Complexity
        ----
        Time : O(N)
        Space : O(logN)
        """
        return self.check_balanced(root).is_balanced

    def check_balanced(self, root):
        # root that is None has height = -1 and is balanced
        if root == None:
            return BalanceStatusWithHeight(True, -1)

        # get the left height and check if it is balanced
        left_result = self.check_balanced(root.left)
        if not left_result.is_balanced:
            return left_result

        # get the right height and check if it is balanced
        right_result = self.check_balanced(root.right)
        if not right_result.is_balanced:
            return right_result

        # balance condition has to be true at every node
        subtrees_are_balanced = abs(
            left_result.height - right_result.height) <= 1

        # NOTE: we have to add one to account for this node
        # In the case where both the left and right children are leaves we get height = max(0,0) + 1
        height = max(left_result.height, right_result.height) + 1

        # pass the information up the recursive call stack
        return BalanceStatusWithHeight(subtrees_are_balanced, height)


class BalanceStatusWithHeight:
    def __init__(self, is_balanced, height):
        self.is_balanced = is_balanced
        self.height = height


"""
           1
          / \
         2   3
            / \
           4   5
          /
         7
"""

head = TreeNode(1, TreeNode(2), TreeNode(
    3, TreeNode(4, TreeNode(7)), TreeNode(5)))
s = Solution()
print(s.isBalanced(head))

"""
Lowest Common Ancestor In A BST
Given the root of a binary search tree root and the value of two nodes x and y, 
return a reference to their lowest common ancestor.
NOTE: by lowest we mean the ancestor with greatest depth relative to the root

Example 1:
Input:
root = Node{50}
x = 1
y = 101
                  50
                /    \
              25     100
             /  \   /   \
            1   27 80   101

Output: Node{50}
Explanation: The root is the lowest common ancestor between Node{1} and Node{101}. 
It is also the highest common ancestor between these two nodes.

Example 2:
Input:
root = Node{50}
x = 1
y = 27
                  50
                /    \
              25     100
             /  \   /   \
            1   27 80   101

Output: Node{25}
Explanation: The Node{25} is the lowest common ancestor between Node{1} and Node{27}. 
Node{50} is also an ancestor of both nodes but it is not the lowest one.

Extension:
Can you do this iteratively as well?
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root, x, y):
        """
        Overview
        ---- 
        Given a root node and two unique values that exist in a BST find the 
        lowest common ancestor of both nodes

        Interface 
        ----
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: TreeNode

        Approach 
        ----
        NOTE: CASE TO RETURN CURRENT NODE
        1. Look for a node in which one of the values x or y is greater and the other 
        is less then the node in question

        2. One value is the current node value and the other is greater or less then 
        the current node

        Complexity
        ----
        Time : O(logN) is the longest path one of the nodes will have 
        Space : O(logN)

        """
        # 1) Both values are less than our root value.
        # look in the left subtree
        if (x < root.val and y < root.val):
            return self.lowestCommonAncestor(root.left, x, y)

        # 2) Both values are greater than our root value.
        # look in the right subtree
        if (x > root.val and y > root.val):
            return self.lowestCommonAncestor(root.right, x, y)

        """
        3) One of x or y is equal to the root.
        OR
        4) NOTE: it is a splitting point 
        One of x or y is less than root and the other is greater than root.
        """
        return root


"""
                  50
                /    \
              25     100
             /  \   /   \
            1   27 80   101
"""

root = TreeNode(50, TreeNode(25, TreeNode(1), TreeNode(27)),
                TreeNode(100, TreeNode(80), TreeNode(101)))

s = Solution()
# we should expect 25 the root
print(s.lowestCommonAncestor(root, 1, 27))
# answer would be 100
print(s.lowestCommonAncestor(root, 80, 101))

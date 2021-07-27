"""
Test If A Binary Tree Is Symmetric
Given a binary tree, test if it is symmetric both in value and in structure.
NOTE: this is a binary tree not a binary search tree

 Example 1:
Input: 
       2
     /   \
    1     1

Output: true

 Example 2:
Input: 
         4
       /   \
      2     2
     / \   /
    1   2 2

Output: false

 Example 3:
Input: 
       X (empty tree)

Output: true
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        """
        Interface
        ----
        :type root: TreeNode
        :rtype: bool

        Approach 
        ----
        1. The tree is symmetric the left subtree and right subtree are symmetric about the center

        2. we require:
        - right child of left subtree = left child of right subtree
        - left child of left subtree = right child of right subtree

        Complexity
        ----
        Time : O(N) we have to touch all nodes
        Space : O(logN) depth of the stack
        """
        if root == None:
            return True

        return self.check_symmetry(root.left, root.right)

    def check_symmetry(self, left_subtree_root, right_subtree_root):
        # basecase both are None
        if (left_subtree_root == None and right_subtree_root == None):
            return True
        # if both of the subtrees under consideration are not None then check them
        if (left_subtree_root != None and right_subtree_root != None):
            return (
                left_subtree_root.val == right_subtree_root.val and
                # inner subtrees must be symmetric
                self.check_symmetry(left_subtree_root.right, right_subtree_root.left) and
                # outer outer subtrees must be symmetric
                self.check_symmetry(left_subtree_root.left,
                                    right_subtree_root.right)
            )
        # one of the subtrees is None therefor the tree is not symmetric
        return False


"""
       2
     /   \
    1     1
   / \   / 
  2   3 3   
"""

head = TreeNode(2, TreeNode(1, TreeNode(2), TreeNode(3)),
                TreeNode(1, TreeNode(3), None))
s = Solution()
print(s.isSymmetric(head))

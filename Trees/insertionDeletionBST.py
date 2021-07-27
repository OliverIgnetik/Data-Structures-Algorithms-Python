"""
Insertion and Deletion In A BST
Given a binary search tree, you will implement two methods.
Insert - given a root node, and a value, insert the value and return the updated bst
Delete - given a root node, and a value, delete this value and return the updated bst

Example 1:
Input:
tree = [ ]
insert  1

Output:
[ 1 ]

Explanation:
Insert node 1 into the empty tree.

Example 2:
Input:
tree = [2, 1, 5, 3]
insert 7

Output:
[2, 1, 5, 3, 7]

Explanation
   2             2
  / \           / \
 1   5   -->   1   5
    /             / \
   3             3   7


Example 3:
Input:
tree = [7, 3, 8, 2, 4]
delete 4

Output:
[7, 3, 8, 2]

Explanation
    7             7
   / \           / \
  3   8   -->   3   8
 / \           /
2   4         2

Constraints
Result should stll be a BST after any deletion/insertion.
BST will contain distinct values.
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    """
    Complexity
    Time : O(logN)
    Space : O(logN)
    """

    def insertIntoBST(self, root, value):
        if root == None:
            return TreeNode(value)
        if value < root.value:
            root.left = self.insertIntoBST(root.left, value)
        else:
            root.right = self.insertIntoBST(root.right, value)

        return root

    def deleteNode(self, root, value):

        if root == None:
            return None

        if value < root.value:
            root.left = self.deleteNode(root.left, value)
        elif value > root.value:
            root.right = self.deleteNode(root.right, value)
        else:
            """
            We have found the node that needs to be removed, we have 3 cases:

            1.) Empty left subtree: We can just return the right subtree of the node,
            cutting root itself out

            2.) Empty right subtree: We can just return the left subtree of the node,
            cutting root itself out

            3.) Non - empty left and right subtrees: We want the next node in the inorder
            traversal after this node to take this node's place.

            Hop to the right and go all the way left to get the next item in the inorder
            traversal.
            """
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left

            nextInorderNode = self.getNextInorderNode(root.right)
            root.value = nextInorderNode.value

            """
            Now update root's right subtree by removing the actual 'nextInorderNode'
            object from it since we just placed its value into root
            """
            root.right = self.deleteNode(root.right, nextInorderNode.value)

            return root

    def getNextInorderNode(self, root):
        if root == None:
            return None

        curr = root
        while curr.left != None:
            curr = curr.left

        return curr


head = TreeNode(2)
s = Solution()
s.insertIntoBST(head, 1)
s.insertIntoBST(head, 5)
s.insertIntoBST(head, 3)
s.insertIntoBST(head, 7)

s.deleteNode(head, 5)
print(head)

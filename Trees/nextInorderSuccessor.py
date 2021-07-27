"""
Compute A Node's Inorder Successor
Given a binary tree and an integer value x, return the inorder successor of the node with value x.

In-order Successors:
The in-order successor of a node in binary tree is defined to be the next node in the in-order traversal of the Binary Tree.

Example 1:
Input: 
          1 
        /   \
      5      8
    /  \      \
   7    3      2
        /       \
       6        10

x = 6

Output: Node{3}

Explanation: The in-order traversal of the tree is [7,5,6,3,1,8,2,10]. 3 comes after 6.

Example 2:
Input: 
          1 
        /   \
      5      8
    /  \      \
   7    3      2
        /       \
       6        10

x = 10

Output: null
Explanation: The in-order traversal of the tree is [7,5,6,3,1,8,2,10]. 10 is the last node.

Constrains:
A node with the value x will always exist
All nodes will have unique values
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.setParents(head)

    def setParents(self, head, parent=None):
        # recursive implementation of setParents
        # NOTE: it's much easier to do this with a queue
        # base case
        if head == None:
            return
        head.parent = parent
        if head.left:
            self.setParents(head.left, head)
        if head.right:
            self.setParents(head.right, head)

        return head

    def inorderSuccessor(self, head, value):
        """
        Complexity
        ----
        Time : O(logN)
        Space : O(1)
        """
        # find the node we are interested in
        # NOTE: BASECASE if we hit a node with None return None
        if head != None:
            if head.value == value:
                return self.inOrderSuccessorSubroutine(head)
            # look in lhs subtree
            lhs = self.inorderSuccessor(head.left, value)
            # look in rhs subtree
            rhs = self.inorderSuccessor(head.right, value)

            # it will be in one or the other
            if lhs != None:
                return lhs
            elif rhs != None:
                return rhs
        return None

    def inOrderSuccessorSubroutine(self, head):
        searchPointer = head
        # CASE 1 : if the node has a right subtree
        # NOTE: the successor will the the left most item
        if searchPointer.right != None:
            searchPointer = searchPointer.right
            while searchPointer.left != None:
                searchPointer = searchPointer.left
            return searchPointer

        # CASE 2 : no right subtree
        # NOTE: this can be explained using the inorder traversal = l n r
        # we traverse up the tree until we hit a node which is a left child
        # this node's parent will be the next inorder node
        while (searchPointer.parent != None and searchPointer.parent.right == searchPointer):
            searchPointer = searchPointer.parent

        # NOTE: that parent which called the inorder traversal on its left subtree is the next node
        return searchPointer.parent


"""
          1 
        /   \
      5      8
    /  \      \
   7    3      2
        /       \
       6        10
"""

head = TreeNode(1, TreeNode(5, TreeNode(7), TreeNode(3, TreeNode(6))),
                TreeNode(8, None, TreeNode(2, None, TreeNode(10))))
s = Solution()
# we expect 1 because 5 is the node that has exhausted it's right subtree call
# NOTE: l n r
# 5 is waiting on r
# 1 is waiting on l
s.inorderSuccessor(head, 3)
print()

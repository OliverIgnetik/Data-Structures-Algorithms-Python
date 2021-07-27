"""
Inorder Traversal Without Recursion
Given a binary tree as input, return its inorder traversal.

Example 1:
Input:
       2
     /   \
    1     3

Output: [1,2,3]

Example 2:
Input:
         10
       /    \
      2      4
     / \      \
    5   8     44

Output: [5,2,8,10,4,44]

Constraints
You may not use any recursion
"""

# A binary tree node


class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Iterative function for inorder tree traversal

############################### GEEKSFORGEEKS IMPLEMENTATION ###############################


def inOrder(root):

    # Set current to root of binary tree
    current = root
    stack = []  # initialize stack
    done = 0

    while True:

        # Reach the left most Node of the current Node
        if current is not None:

            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            stack.append(current)

            current = current.left

        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        elif(stack):
            current = stack.pop()
            print(current.data, end=" ")

            # We have visited the node and its left
            # subtree. Now, it's right subtree's turn
            current = current.right

        else:
            break

    print()
############################### GEEKSFORGEEKS IMPLEMENTATION ###############################

############################### BACK2BACKSWE IMPLEMENTATION ###############################


class Solution:
    def inorderTraversal(self, root):
        """
        Interface
        ----
        :type root: TreeNode
        :rtype: list of int

        Complexity
        ----
        Time : O(N)
        Space : O(logN)
        """
        inorder_traversal = []
        stack = []

        curr = root
        while (len(stack) != 0 or curr != None):
            """
            L N R
            Left: go as left as possible, the stack keeps the history of
            nodes that need searching
            """
            # NOTE: PROCESS L
            while curr != None:
                stack.append(curr)
                curr = curr.left

            # Node: curr is None now, investigate the node on the top of the stack
            # NOTE: PROCESS N
            curr = stack.pop()
            inorder_traversal.append(curr.data)

            # Right: now do this same routine on this node's right subtree
            # NOTE: PROCESS R
            curr = curr.right

        return inorder_traversal
############################### BACK2BACKSWE IMPLEMENTATION ###############################


""" 
Constructed binary tree is
		1
	   / \
      2	  3
     / \
    4   5 
"""

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder(root)

s = Solution()
print(s.inorderTraversal(root))

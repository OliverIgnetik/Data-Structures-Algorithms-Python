"""
Compute The LCA With Parent Pointers
Given references to 2 nodes, n1 and n2, in a binary tree 
(where each node records a reference to its parent in a .parent pointer),
return a reference to the lowest common ancestor of n1 and n2.

Example 1:
Input:
n1 = Node{5}
n2 = Node{9}
            3
          /   \
         4     6
        / \     \
       5   9     7

Output: Node{4}

Example 2:
Input:
n1 = Node{5}
n2 = Node{7}
            3
          /   \
         4     6
        / \     \
       5   9     7

Output: Node{3} (the root)

Example 3:
Input:
n1 = Node{4}
n2 = Node{9}
            3
          /   \
         4     6
        / \     \
       5   9     7

Output: Node{4}
Explanation: Node{4} is an ancestor to itself as well as Node{9}

Constraints:
n1 and n2 are guaranteed to be in the tree
All node values will be unique
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def setParentPointers(self, head):
        q = deque()
        q.append([head, None])
        while len(q) != 0:
            curr_node, parent = q.popleft()
            curr_node.parent = parent
            if curr_node.right:
                q.append([curr_node.right, curr_node])
            if curr_node.left:
                q.append([curr_node.left, curr_node])
        return head

    def lcaWithParentPointers(self, n1, n2):
        """
        Interface
        ----
        :type n1: ParentTreeNode
        :type n2: ParentTreeNode

        Approach 
        ----
        Climbing Parent Pointers
        1. We record the ancestors of one of the nodes in a structure using hashing
        to record key locations. 

        2. We then climb from the other node (up the parent pointers) and return as
        soon as the node is found in the ancestor structure.

        Complexity
        ----
        Time : traversal O(logN) if the tree is unbalanced we will have O(N)
        Space : O(N) we can have all the nodes in the tree
        """
        head = self.setParentPointers(head)

        ancestors = {}

        # go up the n1 path
        while n1 is not None:
            ancestors[n1] = True
            n1 = n1.parent

        # go up the n2 path as soon as we see a node that we saw on the n1 path
        # return that node
        while n2 is not None:
            if n2 in ancestors:
                return n2

            n2 = n2.parent

        return None

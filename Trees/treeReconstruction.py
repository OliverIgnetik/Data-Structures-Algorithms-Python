"""
Tree Reconstruction
Given the preorder and inorder traversals of a tree, construct the binary tree.

Example 1:
Input: 
preorder [ ] 
inorder  [ ]

Output: 
[ ]

Explanation:
The binary tree is empty. 

Example 2:
Input: 
preorder [2, 1, 3] 
inorder  [1, 2, 3]

Output: 
[2, 1, 3]

    2 
   / \
  1   3

Example 3:
Input: 
preorder [7, 1, 12, 15, 3]
inorder  [1, 7, 15, 12, 3]

Output: 
     7
    / \
   1  12 
      / \       
     15  3
"""


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.preorder_index = 0

    def buildTree(self, preorder, inorder):
        """
        Interface
        ----
        :type preorder: list of int
        :type inorder: list of int
        :rtype: TreeNode

        Approach 
        ----
        1. If we are given the preorder and inorder traversals 
        this combination corresponds to a unique binary tree.
        * preorder - n l r 
        * inorder - l n r
        * postorder - l r n

        2. The preorder traversal can tell us the root of the tree, once we know the root of the tree
        we can traverse the inorder traversal until we hit the root of the tree which we now know from 
        the preorder traversal. Furthermore, the inorder traversal also tells us what's in the 
        right subtree aswell. 

        3. We can recursively call this same subroutine on the each
        decision space until we build the whole tree. 

        4. We use the nature of the traversals to tell us about roots of subtrees and constraints for the 
        decision space. 

        Complexity
        ----
        Time : O(N) We have to touch N nodes
        Space : O(N) the call stack depth is not the dominant contributing runtime factor 
        """

        inorder_node_to_index = {}
        # build the hashtable for values in the inorder traversal and their index in the traversal
        # key : inorder[i], value : i
        for i in range(0, len(inorder)):
            inorder_node_to_index[inorder[i]] = i

        # pass in a memory reference to preorder and inorder
        return self.build(preorder, inorder, 0, len(inorder) - 1, inorder_node_to_index)

    def build(
        self,
        preorder,
        inorder,
        inorder_start,
        inorder_end,
        inorder_node_to_index
    ):
        # base case
        # NOTE: we have exhausted the search space
        if inorder_start > inorder_end:
            return None
        # construct the root node and increment the self.preorder_index
        node_value = preorder[self.preorder_index]
        node = TreeNode(node_value)
        self.preorder_index += 1
        # where is the root in the inorder traversal
        inorder_index = inorder_node_to_index[node_value]

        # build the left subtree using values to the left of the root value in the inorder traversal
        node.left = self.build(preorder, inorder, inorder_start,
                               inorder_index - 1, inorder_node_to_index)
        # build the right subtree using values to the right of the root value in the inorder traversal
        node.right = self.build(preorder, inorder, inorder_index + 1,
                                inorder_end, inorder_node_to_index)

        return node


preorder = [2, 1, 3]
inorder = [1, 2, 3]
s = Solution()
head = s.buildTree(preorder, inorder)
print(head)

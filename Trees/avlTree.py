# Python code to insert a node in AVL tree
"""
------------------------------
NOTES
References

- https://www.geeksforgeeks.org/avl-tree-set-1-insertion/ GeeksToGeeks
- https://www.youtube.com/watch?v=vRwi_UcZGjU&t=353s BackToBackSWE AVL trees
- https://bradfieldcs.com/algos/trees/avl-trees/ BradfieldCS 
------------------------------
Overview

AVL trees are BSTs that are self-balancing. 
The reason why this is so beneficial is because BSTs
have linear complexity when the tree becomes skewed.
By doing this we can ensure a linear search complexity.

AVL trees use a rebalancing threshold to check the difference in heights 
between subtrees. At a node we can have:

- left-heavy (left tree has a greater height)
- right-heavy (right tree has a greater height)
- balanced (equal height sub-trees)

------------------------------
RECURSIVE DEFINITION OF HEIGHT

H(null) = -1
H(single node) = 0

H(n) = max(H(T_L), H(T_R)) + 1 
------------------------------
AVL PROPERTY

NOTE: EVERY NODE MUST SATISFY THIS PROPERTY

B(N) = H(T_L) - H(T_R)

+ve LEFT HEAVY

-ve RIGHT HEAVY

|B(n)| <= 1
------------------------------
ROTATIONS

They are focused around two critical nodes. All the other nodes moves around them

1. LEFT HEAVY

2. LEFT HEAVY WITH LEFT CHILD THAT IS RIGHT HEAVY

3. RIGHT HEAVY

4. RIGHT HEAVY WITH CHILD THAT IS LEFT HEAVY

"""
"""
AVL Trees & Rotations
An AVL Tree is a self-balancing binary search tree.

Given an array of integers items and a threshold threshold, return the tree resulting from 
performing insertions of each element items[i] while maintaining the AVL balance property 
with threshold threshold.

Example 1:
Input:
items = [1,2,3]
threshold = 1

Output:
          2
        /   \
       1     3

Explanation:
        1
         \
          2
           \
            3

Do a Left Rotation
Left Rotation (Rooted On 1):

          2
        /   \
       1     3

Example 2:
Input:
items = [3, 1, 2]
threshold = 1

Output:
          2
        /   \
       1     3

Explanation:
        3
       /
      1
       \
        2

Do a Left-Right Rotation
Left Rotation (Rooted On 1):

        3
       /
      2
     /
    1

Right Rotation (Rooted On 3):

          2
        /   \
       1     3


Constraints:
All values to be inserted will be unique
"""


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertAVL(self, items, threshold):
        """
        Interface
        ----
        :type items: list of int
        :type threshold: int
        :rtype: TreeNode
        """
        if not items:
            return None

        root = AVLNode(items[0])

        for idx in range(1, len(items)):
            # save new the root after rotations etc.
            root = self.insert(root, items[idx], threshold)

        # O(n) conversion for testing reasons
        return self.convert_avl_nodes_to_treenode(root)

    def insert(self, node, key, threshold):
        # NOTE: BASECASE
        if not node:
            return AVLNode(key)

        # regular BST insertion
        if (key < node.val):
            node.left = self.insert(
                node.left, key, threshold)  # insert to the left
        else:  # key >= node.val
            node.right = self.insert(node.right, key, threshold)

        # ONCE WE BUBBLE BACK UP FROM RECURSION CHECK THE HEIGHT AGAIN
        # When we return to this node going up in the recursion
        # NOTE: this won't dril all the way down because we have moved back up the recursive calls we already have this information
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        # find the balance factor
        # NOTE: B = H(L) - H(R)
        balance = self.get_balance(node)

        # ROTATIONS
        # the key is maintaining the BST property
        # NOTE: left heavy +ve
        if balance > threshold:  # Did we create a left imbalance? > threshold, positive
            # right rotation
            if self.get_balance(node.left) >= 0:
                node = self.rotate_right(node)
            else:
                # left-right rotation
                node = self.rotate_left_right(node)  # node.left is right-heavy
        # NOTE: right heavy -ve
        elif balance < -threshold:  # Did we create a right imbalance? < -threshold, negative
            # left rotation
            if self.get_balance(node.right) <= 0:
                node = self.rotate_left(node)
            # right-left rotation
            else:
                node = self.rotate_right_left(node)  # node.right is left-heavy

        return node

    # For left-heavy rebalance
    def rotate_right(self, node):
        """
        x and y are the crucial nodes
        BEFORE
        ----
            x
           / \
          y   p  
         / \
        r   b

        AFTER
        ----
            y
           / \
          r   x  
             / \
            b   p

        - Notice p and r do not change
        """

        # x
        left_temp = node.left
        # x.left = y.right
        node.left = left_temp.right
        # y.right = x
        left_temp.right = node

        # Update heights of rotated nodes based on subtree heights
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        left_temp.height = 1 + max(self.get_height(left_temp.left),
                                   self.get_height(left_temp.right))

        # y is now the head
        return left_temp

    # For right-heavy rebalance
    def rotate_left(self, node):
        """
        BEFORE
        ----
            y
           / \
          r   x  
             / \
            b   p

        AFTER
        ---- 
            x
           / \
          y   p  
         / \
        r   b
        """
        right_temp = node.right

        node.right = right_temp.left
        right_temp.left = node

        # Update heights of rotated nodes based on subtree heights
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
        right_temp.height = 1 + max(self.get_height(right_temp.left),
                                    self.get_height(right_temp.right))

        return right_temp

    # For left-heavy rebalance (& node.left has negative balance, right-heavy)
    # NOTE: rotate the left child left first and then rotate node right
    def rotate_left_right(self, node):
        # left child is right heavy
        node.left = self.rotate_left(node.left)

        return self.rotate_right(node)

    # For right-heavy rebalance (& node.right has positive balance, left-heavy)
    # NOTE: rotate the right child right first and then rotate node left
    def rotate_right_left(self, node):
        node.right = self.rotate_right(node.right)

        return self.rotate_left(node)

    def get_balance(self, node):
        if not node:
            return 0

        # NOTE: B = H(L) - H(R)
        return self.get_height(node.left) - self.get_height(node.right)

    def get_height(self, node):
        if not node:
            return -1

        return node.height

    # O(n) conversion to TreeNode type for testing reasons
    def convert_avl_nodes_to_treenode(self, avl_node):
        if not avl_node:
            return None

        root = TreeNode(avl_node.val)

        root.left = self.convert_avl_nodes_to_treenode(avl_node.left)
        root.right = self.convert_avl_nodes_to_treenode(avl_node.right)

        return root

    '''
    Side-Node:
        We can get balance this way, but it will make balance lookups O(n)
        because subtree height lookups will be O(n). Storing current height for each
        node is a must to maintain O(1) balance lookup, and subsequently O(log(n))
        insert (rotations are O(1), etc.).

    def get_balance(self, node):
        return self.height_at_node(node.left) - self.height_at_node(node.right)

    def height_at_node(self, node):
        if not node:
            return -1

        return max(self.height_at_node(node.left), self.height_at_node(node.right)) + 1
    '''


class AVLNode:
    def __init__(self, val):
        """
        By keeping the height field on the node we ensure O(logN) operations
        """
        self.val = val
        self.height = 0
        self.left = None
        self.right = None


# tests
s = Solution()
root = None

root = s.insertAVL(root, [1, 2, 3], 1)
print(root)

"""
The unbalanced tree would be 
		1
         \
          2
           \
            3
We convert this to :
          2
        /   \
       1     3
"""

"""
Given a binary tree as input return its level order traversal.

A "level order traversal" is a level-by-level visitation of each node in the tree from top-to-bottom and left-to-right.

Example 1:
Input:
         2
        / \
       3   4
Output:
[
  [2],
  [3, 4]
]

Example 2:
Input:
         1
        / \
       2   3
        \   \
         4   5
Output:
[
  [1],
  [2, 3],
  [4, 5]
]
"""
from collections import deque


class Solution:
    def levelOrderTraversal(self, root):
        '''
        :type root: TreeNode
        :rtype: list of list of int

        Complexity 
        ---- 
        N = number of nodes
        Time : O(N) we touch every node once
        Space : O(2^N) Maximum width of tree
        '''
        res = []
        q = deque()
        q.append(root)
        current_level_nodes, next_level_nodes = 1, 0
        level_nodes = []
        while len(q) != 0:
            node = q.popleft()
            level_nodes.append(node.value)
            if node.left:
                q.append(node.left)
                next_level_nodes += 1
            if node.right:
                q.append(node.right)
                next_level_nodes += 1

            current_level_nodes -= 1

            if current_level_nodes == 0:
                res.append(level_nodes)
                level_nodes = []
                current_level_nodes, next_level_nodes = next_level_nodes, current_level_nodes
        return res

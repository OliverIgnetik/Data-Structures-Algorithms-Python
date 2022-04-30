"""
All Paths with Sum equal to 'K'
All Paths With Sum
Give a binary tree and a target sum sum, count the total unique paths
that sum to the target sum sum.

Example 1:
Input:  sum = 10

           5
          /
        5
      /   \
     1      0

Output: 2
Explanation:

           5              5
          /              /
         5              5
       /   \          /   \
      1     0        1     0
"""
# code reference : https://www.geeksforgeeks.org/print-k-sum-paths-binary-tree/


def printVector(v, i):
    """
    utility function to print contents of
    a vector from index i to it's end
    """
    for j in range(i, len(v)):
        print(v[j], end=" ")
    print()


# Binary Tree Node
""" utility that allocates a newNode
with the given key """


class newNode:

    # Construct to create a newNode
    def __init__(self, key, left=None, right=None):
        self.data = key
        self.left = left
        self.right = right


def printKPathUtil(root, path, k):
    """
    This function prints all paths
    that have sum k

    Approach
    ----
    EASY WAY TO UNDERSTAND THIS
    1. We drill down all the way to the leaves using a preorder traversal N L R

    2. Once we are at a leaf we can check the path thanks to the preorder traversal

    3. We then pop the left leaf from the stack we can check the right leaf

    4. We have to traverse the stack in a backwards manner because we want to check ALL paths
    """

    # empty node
    if (not root):
        return

    # add current node to the path
    path.append(root.data)

    # check if there's any k sum path
    # in the left sub-tree.
    printKPathUtil(root.left, path, k)

    # check if there's any k sum path
    # in the right sub-tree.
    printKPathUtil(root.right, path, k)

    # check if there's any k sum path that terminates at this node
    # Traverse the entire path as there can be negative elements too
    f = 0
    # notice we read the path information in reverse
    for j in range(len(path) - 1, -1, -1):
        f += path[j]

        # If path sum is k, print the path
        if (f == k):
            printVector(path, j)

    # Remove the current element from the path
    # we have finished exploring this area of the tree
    path.pop(-1)


def printKPath(root, k):
    """
    Approach
    ----
    1. The basic idea to solve the problem is to do a preorder traversal of the given tree.

    2. We also need a container (vector) to keep track of the path that led to that node.

    3. At each node we check if there are any path that sums to k, if any we print the path
    and proceed recursively to print each path. NOTE: it is key to check the property at each node

    Complexity
    ----
    Time : O(n*h*h)  , as maximum size of path vector can be h
    Space : O(h)
    """

    path = []
    printKPathUtil(root, path, k)


"""
           5
          /
         5
        / \
       1   0

"""


class AlternativeSolution:
    def pathSum(self, root, sum):
        prefixSumToTotalPrefixes = {}
        prefixSumToTotalPrefixes[0] = 1
        return self.findPathSum(root, 0, sum, prefixSumToTotalPrefixes)

    def findPathSum(self, root, rootToNodeSum, target, prefixSumToTotalPrefixes):
        if root == None:
            return 0

        rootToNodeSum += root.val

        amountToCompensateFor = rootToNodeSum - target
        totalPathsEndingAtThisNode = prefixSumToTotalPrefixes.get(
            amountToCompensateFor, 0)
        totalPathsWithSum = prefixSumToTotalPrefixes.get(rootToNodeSum, 0)
        prefixSumToTotalPrefixes[rootToNodeSum] = totalPathsWithSum + 1

        totalCompletedPathsInThisSubtree = totalPathsEndingAtThisNode + \
            self.findPathSum(root.left, rootToNodeSum,
                             target, prefixSumToTotalPrefixes) + self.findPathSum(root.right, rootToNodeSum, target, prefixSumToTotalPrefixes)

        prefixSumToTotalPrefixes[
            rootToNodeSum] = prefixSumToTotalPrefixes.get(rootToNodeSum, 0) - 1
        return totalCompletedPathsInThisSubtree


head = newNode(5, newNode(5, newNode(1, None, newNode(5)),
               newNode(0, None, newNode(3, newNode(2)))), newNode(0, None, newNode(2)))
# we expect 1
k = 6
printKPath(head, k)

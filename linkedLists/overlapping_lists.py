"""
Testing For Overlapping Lists (No Cycles)
Given two acyclic linked lists (no cycles) l1 and l2, determine if they overlap.

If they overlap return the node that marks the merge point of the two lists, otherwise, return null.

Example 1:
Input:

1 -> 2 -> 3 -> X
1 -> 2 -> 3 -> 4 -> 5 -> X

Output: null

Example 2:
Input:

1 -> 2 -> 3
           \
            4 -> 6 -> 8 -> X
           /
1 -> 2 -> 3

Output: Node{4}
"""


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.__class__.__name__}({self.data},{self.next})'


class Solution:
    def overlappingList(self, l1: Node, l2: Node) -> Node:
        """
        Complexity
        ----
        Time : O(L1 + L2)
        Space : O(1)
        """
        intersection_node = None

        if not l1 or not l2:
            return None

        # set up dummy pointers
        l1_dummy = l1
        l2_dummy = l2

        while l1_dummy and l2_dummy:
            next_l1 = l1_dummy.next
            next_l2 = l2_dummy.next
            # what about the case when both of them are None
            if next_l1 == None and next_l2 == None:
                intersection_node = None
                return intersection_node
            # general case
            if next_l1 is next_l2:
                intersection_node = next_l1
                return intersection_node

            # increment
            l1_dummy = l1_dummy.next
            l2_dummy = l2_dummy.next

        return intersection_node


l3 = Node(4, Node(6, Node(8, None)))
l1 = Node(1, Node(2, Node(3, l3)))
l2 = Node(1, Node(2, Node(3, l3)))
s = Solution()

print(s.overlappingList(l1, l2))

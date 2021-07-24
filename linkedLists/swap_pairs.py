"""
Swap Linked List Nodes In Pairs
Given a singly linked list, reorder its nodes such that pairs of consecutive nodes are interchanged.

Example 1:
Input:  'a' -> 'b' -> 'c' -> 'd' -> 'e' -> 'f' -> X
Output: 'b' -> 'a' -> 'd' -> 'c' -> 'f' -> 'e' -> X

Example 2:
Input:  'a' -> 'b' -> 'c' -> 'd' -> 'e' -> X
Output: 'b' -> 'a' -> 'd' -> 'c' -> 'e' -> X

Example 3:
Input:  'a' -> X
Output: 'a' -> X

Follow-up:
If you have not already, can you interchange the actual nodes themselves instead of just the values?

Note:
We will only test for values, we will not test for the actual node memory addresses being interchanged
"""


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Solution:
    def swap_pair(self, n1, n2):
        n2_next = n2.next
        n2.next = n1
        n1.next = n2_next
        return n2

    def swap_pairs(self, head):
        """
        Complexity
        ----
        Time : O(N)
        Space : O(1)
        """
        # # swap the first two nodes
        # if head.next:
        #     new_head = self.swap_pair(head, head.next)
        # else:
        #     return head

        # # get the next pair of nodes
        # temp = new_head.next.next
        # if temp:
        #     temp_n = temp.next

        # while temp and temp_n:
        #     next_node = temp_n.next

        # return


head = Node(1, Node(2, Node(3, Node(4, None))))
n1 = head
n2 = n1.next
s = Solution()
s.swap_pair(n1, n2)

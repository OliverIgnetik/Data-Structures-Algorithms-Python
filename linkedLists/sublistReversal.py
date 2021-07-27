"""
Sublist Reversal
Given a singly linked list and a start index start and an end index end, reverse all nodes in the sublist from index start (inclusive) to index end (inclusive).

The list is conceptually one-indexed

Example 1:
Input:
start = 2
end = 4
1 -> 2 -> 3 -> 4 -> 5 -> X

Output: 1 -> 4 -> 3 -> 2 -> 5 -> X

Example 2:
Input:
start = 1
end = 1
1 -> 2 -> X

Output: 1 -> 2 -> X

Example 3:
Input:
start = 1
end = 4
1 -> 2 -> 3 -> 4 -> X

Output: 4 -> 3 -> 2 -> 1 -> X

Follow-Up:
Can you do this with O(1) space usage?

Constraints
1 <= start <= end <= (linked list size)
"""


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Solution:
    def reverseBetween(self, head, start, end):
        """
        Interface
        ----
        :type head: ListNode
        :type start: int
        :type end: int
        :rtype: ListNode

        Approach
        ----
        1. We could solve this using an array and linear space and linear time passes

        2. But we want to do it in O(1) space
        Complexity
        ----
        Time : O(N)
        Space : O(1)
        """
        if start == end:
            return head

        # build a dummy head
        dummy_head = Node(-1)
        dummy_head.next = head

        node_before_reversed_sublist = dummy_head
        pos = 1
        # traverse up to the sublist we want
        while pos < start:
            node_before_reversed_sublist = node_before_reversed_sublist.next
            pos += 1

        # after this traversal node_before_reversed_sublist will have the node we want
        # we need the first node in the sublist
        sublist_working_ptr = node_before_reversed_sublist.next

        # NOTE: we throw the node to next to the working pointer to the front of the sublist
        while start < end:
            # 1.) Cut out of the next node to throw to the head
            node_coming_to_sublist_front = sublist_working_ptr.next
            # change what is next to the working pointer
            sublist_working_ptr.next = node_coming_to_sublist_front.next

            # 2.) Wire the node into sublist head
            # point the node we are putting at the fron to the current sublist head
            node_coming_to_sublist_front.next = node_before_reversed_sublist.next
            # make sure we point the node before the sublist to the new sublist head
            node_before_reversed_sublist.next = node_coming_to_sublist_front

            start += 1

        return dummy_head.next


head = Node(1, Node(2, Node(3, Node(4, None))))
s = Solution()
s.sublistRemoval(head, 2, 3)

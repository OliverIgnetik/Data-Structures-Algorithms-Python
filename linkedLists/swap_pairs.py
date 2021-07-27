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
    def swapInPairs(self, head):
        """
        Interface
        ----
        :type head: ListNode
        :rtype: ListNode

        Complexity
        ----
        Time : O(N)
        Space : O(1)
        """
        if (head == None or head.next == None):
            return head

        first = head
        second = head.next
        start_of_next_segment = None

        # Move the head of the list to the 2nd node in the list
        head = head.next

        while True:
            # get the start of the next segment
            start_of_next_segment = second.next
            # the second node will point to the first
            second.next = first

            # edge case
            # we have one node or nothing after this pair
            if (
                start_of_next_segment == None or
                start_of_next_segment.next == None
            ):
                first.next = start_of_next_segment
                return head

            # point first at second item in the next pair
            # as it will become the first item in the next pair
            first.next = start_of_next_segment.next

            # point first at first node in the next pair
            first = start_of_next_segment
            # point second at the second node in the next pair
            second = start_of_next_segment.next


head = Node(1, Node(2, Node(3, Node(4, None))))
s = Solution()
s.swapInPairs(head)

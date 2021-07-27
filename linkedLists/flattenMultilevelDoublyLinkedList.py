"""
Flatten A Multilevel Doubly Linked List
We are given a special doubly linked list with node structure like so:

Node {
  int value;
  Node next;
  Node prev;
  Node child;
}

This special doubly linked list is the same as any other doubly linked list:
Each node carries a value or some data
It has a next pointer that points to the next item in the list's conceptual sequence
It has a prev pointer that points to the previous item in the list's conceptual sequence

The only difference is the child field. The child field points to another doubly linked list's head creating another "level" of doubly linked list in the overall structure.

You are tasked with flattening this multilevel doubly linked list structure into a single, single-level doubly linked list.

Example 1:
Input:
1 <-> 2 <-> 6 <-> 7 -> X
      ^
      |
      v
      3 <-> 4 <-> 5 -> X

Output: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 -> X

Explanation: The node with value 2 has a populated child pointer. It points to the node with value 3, forming another level of doubly linked list.

Example 2:
Input:
1 <-> 2 <-> 8 <-> 9 -> X
      ^
      |
      v
      3 <-> 4 <-> 7 -> X
            ^
            |
            v
            5 <-> 6 -> X

Output: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6 <-> 7 <-> 8 <-> 9 -> X
"""


class Node:
    def __init__(self, value, next, prev=None, child=None):
        self.value = value
        self.next = next
        self.prev = prev
        self.child = child


class Solution:
    def flattenList(self, head):
        """
        Interface
        :type: Node head reference
        :rtype: Node head reference of flattened list

        Approach
        1. Use a recursive approach and draw out an example

        2. In the recursive stackframe:
        - pass on the work to flatten everything in the child pointer
        - once the call returns the stackframe can finish the work

        3. Establish base cases and identify the state we need to pass
        """
        return self.recursive_flatten(head)

    def recursive_flatten(self, head):
        # base cases
        if head == None:
            return None

        curr = head
        while (curr != None):
            # grab a reference to the next node
            savedNext = curr.next
            # point the prev of the child to curr
            if curr.child != None:
                child = curr.child
                child.prev = curr
                # rely on the base case to flatten this list
                flattenedListhead = self.recursive_flatten(child)
                curr.next = flattenedListhead
                # remove the child pointer
                curr.child = None
                if savedNext != None:
                    tailFlattenedList = self.last(flattenedListhead)
                    # rewire the tail of the flattened list and the savedNex node
                    tailFlattenedList.next = savedNext
                    savedNext.prev = tailFlattenedList
            # move on to the next node
            curr = savedNext
        # we are done return head
        return head

    def last(self, head):
        # grab the last node
        curr = head
        while curr.next:
            curr = curr.next
        return curr

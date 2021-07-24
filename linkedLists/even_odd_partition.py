"""
Given a singly linked list, arrange the nodes such that all even index nodes appear before the odd index nodes.
When we refer to "index" we are referring to the node's zero-indexed position in the input (original) list.
The relative ordering of the nodes within the same region must be maintained.

Example 1:
Input:  5 -> 1 -> 3 -> 7 -> 3 -> X  
Output: 5 -> 3 -> 3 -> 1 -> 7 -> X 
Explanation: All the even index nodes go first, followed by the odd. The relative ordering of the nodes is maintained.

Example 2:
Input:  1 -> 2 -> 3 -> 4 -> 5 -> X
Output: 1 -> 3 -> 5 -> 2 -> 4 -> X

Example 3:
Input:  4 -> 1 -> X
Output: 4 -> 1 -> X

Constraints:
The arrangement must be performed using O(1) space
"""
# we can import the LinkedList class we built before
from linked_list import LinkedList


class Solution:
    def oddEvenList(self, l: LinkedList) -> LinkedList:
        """
        input 
        ----
        l : LinkedList object

        output 
        ----
        l : LinkedList object
        Complexity
        ----
        Time : O(N)
        Space : O(1) (pointer manipulation)
        """
        # edge case
        if l.length == 0:
            return l

        # pointers
        i = 0
        prevEven = None
        prevOdd = None
        evenHead = None
        oddHead = None
        temp = l.head

        # create odd and even partitions
        while temp:
            if i == 0:
                evenHead = temp
                prevEven = evenHead
                temp = temp.next
                i += 1
                continue
            if i == 1:
                oddHead = temp
                prevOdd = oddHead
                temp = temp.next
                i += 1
                continue

            # grab the next node
            next_ = temp.next
            # even
            if i % 2 == 0:
                prevEven.next = temp
                prevEven = temp

            # odd
            if i % 2 == 1:
                prevOdd.next = temp
                prevOdd = temp

            temp = next_
            i += 1

        # the end of the even linked list should point to the head of the odd linked list
        prevEven.next = oddHead
        prevOdd.next = None
        l.head, l.tail = evenHead, prevOdd
        return l


class AlternativeSolution:
    def oddEvenList(self, head):
        """
        This approach expects a node as input. 
        This approach uses less pointers

        Complexity
        ----
        Time : O(N)
        Space : O(1)
        """
        if not head.next:
            return head

        even = head
        odd = oddHead = head.next
        while odd != None and odd.next != None:
            even.next = odd.next
            even = odd.next
            odd.next = even.next
            odd = even.next

        even.next = oddHead
        return head


if __name__ == "__main__":
    l = LinkedList()
    l.append(10)
    l.append(5)
    l.append(6)
    l.prepend(1)
    l.printl()
    print(l.head.data, l.tail.data)
    print('-' * 10)
    print('Odd Even Partition')
    l = Solution().oddEvenList(l.head)
    l.printl()

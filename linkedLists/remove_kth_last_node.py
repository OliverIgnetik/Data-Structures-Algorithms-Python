class Node:
    def __init__(self, data: int, next) -> None:
        self.data = data
        self.next = next

    def __repr__(self):
        return f'{self.__class__.__name__}({self.data}{self.next})'


class Solution:
    def removeKthToLast(self, head: Node, k: int) -> Node:
        '''
        :type head: ListNode
        :type k: int
        :rtype: ListNode

        Input Constraints
        ----
        1 <= k <= linked list size

        Complexity 
        ----
        Time : O(k)
        Space : O(1)
        '''
        leftPointer = head
        rightPointer = head
        # we need to move the rightPointer to the node just before the
        # kth last node

        if k == 0:
            raise LookupError('1 <= k <= length')

        for i in range(k):
            rightPointer = rightPointer.next
            if i == k - 1:
                return head.next

        # iterate until the rightPointer reaches end of the linked list
        while rightPointer.next:
            leftPointer = leftPointer.next
            rightPointer = rightPointer.next

        leftPointer.next = leftPointer.next.next
        return head


if __name__ == "__main__":
    l = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
    s = Solution()
    l = s.removeKthToLast(l, 5)
    print(l)

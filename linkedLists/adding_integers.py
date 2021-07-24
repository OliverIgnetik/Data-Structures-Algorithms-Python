"""
Add 2 Integers Represented As Linked Lists
You are given two singly linked lists l1 and l2. Each represents a number in reverse (where each node is a digit).

Return a singly linked list that is the sum of the two numbers that l1 and l2 each respectively represent (this output list will also be in reverse order).

Example 1:
Input:
2 -> 2 -> 5 -> X
5 -> 9 -> 2 -> X

Output: 
7 -> 1 -> 8 -> X

Explanation: 
522 + 295 = 817 as reverse list 7 -> 1 -> 8 -> X

Example 2:
Input:
2 -> 1 -> 2 -> X
5 -> 9 -> 2 -> X

Output: 
7 -> 0 -> 5 -> X

Explanation: 
212 + 295 = 507 as reverse list 7 -> 0 -> 5 -> null 
"""


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        '''
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Complexity 
        ---- 
        Time : O(L1 + L2)
        Space : O(1)
        '''
        l1p = l1head = l1
        l2p = l2head = l2
        carry = 0
        while (l1p and l2p):
            s = l1p.value + l2p.value + carry
            digit = s % 10
            carry = s // 10
            l1p.value = digit
            l2p.value = digit
            l1p = l1p.next
            l2p = l2p.next

        if not l1p and not l2p and carry != 0:
            l1p.next = Node(carry, None)
            head = l1head
        if not l1p and not l2p and carry == 0:
            head = l1head
        if l1p:
            while l1p:
                s = l1p.value + carry
                digit = s % 10
                carry = s // 10
                l1p.value = digit
                l1p = l1p.next
            if carry != 0:
                l1p.next = Node(carry, None)
            head = l1head
        if l2p:
            while l2p:
                s = l2p.value + carry
                digit = s % 10
                carry = s // 10
                l2p.value = digit
                l2p = l2p.next
            if carry != 0:
                l2p.next = Node(carry, None)
            head = l2head

        return head


class AlternativeSolution:
    def addTwoNumbers(self, l1, l2):
        '''
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Complexity 
        ---- 
        Time : O(M + N)
        Space : O(max(M,N)) including the output
        '''
        ptr1 = l1
        ptr2 = l2

        dummy_head = Node(0, None)
        new_list_build_ptr = dummy_head

        carry = 0

        while (ptr1 != None or ptr2 != None):
            first = ptr1.val if (ptr1 != None) else 0
            second = ptr2.val if (ptr2 != None) else 0

            sum = carry + first + second
            carry = sum // 10

            new_list_build_ptr.next = Node(sum % 10, None)

            if ptr1 != None:
                ptr1 = ptr1.next

            if ptr2 != None:
                ptr2 = ptr2.next

            new_list_build_ptr = new_list_build_ptr.next

        # If a carry remains create a node for it
        if carry > 0:
            new_list_build_ptr.next = Node(carry, None)

        return dummy_head.next


s = Solution()
l1 = Node(2, Node(2, Node(5, None)))
l2 = Node(5, Node(9, Node(2, None)))
print(s.addTwoNumbers(l1, l2))

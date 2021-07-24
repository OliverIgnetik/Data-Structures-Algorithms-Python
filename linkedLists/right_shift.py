"""
Right Shift A Singly Linked List
Given the head of a singly linked list, rotate the list k steps to the right.

Example 1:
Input:
k = 2
1 -> 2 -> 3 -> 4 -> X

Output:
3 -> 4 -> 1 -> 2 -> X

Example 2:
Input:
k = 4
4 -> 1 -> 6 -> 7 -> X

Output:
4 -> 1 -> 6 -> 7 -> X

Constraints
k >= 0
"""


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


from collections import deque
# https://wiki.python.org/moin/TimeComplexity
# rotate = O(k)


class NaiveSolution:
    def rotateRight(self, head, k):
        """
        Make use of collections.deque and the efficient O(k) rotate operation 
        Time : O(max(k, N)) deque rotate has time complexity of O(k)
        Space : O(N)
        """
        items = deque([head.value])
        temp = head.next
        while temp:
            items.append(temp.value)
            temp = temp.next
        for _ in range(k):
            items.rotate()

        head = None
        temp = head
        for j in range(len(items)):
            new_node = Node(items[j], None)
            if head == None:
                head = new_node
                temp = head
            else:
                temp.next = new_node
                temp = temp.next

        return head


class OptimizedSolution:
    def rotateRight(self, head, k):
        """
        Approach 
        ----
        Example k = 2
        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None

        Head becomes 5  
        1 -> 2 -> 3 -> 4    5 -> 6 

        5 -> 6 -> 1 -> 2 -> 3 -> 4 -> None
        Time : O(N)
        Space : O(1)
        """
        # edge case
        if k == 0:
            return head

        size_list = 0
        temp = head
        # get the size of the list O(N)
        while temp:
            size_list += 1
            temp = temp.next

        # O(k) find the new head
        count = 0
        temp = head
        while count != size_list - k % size_list - 1:
            count += 1
            temp = temp.next

        # change to tail
        head_new_list = temp.next
        temp.next = None

        # reform the lists
        temp = head_new_list
        while temp.next != None:
            temp = temp.next

        temp.next = head

        return head_new_list


s1 = NaiveSolution()
s2 = OptimizedSolution()
l = Node(1, Node(2, Node(3, Node(4, None))))
print(s2.rotateRight(l, 2))

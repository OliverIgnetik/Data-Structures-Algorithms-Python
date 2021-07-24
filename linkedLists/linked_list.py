# 15 --> 6 --> 8

"""
TIME COMPLEXITY
----
insertAtIndex : O(1)
removeAtIndex : O(1)
search : O(N)
access : O(N) (to access the element at index j we have to traverse the linked list)

SPACE COMPLEXITY : O(N)
"""


class Node():

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, data):
        new_node = Node(data)
        temp = self.head
        if index >= self.length:
            raise IndexError('Index out of range')
        if index == 0:
            self.prepend(data)
            return
        i = 0
        while i < self.length:
            if i == index - 1:
                temp.next, new_node.next = new_node, temp.next
                self.length += 1
                return
            temp = temp.next
            i += 1

    def remove(self, index):
        temp = self.head
        i = 0
        if index >= self.length:
            raise IndexError('Index out of range')

        # remove the head
        if index == 0:
            if self.length == 1:
                self.head = None
                self.tail = head
                self.length -= 1
                return
            else:
                self.head = self.head.next
                self.length -= 1
                return

        while i < self.length:
            # removing the tail
            if i == index - 1 and index == self.length - 1:
                temp.next = None
                self.tail = temp
                self.length -= 1
                return

            # otherwise
            elif i == index - 1:
                temp.next = temp.next.next
                self.length -= 1
                return
            i += 1
            temp = temp.next

    def printl(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
        print('Length = ' + str(self.length))

    def reverse(self):
        prev = None
        temp = self.head
        while temp:
            next_ = temp.next
            temp.next = prev
            prev, temp = temp, next_

        self.head, self.tail = self.tail, self.head


if __name__ == '__main__':
    l = LinkedList()
    l.append(10)
    l.append(5)
    l.append(6)
    l.prepend(1)
    l.insert(2, 99)
    l.insert(4, 23)
    l.remove(5)
    l.reverse()
    l.printl()
    print(l.head.data, l.tail.data)

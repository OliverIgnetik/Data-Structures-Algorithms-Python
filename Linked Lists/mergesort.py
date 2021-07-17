from random import randint


class Node:
    def __init__(self, val, n=None):
        self.val = val
        self.next = n

    def __repr__(self):
        return f'{self.__class__.__name__}({self.val}, {self.next})'


def mergesort(l):
    """
    input
    ----
    l : linked list of integers 
    output
    ----
    sorted_l : sorted linked list

    Complexity
    Time : O(NlogN)
    Space : O(logN)
    """
    def split(l):
        count, current = 0, l
        # count length of linked list
        while current:
            current = current.next
            count += 1

        # get the middle index
        mid = count // 2
        count = 0
        current = l

        # retrieve the middle node
        while count != mid - 1:
            current = current.next
            count += 1

        right = current.next
        current.next = None
        left = l

        return (left, right)

    def merge(left, right):
        def get_min_node(left, right):
            min_node = None
            if left.val < right.val:
                min_node = left
                left = left.next
            else:
                min_node = right
                right = right.next

            return (min_node, left, right)

        original_head = None
        original_head, left, right = get_min_node(left, right)
        temp = original_head
        while left and right:
            temp, left, right = get_min_node(left, right)

        if left:
            temp.next = left
        if right:
            temp.next = right

        return original_head

    if (l == None or l.next == None):
        return l

    left, right = split(l)

    left_sorted = mergesort(left)
    right_sorted = mergesort(right)

    return merge(left_sorted, right_sorted)


def display_as_array(l):
    curr = l
    values = []
    while curr:
        values.append(curr.val)
        curr = curr.next
    return values


l = Node(randint(0, 10), None)
temp = l

for _ in range(4):
    new_node = Node(randint(0, 10), None)
    temp.next = new_node
    temp = temp.next

print(f'Unsorted Values : {display_as_array(l)}')
# perform mergesort
sorted_l = mergesort(l)

print(f'Sorted Values : {display_as_array(sorted_l)}')

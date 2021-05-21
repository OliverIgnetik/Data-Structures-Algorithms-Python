from nose.tools import assert_equal


class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode = None

##################################### PROBLEM ########################################
# Given a linked list, write a function which finds the nth to last node


def nth_to_last_node(n, head):

    left_pointer = head
    right_pointer = head

    # Set right pointer at n nodes away from head
    for i in range(n-1):
        # Check for edge case of not having enough nodes!
        if not right_pointer.nextnode:
            raise LookupError('Error: n is larger than the linked list.')
        # Otherwise, we can set the block
        right_pointer = right_pointer.nextnode

    # Move the block down the linked list
    # you need to stop when you reach the last node
    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    # Now return left pointer, its at the nth to last element!
    return left_pointer

##### BASIC TEST #######


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# find the 3rd last node in the singly linked list
nth_to_last_node(3, a).value

#################### TESTING #################################################

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

####


class TestNLast(object):

    def test(self, sol):

        assert_equal(sol(3, a), c)
        print('ALL TEST CASES PASSED')


# Run tests
t = TestNLast()
t.test(nth_to_last_node)

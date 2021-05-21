from nose.tools import assert_equal
##################################### PROBLEM ########################################
# Given a singly linked list, write a function which takes in the first node in a singly
# linked list and returns a boolean indicating if the linked list contains a "cycle".
# A cycle is when a node's next point actually points back to a previous node in the list.
# This is also sometimes known as a circularly linked list.


class Node(object):

    def __init__(self, value):

        self.value = value
        self.nextnode = None


def cycle_check(node):

    # Begin both markers at the first node
    # quick assign two variables to same memory object
    marker1 = marker2 = node

    # Go until end of list
    while marker2 != None and marker2.nextnode != None:

        # Note
        marker1 = marker1.nextnode
        # this is why you have the check to see if marker2.nextnode != None
        # if you omit this check you will get an error for trying to access an attribute of None
        marker2 = marker2.nextnode.nextnode

        # Check if the markers have matched
        if marker2 == marker1:
            return True

    # Case where the faster marker reaches the end of the list
    return False


##################################### TESTING ########################################
# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a  # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


class TestCycleCheck(object):

    def test(self, sol):
        assert_equal(sol(a), True)
        assert_equal(sol(x), False)

        print("ALL TEST CASES PASSED")


# Run Tests

t = TestCycleCheck()
t.test(cycle_check)

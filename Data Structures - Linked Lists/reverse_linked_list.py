class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None

    def __repr__(self):
        return f'Node \n value : {self.value}'

############################### PROBLEM ###############################
# Reverse a singly linked list


def reverse(head):
    # Set up current,previous, and next nodes
    current = head
    previous = None
    nextnode = None

    # until we have gone through to the end of the list
    while current:
        # Make sure to copy the current nodes next node to a variable next_node
        # Before overwriting as the previous node for reversal
        nextnode = current.nextnode

        # Reverse the pointer to the next_node
        current.nextnode = previous

        # Go one forward in the list
        previous, current = current, nextnode

    return previous


# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

# will return the new head of the list -> Node d
reverse(a)

print(d.value)
print(d.nextnode.value)
print(c.nextnode.value)
print(b.nextnode.value)

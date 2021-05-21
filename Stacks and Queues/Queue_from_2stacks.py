class Queue2Stacks(object):

    def __init__(self):

        # Two Stacks
        self.instack = []
        self.outstack = []

    def enqueue(self, element):

        # Add an enqueue with the "IN" stack
        self.instack.append(element)

    def dequeue(self):
        # check to see if empty
        # you wouldn't want to accidentally put something in the front of the queue ie. top of the outstack
        if not self.outstack:
            # pattern for emptying the instack
            while self.instack:
                # Add the elements to the outstack to reverse the order when called
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()


q = Queue2Stacks()

for i in range(5):
    q.enqueue(i)

for i in range(5):
    print(q.dequeue())

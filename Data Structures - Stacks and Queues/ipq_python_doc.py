# An indexed priority queue is a traditional priority queue
# variant which on top of the regular priority queue operations
# supports quick updates and deletions of key-value pairs

# https://docs.python.org/3/library/heapq.html#module-heapq

import itertools
from heapq import heappush, heappop


class IPQ:
    REMOVED = '<removed-task>'      # placeholder for a removed task

    def __init__(self):
        self.pq = []                         # list of entries arranged in a heap
        self.entry_finder = {}               # mapping of tasks to entries
        self.counter = itertools.count()     # unique sequence count

    def add_task(self, task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.__class__.REMOVED

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not self.__class__.REMOVED:
                del self.entry_finder[task]
                return (task, priority)
        raise KeyError('pop from an empty priority queue')


###################################### TEST #######################################
ipq = IPQ()
ipq.add_task(0, 5)
ipq.add_task(1, 2)
print(ipq.pop_task())
ipq.add_task(1, 1)

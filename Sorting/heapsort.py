# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap

# COMPLEXITY ANALYSIS
# O(NlogN) time complexity

from heapq import heappush, heappop

#################### PYTHON DOCS IMPLEMENTATION ##################################
# https://docs.python.org/2/library/heapq.html#priority-queue-implementation-notes
# this works more succintly because we make use of a minheap not a maxheap


def heapsort_alt(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for _ in range(len(h))]


arr = [12, 11, 13, 5, 6, 7]
print(heapsort_alt(arr))

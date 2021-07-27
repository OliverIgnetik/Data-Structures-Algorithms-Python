import heapq
from queue import PriorityQueue


class AlternativeSolution:
    def kSmallestElements(self, arr, k):
        """
        Interface
        ----
        :type elements: list of int
        :type k: int
        :rtype: list of int

        Approach
        ----
        1. If we keep a min heap and eject items when the size is > k we are left with the k largest items

        2. The item left at the top of the heap is the kth largest item

        3. If we negate all the items the item left at the top of the heap will be the kth smallest item

        Complexity
        ----
        Time : O(Nlogk)
        Space : O(k)
        """
        res = [None] * k

        q = PriorityQueue()
        for num in arr:
            q.put(-num)
            if q.qsize() > k:
                q.get()

        for i in range(len(res) - 1, -1, -1):
            res[i] = -q.get()
        return res


class Solution:
    def kSmallestElements(self, elements, k):
        """
        Interface
        ----
        :type elements: list of int
        :type k: int
        :rtype: list of int

        Complexity
        ----
        Time : O(Nlogk)
        Space : O(k)
        """
        max_heap = MaxHeap()

        for element in elements:
            max_heap.add(element)

            if (max_heap.size() == k + 1):
                max_heap.poll()

        return max_heap.to_list()


class MaxHeap:
    def __init__(self):
        self.data = []

    def peek(self):
        return -self.data[0]

    def add(self, val):
        heapq.heappush(self.data, -val)

    def poll(self):
        return -heapq.heappop(self.data)

    def to_list(self):
        return list(map(lambda item: -item, self.data))

    def size(self):
        return len(self.data)


arr = [8, 1, 3, 2, 6, 7]
k = 2
print(AlternativeSolution().kSmallestElements(arr, k))

# Comparable to a complete binary tree
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # ensure minHeap property is upheld
    def percUp(self, i):
        # move up until you are at the top of the tree
        while i // 2 > 0:
            # move up
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):

        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):

        while (i * 2) <= self.currentSize:
            # Which child is the minimum?
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        # if there are only 2,4,6... elements
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        # O(N) time complexity bonus
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1


# MINHEAP
# bh.buildHeap([1, 3, 4, 10, 8, 7, 12])
bh = BinHeap()
bh.insert(10)
bh.insert(4)
bh.insert(3)
bh.delMin()
bh.insert(2)
bh.insert(1)
bh.delMin()
bh.insert(-2)
bh.insert(0)
bh.insert(7)
bh.delMin()
print(bh.heapList)

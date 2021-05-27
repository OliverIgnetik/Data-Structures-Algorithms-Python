# CREDIT
# https: // github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/graphtheory/DijkstrasShortestPathAdjacencyListWithDHeap.java
class minIndexedDHeap:

    def __init__(self, degree: int, maxSize: int):
        self.D = max(2, degree)
        self.N = max(self.D + 1, maxSize)
        self.size = 0

        ################# UNDERSTANDING different mappings is crucial in IPQs ###########################
        # im - inverse mapping array, index = heap position, value = key index
        # pm - position mapping array, index = key index, value = heap position
        # values - values array, index = key index, value = value

        # given the position in the heap of the node what is the associated key index and value?
        self.im = [0] * self.N
        # given the key index what is the heap index of that node in the heap?
        self.pm = [0] * self.N
        # child and parent references are needed for a d-ary heap
        self.child = [0] * self.N
        self.parent = [0] * self.N
        # given the certain key what is the value of that associated node?
        self.values = [0] * self.N

        for i in range(self.N):
            self.parent[i] = (i - 1) // self.D
            self.child[i] = i * self.D + 1
            self.pm[i] = self.im[i] = -1

    def __contains__(self, ki: int):
        return self.pm[ki] != -1

    def peekMinKeyIndex(self):
        return self.im[0]

    def pollMinKeyIndex(self):
        minki = self.peekMinKeyIndex()
        self.delete(minki)
        return minki

    def peekMinValue(self):
        return self.values[self.im[0]]

    def pollMinValue(self):
        minValue = self.peekMinValue()
        self.delete(self.peekMinKeyIndex())
        return minValue

    def insert(self, ki: int, value):
        if ki in self:
            raise KeyError('Index already exists')
        self.pm[ki] = self.size
        self.im[self.size] = ki
        self.values[ki] = value
        self.size += 1
        self.__swim(self.size)

    def delete(self, ki: int):
        i = self.pm[ki]
        self.size -= 1
        self.__swap(i, self.size)
        self.__sink(i)
        self.__swim(i)
        value = self.values[ki]
        self.values[ki] = None
        self.pm[ki] = -1
        self.im[self.size] = -1
        return value

    def update(self, ki: int, value):
        i = self.pm[ki]
        oldValue = self.values[ki]
        self.values[ki] = value
        self.__sink(i)
        self.__swim(i)
        return oldValue

    def decrease(self, ki: int, value):
        if (self.__less(value, self.values[ki])):
            self.values[ki] = value
            self.__swim(self.pm[ki])

    def increase(self, ki: int, value):
        if (self.__less(self.values[ki], value)):
            self.values[ki] = value
            self.__sink(self.pm[ki])

    # helper methods
    def __swim(self, i: int):
        while (self.__less(i, self.parent[i])):
            self.__swap(i, self.parent[i])
            i = parent[i]

    def __sink(self, i: int):
        j = self.__minchild(i)
        while j != -1:
            self.__swap(i, j)
            i = j
            j = self.__minchild(i)

    def __minchild(self, i: int):
        index = -1
        from_ = self.child[i]
        to = min(self.size, from_ + self.D)

        j = from_
        while j < to:
            if (self.__less(j, i)):
                index = i = j
            j += 1
        return index

    def __swap(self, i: int, j: int):
        self.pm[self.im[j]] = i
        self.pm[self.im[i]] = j
        tmp = self.im[i]
        self.im[i] = self.im[j]
        self.im[j] = tmp

    @staticmethod
    def __less(x, y):
        return x < y

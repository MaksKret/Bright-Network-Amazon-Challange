import math


## Minimum Heap that works with arrays of tuples (key, node)


class minHeap:

    def __init__(self, array):
        self.heap = array
        self.heapsize = len(array)
        self.buildMinHeap()

    def parent(self, i):
        if i == 0:
            return 0
        else:
            return math.ceil(i/2) - 1

    def left(self, i):
        return i*2 + 1

    def right(self, i):
        return i*2 + 2
    
    def heapMin(self):
        if self.heapsize == 0:
            return None
        else:
            return self.heap[0]

    def buildMinHeap(self):
        for i in range(math.floor(self.heapsize/2) - 1, -1, -1):
            self.minHeapify(i)
    
    def extractMin(self):
        self.heapsize = self.heapsize - 1
        min = self.heap.pop(0)
        self.buildMinHeap()
        return min

    def insertItem(self, tuple):
        self.heapsize = self.heapsize + 1
        self.heap.append(tuple)
        self.buildMinHeap()
    
    def reduceKey(self, key, node):
        for i in range(self.heapsize):
            if self.heap[i][1] == node:
                self.heap[i][0] = key
        self.buildMinHeap()


    def minHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < self.heapsize and self.heap[l][0] < self.heap[i][0]:
            smallest = l
        if r < self.heapsize and self.heap[r][0] < self.heap[smallest][0]:
            smallest = r
        if smallest != i:
            temp = self.heap[i]
            self.heap[i] = self.heap[smallest]
            self.heap[smallest] = temp
            self.minHeapify(smallest)


## ######################## ##
## Getter and string method ##
## ######################## ##

    def getHeap(self):
        return self.heap

    def __str__(self):
        return str(self.heap)
    
    def isEmpty(self):
        return self.heapsize == 0




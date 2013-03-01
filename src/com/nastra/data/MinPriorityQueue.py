'''
Implements a min priority queue based on a binary min heap

@author: nastra - Eduard Tudenhoefner
'''
from com.nastra.data.MinHeap import MinHeap

class MinPriorityQueue(object):

    def __init__(self):
        self.heap = MinHeap()
        
    def insert(self, key):
        self.heap.insert(key)
        
    def decreaseKey(self, index, key):
        if key > self.heap.heap[index]:
            raise ValueError("New key must be smaller than the old key!")
        self.heap.heap[index] = key
        self.heap.siftUp(index)
    
    def extractMin(self):
        return self.heap.extractMin()
    
    def getMin(self):
        return self.heap.getMin()
    
    def printQueueContent(self):
        print(self.heap.heap)


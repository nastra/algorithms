'''
Implements a min priority queue based on a binary min heap

@author: nastra - Eduard Tudenhoefner
'''
from com.nastra.data.minheap import MinHeap

class MinPriorityQueue(object):

    def __init__(self):
        self.heap = MinHeap()
        
    def insert(self, key):
        '''
        Inserts a new element to the queue. Runs in time O(log n).
        '''
        self.heap.insert(key)
        
    def decreaseKey(self, index, key):
        '''
        Decreases the priority of an element. Runs in time O(log n).
        '''
        if key > self.heap.heap[index]:
            raise ValueError("New key must be smaller than the old key!")
        self.heap.heap[index] = key
        self.heap.siftUp(index)
    
    def extractMin(self):
        '''
        Retrieves and removes the min element from the queue. Runs in time O(log n)
        '''
        return self.heap.extractMin()
    
    def getMin(self):
        '''
        Retrieves the minimum element from the queue. Runs in time O(1).
        '''
        return self.heap.getMin()
    
    def printQueueContent(self):
        print(self.heap.heap)
        
    def empty(self):
        return len(self.heap.heap) == 0
    
    def contains(self, key):
        return key in self.heap.heap


'''
Implements a Binary Min Heap

@author: nastra - Eduard Tudenhoefner
'''
import math

class MinHeap(object):

    def __init__(self, heapArray=[]):
        self.heap = heapArray
        if len(heapArray) > 0:
            self.buildMinHeap()
        
    def getParent(self, index):
        if index == 0:
            return 0
        return math.ceil(index / 2) - 1
    
    def getLeft(self, index):
        return 2 * index + 1
    
    def getRight(self, index):
        return 2 * index + 2
    
    def heapify(self, index):
        '''
        This function is mainly responsible for maintaining the heap property. Runs in time O(log n).
        '''
        leftIndex = self.getLeft(index)
        rightIndex = self.getRight(index)
        smallest = index
        heapSize = len(self.heap)
        
        if leftIndex < heapSize and self.heap[leftIndex] < self.heap[index]:
            smallest = leftIndex
        if rightIndex < heapSize and self.heap[rightIndex] < self.heap[smallest]:
            smallest = rightIndex
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify(smallest)
        
    def insert(self, element):
        '''
        Insert a new elements into the heap. Running time is O(log n).
        '''
        self.heap.append(element)
        index = len(self.heap) - 1
        self.siftUp(index)
            
    def siftUp(self, index):
        while index != 0 and self.heap[self.getParent(index)] > self.heap[index]:
            self.heap[index], self.heap[self.getParent(index)] = self.heap[self.getParent(index)], self.heap[index]
            index = self.getParent(index)

    def extractMin(self):
        '''
        Retrieves and removes the minimum element from the heap. Runs in time O(log n).
        '''
        heapSize = len(self.heap) - 1
        minElement = self.heap[0]
        self.heap[0] = self.heap[heapSize]
        self.heap.pop(heapSize)
        self.heapify(0)  # now re-establish the heap property
        return minElement
    
    def getMin(self):
        '''
        Retrieves the minimum element from the heap. Runs in time O(1).
        '''
        return self.heap[0]
    
    def buildMinHeap(self):
        '''
        Builds up the min heap. Running time is O(n).
        '''
        for i in range(int(len(self.heap) / 2), -1, -1):
            self.heapify(i)
            
    def heapsort(self):
        """ The heap-sort algorithm with a time complexity O(n log n) """
        self.buildMinHeap()
        output = []
        for i in range(len(self.heap) - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            output.append(self.heap.pop())
            self.heapify(0)
        output.append(self.heap.pop())
        self.heap = output
        return output

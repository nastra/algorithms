'''
This is an implementation of a Binary Max Heap including the heapsort algorithm.

@author: nastra - Eduard Tudenhoefner
'''
import math
class MaxHeap(object):
    def __init__(self, heapArray=[]):
        self.heap = heapArray
        if len(heapArray) > 0:
            self.buildMaxHeap()
     
    def parent(self, index):
        if index == 0:
            return 0
        return math.ceil(index / 2) - 1
     
    def leftChild(self, index):
        return 2 * index + 1
     
    def rightChild(self, index):
        return 2 * index + 2
    
    def heapify(self, index):
        """
        Responsible for maintaining the heap property of the heap. Running time is O(log n)
        """
        leftIndex = self.leftChild(index)
        rightIndex = self.rightChild(index)
         
        largest = index
        if leftIndex < len(self.heap) and self.heap[leftIndex] > self.heap[index]:
            largest = leftIndex
        if rightIndex < len(self.heap) and self.heap[rightIndex] > self.heap[largest]:
            largest = rightIndex
         
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify(largest)

    def buildMaxHeap(self):
        """
        Responsible for building the heap bottom up. It starts with the lowest non-leaf nodes
        and calls heapify on them. This function is useful for initialising a heap with an
        unordered array. Running time is O(n)
        """
        for i in range(int(len(self.heap) / 2), -1, -1):
            self.heapify(i)
            
    def extractMax(self):
        '''
        Retrieves and removes the maximum element from the heap. Runs in time O(log n)
        '''
        maxElement = self.heap[0]
        heapSize = len(self.heap) - 1
        self.heap[0] = self.heap[heapSize]
        self.heap.pop(heapSize)
        self.heapify(0)  # now re-establish the heap property
        return maxElement
    
    def getMax(self):
        '''
        Retrieves the maximum element from the heap. Runs in time O(1).
        '''
        return self.heap[0]
    
    def insert(self, element):
        '''
        Insert a new elements into the heap. Running time is O(log n).
        '''
        self.heap.append(element)
        index = len(self.heap) - 1
        self.siftUp(index)
    
    def siftUp(self, index):
        while index != 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)
            
    def size(self):
        return len(self.heap)
            
    def heapsort(self):
        """ The heap-sort algorithm with a time complexity O(n log n) """
        self.buildMaxHeap()
        output = []
        for i in range(len(self.heap) - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            output.append(self.heap.pop())
            self.heapify(0)
        output.append(self.heap.pop())
        self.heap = output
        return output
    

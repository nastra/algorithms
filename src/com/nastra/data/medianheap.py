'''
Implements a median heap by using two binary heaps. It allows to insert an element in time O(log n) and 
to retrieve the median in time O(1) by using two binary heaps.

@author: nastra - Eduard Tudenhoefner
'''
from com.nastra.data.minheap import MinHeap
from com.nastra.data.maxheap import MaxHeap

class MedianHeap(object):

    def __init__(self):
        self.left = MaxHeap()
        self.right = MinHeap()
        
    def getMedian(self):
        '''
        Retrieves and returns the median element. Runs in time O(1).
        If we have even elements, then the median of the left part is returned. 
        If either side has one more element, then we return the median from this side.
        '''
        leftSize = self.left.size()
        rightSize = self.right.size()
        if self.__evenSize() or (leftSize > rightSize):
            return self.left.getMax()
        
        return self.right.getMin()
        
        
    def insert(self, element):
        if self.left.size() == 0:
            self.left.insert(element)
        if element <= self.left.getMax():
            self.left.insert(element)
        else:
            self.right.insert(element)
            
        self.balance()  # need to balance both sides in case they get imbalanced
        
    def balance(self):
        '''
        We re-balance in case one side gets off by 2 elements. Runs in time O(log n).
        '''
        leftSize = len(self.left.heap)
        rightSize = len(self.right.heap)
        if leftSize == rightSize + 2:
            self.right.insert(self.left.extractMax())
        elif rightSize == leftSize + 2:
            self.left.insert(self.right.extractMin())
            
    def __evenSize(self):
        ''' 
        Returns True if we have an even length.
        '''
        return (self.left.size() + self.right.size()) % 2 == 0
    

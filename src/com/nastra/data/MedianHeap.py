'''
Implements a median heap by using two binary heaps.

@author: nastra - Eduard Tudenhoefner
'''
from com.nastra.data.MinHeap import MinHeap
from com.nastra.data.MaxHeap import MaxHeap

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
        leftSize = len(self.left)
        rightSize = len(self.right)
        if self.__evenSize(leftSize, rightSize) or (leftSize > rightSize):
            return self.left.getMax()
        
        return self.right.getMin()
        
        
    def insert(self, element):
        if element <= self.left.getMax():
            self.left.insert(element)
        else:
            self.right.insert(element)
            
        self.balance()  # need to balance both sides in case they get imbalanced
        
    def balance(self):
        '''
        We re-balance in case one side gets off by 2 elements. Runs in time O(log n).
        '''
        leftSize = len(self.left)
        rightSize = len(self.right)
        if leftSize == rightSize + 2:
            self.right.insert(self.left.extractMax())
        elif rightSize == leftSize + 2:
            self.left.insert(self.right.extractMin())
            
    def __evenSize(self, leftSize, rightSize):
        ''' 
        Returns True if we have an even length.
        '''
        return (leftSize + rightSize) % 2 == 0
                
            
        

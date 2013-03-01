'''
This is an implementation of a max heap sorting algorithm.

@author: nastra - Eduard Tudenhoefner
'''
class MaxHeap:
    def __init__(self, heap):
        self.heap = heap
     
    def parent(self, index):
        return index / 2
     
    def left_child(self, index):
        return 2 * index + 1
     
    def right_child(self, index):
        return 2 * index + 2
    
    def max_heapify(self, index):
        """
        Responsible for maintaining the heap property of the heap. Running time is O(log n)
        """
        left_index = self.left_child(index)
        right_index = self.right_child(index)
         
        largest = index
        if left_index < len(self.heap) and self.heap[left_index] > self.heap[index]:
            largest = left_index
        if right_index < len(self.heap) and self.heap[right_index] > self.heap[largest]:
            largest = right_index
         
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.max_heapify(largest)

    def build_max_heap(self):
        """
        Responsible for building the heap bottom up. It starts with the lowest non-leaf nodes
        and calls heapify on them. This function is useful for initialising a heap with an
        unordered array. Running time is O(n)
        """
        for i in range(int(len(self.heap) / 2), -1, -1):
            self.max_heapify(i)
            
    def extract_max(self):
        maxElement = self.heap.pop(0)
        self.max_heapify(0)
        return maxElement
            
    def heapsort(self):
        """ The heap-sort algorithm with a time complexity O(n log n) """
        self.build_max_heap()
        output = []
        for i in range(len(self.heap) - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            output.append(self.heap.pop())
            self.max_heapify(0)
        output.append(self.heap.pop())
        self.heap = output
        return output

if __name__ == '__main__':
    input = [1, 4, 7, 44, 67, 234, 9, 66, 123, 88, 54, 34]
    heap = MaxHeap(input)
    output = heap.heapsort()
    print(output)

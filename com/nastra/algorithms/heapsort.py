'''
This is an implementation of a max heap sorting algorithm.

@author: nastra
'''

import math
heapSize = 0

def get_parent(i):
    if i == 0:
        return 0
    return math.ceil(i / 2) - 1

def get_left(i):
    return 2 * i + 1

def get_right(i):
    return 2 * i + 2

def build_max_heap(array):
    global heapSize
    heapSize = len(array)
    
    for i in range(int(heapSize / 2), 0, -1):
        max_heapify(array, i)
    

def max_heapify(array, i):
    left = get_left(i)
    right = get_right(i)
    largest = i

    if left < heapSize and array[left] > array[i]:
        largest = left
        
    if right < heapSize and array[right] > array[largest]:
        largest = right
    
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, largest)

def heapsort(array):
    build_max_heap(array)
    counter = len(array) - 1
    while counter > 0:
        array[counter], array[0] = array[0], array[counter]
        max_heapify(array, 0)
        counter = counter - 1
    


if __name__ == '__main__':
    # array = [4, 2, 9, 31, 66, 46, 99, 105, 32, 14, 50]
    ''' we give an array as input that represents a heap data structure. 
    In general, a heap data structure is an almost complete binary tree (tree that is completely filled on all levels, except maybe at the lowest level).'''
    array = [2, 7, 9, 4, 15, 3]
    heapsort(array)
    print(array)

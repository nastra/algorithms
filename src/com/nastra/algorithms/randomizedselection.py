'''
Implements the randomized selection algorithm that can be applied to the following question:

"Find the k-th smallest element in an unsorted array in time O(n)."

The expected running time of this algorithm is O(n), assuming that the elements are distinct. This algorithm
can be further modified to have not only an expected running time of O(n), but also a worst-case running time
that is O(n).

@author: nastra - Eduard Tudenhoefner
'''
import random

def randomizedSelection(array, k):
    if len(array) == 1:
        return array[0]
    pivotIndex = randomizedPartition(array)
    if (pivotIndex + 1) == k:
        return array[pivotIndex]
    elif k < (pivotIndex + 1):
        return randomizedSelection(array[0:pivotIndex], k)
    else:
        return randomizedSelection(array[pivotIndex + 1:len(array)] , k - (pivotIndex + 1))
    
def randomizedPartition(array):
    high = len(array) - 1
    index = random.randint(0, high)
    array[index], array[0] = array[0], array[index]  # swap the two elements
    return partition(array)

def partition(array):
    pivot = array[0]
    i = 1
    for j in range(1, len(array)):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i - 1], array[0] = array[0], array[i - 1]
    return i - 1  # the index where the pivot element resides


if __name__ == '__main__':
    array = [random.randint(0, 100) for i in range(0, 10)]
    print("Input array is: ")
    print(array)
    print("-" * 70)
    for i in range(1, len(array) + 1):
        selection = randomizedSelection(array, i)    
        print("The " + str(i) + "th element is: " + str(selection))

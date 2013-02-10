'''
Implements the randomized selection algorithm that can be applied to the following question:

"Find the k-th smallest element in an unsorted array in time O(n)."

The expected running time of this algorithm is O(n), assuming that the elements are distinct. This algorithm
can be further modified to have not only an expected running time of O(n), but also a worst-case running time
that is O(n).

@author: nastra - Eduard Tudenhoefner
'''
import random

def randomizedSelection(array, low, high, element):
    if low == high:  # base case
        return array[low]
    else:
        pivot = randomizedPartition(array, low, high)
        if pivot == element:
            return array[pivot]
        elif element < pivot:
            return randomizedSelection(array, low, pivot - 1, element)
        else:
            return randomizedSelection(array, pivot + 1, high, element - pivot)

def randomizedPartition(array, low, high):
    index = random.randint(low, high)
    array[index], array[low], array[low], array[index]  # swap the two elements
    return partition(array, low, high)
    
def partition(array, low, high):
    x = array[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if array[j] <= x:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[i - 1], array[low], array[low], array[i - 1]
    return i - 1  # the index where the pivot element resides

if __name__ == '__main__':
    # array = [random.randint(0, 25) for i in range(0, 15)]
    array = [9, 4, 7, 123, 55, 56, 43, 90, 34, 23]
    print("Input array is: ")
    print(array)
    print("-" * 70)
    element = 8
    print("Searching for the " + str(element) + "th element in the input array")
    print("Sorted output is...")
    print(sorted(array))
    selection = randomizedSelection(array, 0, len(array) - 1, element - 1)  # because array is zero-based
    print("The " + str(element) + "th element is: " + str(selection))
    pass

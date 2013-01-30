'''
Created on Jan 20, 2013

@author: nastra
'''
import random


def randomized_partition(array, p, r):
    i = random.randint(p, r)
    array[i], array[r] = array[r], array[i]
    return partition(array, p, r)

def randomized_quicksort(array, p, r):
    if p < r:
        q = randomized_partition(array, p, r)
        randomized_quicksort(array, p, q - 1)
        randomized_quicksort(array, q + 1, r)
        
    
def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)


def partition(array, p, r):
    ''' Partitions an array around a pivot element'''
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1

if __name__ == '__main__':
    array = [4, 2, 9, 31, 66, 46, 99, 105, 32, 14, 50]
    array2 = array[:]
    print("Before quicksort: ")
    print(array)
    print("-" * 50)
    print("Running quicksort...")
    quicksort(array, 0, len(array) - 1)
    print("After quicksort: ")
    print(array)
    print("-" * 50)
    print("Running randomized quicksort...")
    randomized_quicksort(array2, 0, len(array2) - 1)
    print("After randomized quicksort: ")
    print(array2)

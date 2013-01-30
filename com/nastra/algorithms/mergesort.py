'''
Created on Jan 30, 2013

@author: nastra - Eduard Tudenhoefner
'''

def mergesort(numbers):
    ''' Sorts an input list by using the divide-and-conquer approach '''
    # if there is just one element, no work has to be done
    if len(numbers) <= 1:
        return numbers
    
    mid = len(numbers) // 2
    left = mergesort(numbers[0:mid])  # sort the left list
    right = mergesort(numbers[mid:len(numbers)])  # sort the right list
    return merge(left, right)  # merge both lists and return a sorted version of them
    
def merge(left, right):
    ''' Merges the left and right list and returns a sorted list '''
    i = 0
    j = 0
    out = []
    # copy the smallest value from either the left or the right side to the output
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    # copy the rest of the left list to the output
    while i < len(left):
        out.append(left[i])
        i += 1
    # copy the rest of the right list to the output
    while j < len(right):
        out.append(right[j])
        j += 1
        
    return out
    


if __name__ == '__main__':
    import random
    numbers = [random.randint(0, 100) for i in range(0, 20)]
    print("Before sort: " + str(numbers))
    sortedNumbers = mergesort(numbers)
    print("After sort:  " + str(sortedNumbers))
    pass

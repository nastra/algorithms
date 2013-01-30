'''
Counts the number of inversions in a given list by using the Mergesort algorithm

@author: nastra - Eduard Tudenhoefner
'''

def countInversionsAndSort(numbers):
    ''' Sorts an input list by using the divide-and-conquer approach '''
    # if there is just one element, no work has to be done
    if len(numbers) <= 1:
        return numbers, 0
    
    mid = len(numbers) // 2
    left, leftInv = countInversionsAndSort(numbers[0:mid])  # sort the left list
    right, rightInv = countInversionsAndSort(numbers[mid:len(numbers)])  # sort the right list
    merged, totalInv = merge(left, right)  # merge both lists and return a sorted version of them
    return merged, (totalInv + leftInv + rightInv)
    
def merge(left, right):
    ''' Merges the left and right list and returns a sorted list '''
    i = 0
    j = 0
    out = []
    inversions = 0
    # copy the smallest value from either the left or the right side to the output
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
            inversions += (len(left) - i)
    # copy the rest of the left list to the output
    while i < len(left):
        out.append(left[i])
        i += 1
    # copy the rest of the right list to the output
    while j < len(right):
        out.append(right[j])
        j += 1
        
    return out, inversions
    


if __name__ == '__main__':
    import random
    numbers = [random.randint(0, 100) for i in range(0, 6)]
    print("Before sort: " + str(numbers))
    sortedNumbers, inversions = countInversionsAndSort(numbers)
    print("After sort:  " + str(sortedNumbers))
    print("# of found inversions:  " + str(inversions))
    pass

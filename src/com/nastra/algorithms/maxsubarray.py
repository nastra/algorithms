'''
Solution to the maximum subarray problem.
@author: nastra - Eduard Tudenhoefner
'''
import sys
import math

def findMaxSubarray(array, low, high):
    if low == high:
        return (low, high, array[low])
    else:
        mid = math.floor((high + low) / 2)
        (leftLow, leftHigh, leftSum) = findMaxSubarray(array, low, mid)
        (rightLow, rightHigh, rightSum) = findMaxSubarray(array, mid + 1, high)
        (crossLow, crossHigh, crossSum) = findMaxCrossingSubarray(array, low, mid, high)
        
        if(leftSum >= rightSum and leftSum >= crossSum):
            return (leftLow, leftHigh, leftSum)
        elif(rightSum >= leftSum and rightSum >= crossSum):
            return (rightLow, rightHigh, rightSum)
        else:
            return (crossLow, crossHigh, crossSum)

def findMaxCrossingSubarray(array, low, mid, high):
    leftSum = -sys.maxsize - 1
    rightSum = -sys.maxsize - 1
    maxLeft = mid
    maxRight = mid
    total = 0
    for i in range(mid, low, -1):
        total += array[i]
        if total > leftSum:
            leftSum = total
            maxLeft = i
    total = 0    
    for j in range(mid + 1, high, 1):
        total += array[j]
        if total > rightSum:
            rightSum = total
            maxRight = j
        
    return (maxLeft, maxRight, leftSum + rightSum)

if __name__ == '__main__':
    array = [-5, 3, 1, -1, 7, 12, -9, 13, -34, -12, -2, 6, -1, 11, -4, 13, 2, -1]
    (startsAt, endsAt, maxSum) = findMaxSubarray(array, 0, len(array) - 1)
    print("Found a maximum sum of: " + str(maxSum))
    print("Starts at: " + str(startsAt) + " ---- Ends at: " + str(endsAt))
    subarray = array[startsAt:endsAt + 1]
    print(subarray)
    pass

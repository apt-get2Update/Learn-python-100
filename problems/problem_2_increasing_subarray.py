'''
Find all increasing subsequences of an array

Given an integer array, find all distinct increasing subsequences of length two or more.

For example,

Input: [2, 4, 5, 6]
Output: [[2, 4, 5] [4, 5, 6], [2, 5], [2, 4], [4, 5]]
 
Input: [3, 2, 1]
Output: []
'''



from collections import deque
 
def findsubArray(numArray, result, curr=deque(), start=0):
    # if the current sequence has length of two or more, push it to the result set
    if len(curr) >= 2:
        result.append(list(curr))
 
    # start from the next index till the last
    for i in range(start, len(numArray)):
        # if sequence is empty, or current number is more than the previous number
        # in the sequence
        if not curr or numArray[i] > curr[-1]:
            # append current number to the sequence
            curr.append(numArray[i])
            # findsubArray for the next index `i+1`
            findsubArray(numArray, result, curr, i + 1)
            # backtrack: remove current number from the sequence
            curr.pop()
 
 
def findSubsequences(numArray):
    result = []
    findsubArray(numArray, result)
    return result
 
 
if __name__ == '__main__':
    numArray = [2, 4, 5, 6]
 
    result = findSubsequences(numArray)
    print(result)
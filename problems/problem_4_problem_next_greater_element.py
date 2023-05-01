
'''
Find the next greater element for every array element

Given an integer array, find the next greater element for every array element. 
The next greater element of a number x is the first greater number to the right of x in the array.

In other words, for each element A[i] in the array A, 
find an element 
A[j] such that j > i and 
A[j] > A[i] and the value of j should be as minimum as possible. If the next greater element 
doesn’t exist in the array for any element, consider it -1.

 
For example,

Input:  [2, 7, 3, 5, 4, 6, 8]
Output: [7, 8, 5, 6, 6, 8, -1]
 
 
Input:  [5, 4, 3, 2, 1]
Output: [-1, -1, -1, -1, -1]
 
 
Note that the next greater element for the last array element is always -1.
    
'''


# def check(num):
#     nums = num

#     #  [2, 7, 3, 5, 4, 6, 8]
#     val = []
#     for i in range(0,len(num)):
#         for j in range(i+1, len(num)):
#             if num[i] < num[j]:
#                 num[i] = num[j]
#                 break
#             elif j == len(num)-1:
#                 num[i] = -1
#             print(j)

#     print(num)
#     print(val)
# check([2, 7, 3, 5, 4, 6, 8])




def findNextGreaterElements(input):
 
    # base case
    if not input:
        return
 
    # do for each element
    for i in range(len(input)):
        # keep track of the next greater element for element `input[i]`
        next = -1
        # process elements on the right of element `input[i]`
        for j in range(i + 1, len(input)):
            # break the inner loop at the first larger element on the
            # right of element `input[i]`
            if input[j] > input[i]:
                next = input[j]
                break
 
        print(next, end=' ')
 
 
if __name__ == '__main__':
 
    input = [2, 7, 3, 5, 4, 6, 8]
    findNextGreaterElements(input)
 
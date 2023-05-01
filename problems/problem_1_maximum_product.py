'''
Find the maximum product of two integers in an array

Given an integer array, find the maximum product of two integers in it.

For example, consider array {-10, -3, 5, 6, -2}. 
The maximum product is the (-10, -3) or (5, 6) pair.
'''

'''
1,2 = > -10 * -3 = 30
-10*5 = -50
-10*6 = -60
-10*-2 =  -20

-3 * 5
-3 *6
-3 * -2
5* 6
5 * -2
6* -2

'''

pmax=0
psmx =0
nmax = 0
nsmx = 0

arr = [-10, -3, 5, 6, -2]

nmax = -10
nsmax = -3
pmax = 6
psmax = 5

def findMaximumProduct_traversal(A):
 
    # to store the maximum and second maximum element in a list
    max1 = A[0]
    max2 = -sys.maxsize
 
    # to store the minimum and second minimum element in a list
    min1 = A[0]
    min2 = sys.maxsize
 
    for i in range(1, len(A)):
 
        # if the current element is more than the maximum element,
        # update the maximum and second maximum element
        if A[i] > max1:
            max2 = max1
            max1 = A[i]
 
        # if the current element is less than the maximum but greater than the
        # second maximum element, update the second maximum element
        elif A[i] > max2:
            max2 = A[i]
 
        # if the current element is less than the minimum element,
        # update the minimum and the second minimum
        if A[i] < min1:
            min2 = min1
            min1 = A[i]
 
        # if the current element is more than the minimum but less than the
        # second minimum element, update the second minimum element
        elif A[i] < min2:
            min2 = A[i]
 
        # otherwise, ignore the element
 
    # choose the maximum of the following:
    # 1. Product of the maximum and second maximum element or
    # 2. Product of the minimum and second minimum element
    if max1 * max2 > min1 * min2:
        print("Pair is", (max1, max2))
    else:
        print("Pair is", (min1, min2))


    findMaximumProduct_traversal([[-10, -3, 5, 6, -2]])


[-10, -3, -2, 5, 6]
import sys
print(sys.maxsize)
def manual():
    max = None
    max_i= 0 
    max_j = 0
    nums = [-10, -3, 5, 6, -2]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if max is not None:
                if max < nums[i]*nums[j]:
                    max = nums[i]*nums[j]
                    max_j = nums[j]
                    max_i= nums[i]
            else:
                max = nums[i]*nums[j]
                max_j = nums[j]
                max_i= nums[i]
            # print(nums[i]*nums[j])
    print(max_i)
    print(max_j)

manual()



#  O(n.log(n))
def findMaximumProduct_sorting(A):
 
    # `n` is the length of the list
    n = len(A)
 
    # base case
    if n < 2:
        return
 
    # sort list in ascending order
    A.sort()
 
    # choose the maximum of the following:
    # 1. Product of the first two elements or
    # 2. Product of the last two elements.
 
    if (A[0] * A[1]) > (A[n - 1] * A[n - 2]):
        print("Pair is", (A[0], A[1]))
    else:
        print("Pair is", (A[n - 1], A[n - 2]))
findMaximumProduct_sorting([-10, -3, 5, 6, -2])

# import sys
 

#  #O(n^2)
 
# # A naive solution to finding the maximum product of two integers in a list
# def findMaximumProduct_bruit_force(A):
 
#     # base case
#     if len(A) < 2:
#         return
 
#     max_product = -sys.maxsize
#     max_i = max_j = -1
 
#     # consider every pair of elements
#     for i in range(len(A) - 1):
#         for j in range(i + 1, len(A)):
#             # update the maximum product if required
#             if max_product < A[i] * A[j]:
#                 max_product = A[i] * A[j]
#                 (max_i, max_j) = (i, j)
 
#     print("Pair is", (A[max_i], A[max_j]))
 
 
# #  O(n.log(n))
# def findMaximumProduct_sorting(A):
 
#     # `n` is the length of the list
#     n = len(A)
 
#     # base case
#     if n < 2:
#         return
 
#     # sort list in ascending order
#     A.sort()
 
#     # choose the maximum of the following:
#     # 1. Product of the first two elements or
#     # 2. Product of the last two elements.
 
#     if (A[0] * A[1]) > (A[n - 1] * A[n - 2]):
#         print("Pair is", (A[0], A[1]))
#     else:
#         print("Pair is", (A[n - 1], A[n - 2]))
 
 



# def findMaximumProduct_traversal(A):
 
#     # to store the maximum and second maximum element in a list
#     max1 = A[0]
#     max2 = -sys.maxsize
 
#     # to store the minimum and second minimum element in a list
#     min1 = A[0]
#     min2 = sys.maxsize
 
#     for i in range(1, len(A)):
 
#         # if the current element is more than the maximum element,
#         # update the maximum and second maximum element
#         if A[i] > max1:
#             max2 = max1
#             max1 = A[i]
 
#         # if the current element is less than the maximum but greater than the
#         # second maximum element, update the second maximum element
#         elif A[i] > max2:
#             max2 = A[i]
 
#         # if the current element is less than the minimum element,
#         # update the minimum and the second minimum
#         if A[i] < min1:
#             min2 = min1
#             min1 = A[i]
 
#         # if the current element is more than the minimum but less than the
#         # second minimum element, update the second minimum element
#         elif A[i] < min2:
#             min2 = A[i]
 
#         # otherwise, ignore the element
 
#     # choose the maximum of the following:
#     # 1. Product of the maximum and second maximum element or
#     # 2. Product of the minimum and second minimum element
#     if max1 * max2 > min1 * min2:
#         print("Pair is", (max1, max2))
#     else:
#         print("Pair is", (min1, min2))

# if __name__ == '__main__':
#     B = [-10, -3, 5, 6, -20]
#     A = [-10, -3, 5, 6, -2]
#     findMaximumProduct_bruit_force(A)
#     findMaximumProduct_sorting(A)
#     findMaximumProduct_traversal(A)
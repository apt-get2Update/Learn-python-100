
'''
Find the smallest missing positive number from an unsorted array

Given an unsorted integer array, find the smallest missing positive integer in it.

For example,

Input:  {1, 4, 2, -1, 6, 5}
Output: 3
 
Input:  {1, 2, 3, 4}
Output: 5

'''

def findSmallestMissing(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] > 0:
            if(nums[i]+1 != nums[i+1]):
                print(nums[i]+1)
                break
 
 
if __name__ == '__main__':
 
    nums = [1, 4, 2, -1, 6, 5]
    
    print(nums)
    print('The smallest missing positive number from the array is',
        findSmallestMissing(nums))
'''
Find all duplicate elements in a limited range array

Find the duplicate numbers in an integer array of size n that contains elements between 1 and n, at least one of which repeats.

For example,

Input: nums[] = [5, 3, 4, 2, 5, 1, 2]
Output: [5, 2]
 
Input: [1, 2, 3]
Output: []
'''

freq = {
    "name":"murugan"
}
print(freq)
value = freq.setdefault("name","thiru")
print(value)
print(freq)
    







#O(n)
def findDuplicates_using_map(nums):
    # create an empty map to store the count of each array element

    freq = {}
    # [5, 3, 4, 2, 5, 1, 2]
    # {
        
    # }

 
    # traverse the input array and update the frequency of each element
    for i in nums:
        freq[i] = freq.setdefault(i, 0) + 1
 
    # iterate through the frequency map and collect elements having a count of two or more
    return {key for key in freq.keys() if freq[key] >= 2}
 
 
if __name__ == '__main__':
    nums = [5, 3, 4, 2, 5, 1, 2]
    result = findDuplicates_using_map(nums)
    print(result) 
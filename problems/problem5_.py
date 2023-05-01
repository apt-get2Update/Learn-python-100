'''
Find a pair with the given sum in a circularly sorted array

Given a circularly sorted integer array, find a pair with a given sum. Assume there are no duplicates in the array, and the rotation is in an anti-clockwise direction around an unknown pivot.

For example

Input:  A[] = { 10, 12, 15, 3, 6, 8, 9 }, target = 18
 
Output: Pair found (3, 15)
 
 
Input:  A[] = { 5, 8, 3, 2, 4 }, target = 12
 
Output: Pair found (4, 8)
 
 
Input:  A[] = { 9, 15, 2, 3, 7 }, target = 20
 
Output: Pair not found
'''

def findPair(arr, target):
    pair=[]
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)-1):
            if(arr[i]+arr[j] == target):
                pair.append((arr[i],arr[j]))
                print(f'Pair found ({arr[i]}, {arr[j]}))')
    print(pair)
findPair([ 9, 15, 2, 3, 7 ],18)
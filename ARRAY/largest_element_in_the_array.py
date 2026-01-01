# Find the largest element in an array
#
# Problem Statement: Given an array, we have to find the smallest element in the array.
#
# Examples:
#
# Example 1:
# Input: arr[] = {2,5,1,3,0};
# Output: 5
# Explanation: 5 is the smallest element in the array.
#
# Example2:
# Input: arr[] = {8,10,5,7,9};
# Output: 10
# Explanation: 10 is the smallest element in the array.

def largest(arr):
    maxi=arr[0]
    for i in range(len(arr)):
        if arr[i]>maxi:
            maxi=arr[i]
    return maxi

arr=[8,10,5,7,9]
print(largest(arr))
# Find the smallest element in an array
#
# Problem Statement: Given an array, we have to find the smallest element in the array.
#
# Examples:
#
# Example 1:
# Input: arr[] = {2,5,1,3,0};
# Output: 0
# Explanation: 0 is the smallest element in the array.
#
# Example2:
# Input: arr[] = {8,10,5,7,9};
# Output: 5
# Explanation: 5 is the smallest element in the array.

def smallest(arr):
    min_element=arr[0]
    for i in range(len(arr)):
        if arr[i]<min_element:
            min_element=arr[i]
    return min_element
array=[8,10,5,7,9]
print(smallest(array))
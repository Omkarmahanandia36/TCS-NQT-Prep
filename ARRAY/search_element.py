# problem Statement: Search an element in an array and return its position
# Example 1:
# Input: array[] = {1,2,3,4,5} k=3                                                                              
# Output: 2                                                                                                             
# Explanation: The answer is 2 because 3 is present at 2nd index.

# Example 2:
# Input: array[]={6,7,9,5,3,10} k=10
# Output: 5
# Explanation: The answer is 5 because 10 is present at 5th index.

#sorted array
def search(arr, k):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == k:
            return mid
        elif k>arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
k = 3
print(search(arr, k))

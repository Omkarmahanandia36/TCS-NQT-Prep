# Problem statement: Given an array, we have found the number of occurrences of each element in the array.

# Examples:

# Example 1:
# Input: arr[] = {10,5,10,15,10,5};
# Output: 10  3
# 	 5  2
#         15  1
# Explanation: 10 occurs 3 times in the array
# 	      5 occurs 2 times in the array
#               15 occurs 1 time in the array

# Example2: 
# Input: arr[] = {2,2,3,4,4,2};
# Output: 2  3
# 	3  1
#         4  2
# Explanation: 2 occurs 3 times in the array
# 	     3 occurs 1 time in the array
#              4 occurs 2 time in the array

def count(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for i in freq:
        print(i, "=", freq[i])
    return
arr=[2,2,3,4,4,2]
print(count(arr))
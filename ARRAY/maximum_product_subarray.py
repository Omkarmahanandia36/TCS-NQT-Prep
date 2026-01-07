# Given an integer array nums. Find the subarray with the largest product, and return the product of the elements present in that subarray.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Examples:
# Input: nums = [4, 5, 3, 7, 1, 2]
# Output: 840
# Explanation: The largest product is given by the whole array itself

# Input: nums = [-5, 0, -2]
# Output: 0

# Explanation: The largest product is achieved with the following subarrays [0], [-5, 0], [0, -2], [-5, 0, -2].
# current solution is correct but has a time complexity of O(n²) due to the nested loops. We can make it far more efficient using Kadane’s algorithm-inspired 
# approach for products

#using kadane's algorithm

def max_product_subarray(arr):
    x=1
    maximum=float("-inf")
    for i in range(len(arr)):
       x*=arr[i]
       maximum=max(maximum,x)
       if arr[i]==0:
            x=1
    return maximum
           
arr=[-5, 0, -2]
answer=max_product_subarray(arr)
print(answer)
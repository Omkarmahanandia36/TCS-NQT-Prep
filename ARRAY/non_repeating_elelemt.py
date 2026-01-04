# Problem Statement: Find all the repeating elements present in an array.

# Examples:

# Example 1:
# Input: 
# Arr[] = [1,1,2,3,4,4,5,2]
# Output:
#  1,2,4
# Explanation:
#  1,2 and 4 are the elements which are occurring more than once.

# Example 2:
# Input:
#  Arr[] = [1,1,0]
# Output:
#  1
# Explanation:
#  Only 1 is occurring more than once in the given array.

def repeate(arr):
    frequency={}
    answer=[]
    for word in arr:
        if word in frequency:
            frequency[word]+=1
        else:
            frequency[word]=1
    for key,value in frequency.items():
        if value==1:
            answer.append(key)
    return answer
arr=[1,1,2,3,4,4,5,2]
print(repeate(arr))
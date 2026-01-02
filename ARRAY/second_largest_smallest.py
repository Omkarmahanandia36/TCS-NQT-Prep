
def second_largest(arr):
    largest=arr[0]
    second_largest=arr[0]
    for i in range(len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    for i in range(len(arr)):
        if arr[i]!=largest and arr[i]>second_largest:
            second_largest=arr[i]
    return second_largest

def second_smallest(arr):
    small=arr[0]
    smallest=arr[0]
    for i in range(len(arr)):
        if arr[i]<small:
            small=arr[i]
    for i in range(len(arr)):
        if arr[i]!=small and arr[i]<smallest:
            smallest=arr[i]
    return smallest
arr=[5, 3, 8, 1, 9, 2]
answer=[second_largest(arr),second_smallest(arr)]
print(answer)



#sorting technique
array=[5, 3, 8, 1, 9, 2]
array.sort()
smallest2=array[1]
largest2=array[-2]
print([largest2,smallest2])
            
def rev(arr,mid):
    left=mid
    right=len(arr)-1
    
    while left<=right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right=right-1
    return arr

arr=[4, 2, 8, 6, 15, 5, 9, 20]
arr.sort()

mid=len(arr)//2
ans=rev(arr,mid)
print(ans)
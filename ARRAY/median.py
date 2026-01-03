def median(arr):
    arr.sort()
    n = len(arr)

    if n % 2 == 0:
        return (arr[n//2] + arr[n//2 - 1]) / 2
    else:
        return arr[n//2]

arr = [1,2,3,4,5,6,7,8,2]
answer = median(arr)
print(answer)

def product(arr):
    pro = 1
    total = []

    for i in arr:
        pro *= i

    for i in arr:
        total.append(pro // i)

    return total

arr = [1, 2, 3, 4]
answer = product(arr)
print(answer)

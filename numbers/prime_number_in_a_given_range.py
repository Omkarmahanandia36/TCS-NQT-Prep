def Prime(i):
    if i < 2:
        return False
    if i == 2:
        return True
    if i % 2 == 0:
        return False

    for num in range(3, int(i**0.5) + 1, 2):
        if i % num == 0:
            return False
    return True
def Isprime(mini,maxi):
    answer=[]
    for i in range(mini,maxi):
        if Prime(i):
            answer.append(i)
    return answer
minimum=int(input("Enter the minimum number :"))
maximu=int(input("enter the maximum number :"))
print(Isprime(minimum,maximu))
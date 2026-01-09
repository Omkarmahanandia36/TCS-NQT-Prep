def Palindrom(number):
    rev=0
    copy=number
    while copy>0:
        x=copy%10
        rev=rev*10+x
        copy=copy//10
    if number==rev:
        return True
    else:
        return False
def RangeOfNumber(mini,maxi):
    answer=[]
    for i in range(mini,maxi):
        if Palindrom(i)==True:
            answer.append(i)
    return answer
        
mini=int(input("enter the minimum number : "))
maxi=int(input("Enter the maximum number : "))
answer=RangeOfNumber(mini,maxi)
print(answer)    
def NumberPalindrom(number):
    rev=0
    copy=number
    while copy>0:
        x=copy%10
        rev=rev*10+x
        copy=copy//10
    if number==copy:
        return True
    else:
        return False
    
x=int(input("enter a number"))
print(NumberPalindrom(x))
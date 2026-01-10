def armstrong(number):
    original=number
    sumi=0
    l=len(str(number))
    while number >0:
        x=number%10
        sumi+=x**l
        number=number//10
    if sumi==original:
        return True
    else:
        return False
print(armstrong(153))
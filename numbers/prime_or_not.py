def PrimeNumber(number):
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False 
    return True
number=int(input("enter the number : "))
print(PrimeNumber(number))
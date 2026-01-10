def perfectNumber(number):
    if number < 2:
        return False

    sumi = 0
    for i in range(1, number):
        if number % i == 0:
            sumi += i

    return sumi == number


def numbers(mini, maxi):
    perfect_numbers = []
    for i in range(mini, maxi):
        if perfectNumber(i):
            perfect_numbers.append(i)
    return perfect_numbers


mini = 0
maxi = 50
print(numbers(mini, maxi))

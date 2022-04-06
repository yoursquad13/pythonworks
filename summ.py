num = int(input("Enter a number: "))


def sumcount(some):
    summ = 0
    for i in range(1,some + 1):
        if i % 2 == 1:
            summ = summ + i
    return summ


print(sumcount(num))

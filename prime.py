x = int(input("Enter a number: "))
y = x - 1

isPrime = "Prime Number"

if x != 2:
    while y >= 2:
        if(x % y == 0):
            isPrime = "Not Prime Number"
            break
        y = y - 1

print(x," is ",isPrime)

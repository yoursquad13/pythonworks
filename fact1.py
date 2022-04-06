x = int(input("Enter a number: "))

if x <= 0:
    print("Enter a positive number")
else:
    y = 1
    while x > 1:
        y = y * x
        x -= 1

print("Factorial is ",y)
        

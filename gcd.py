x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
if x > y: 
    small = y 
else: 
    small = x 

i=1
while i <= small:
    if((x%i ==0) and (y%i==0)):
        gcd = i
        i+=1

print(gcd)

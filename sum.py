num = int(input("Enter a number: "))
summ = 0

#for i in range(0,len(num)):
 #   summ = summ + int(num[i])

#print('The sum is: ',summ)

num = num
arr = []
for i in range(0,len(str(num))):
    arr.append(num % 10)
    num = int(num/10)
    summ = summ + arr[i]
print(arr)

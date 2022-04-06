n = int(input("Enter number of numbers in list: "))
numList = []

for i in range(0,n):
    numb = int(input("Enter a number: "))
    numList.append(numb)

#print(numList)

minnum = numList[0]
maxnum = numList[0]

for number in numList:
    if minnum > number: 
        minnum = number
    if maxnum < number:
        maxnum = number

print("Maximum is ", maxnum,"\nMinimum is ", minnum)

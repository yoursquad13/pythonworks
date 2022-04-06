list1 = ['a','b','c']
list2 = [1,2,3]
list3 = []

for i in range(0,len(list1)):
    list3.append(list1[i])
    list3.append(list2[i])

print("Combined list: \n",list3)

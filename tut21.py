list1 = [[24,3,6],[8,12,18],[2,66,7]]
div = []
maxx = list1[0][0]
minn = list1[0][0]

for i in list1:
    for j in i:
        if j % 2 == 0 and j % 3 == 0:
            div.append(j)
        if j > maxx:
            maxx = j
        if j < minn:
            minn = j



print("Number divisible by 2 and 3 are: ",div,"\nMaximum is: ",maxx,"\nMinimum is: ",minn)

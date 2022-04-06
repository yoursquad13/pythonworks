matrix = [[2,3,4],[1,5,6],[5,8,5]]
summ = 0
maxx=matrix[0][0]
minn=matrix[0][0]

#Calculating the sum of diagonal elements
for i in range(0,3):
    summ = summ + matrix[i][i]

print('The sum of diagonol elements: ',summ)


#Finding minimum and maximum value
for i in matrix:
    for j in i:
        if j > maxx:
            maxx=j
        if j < minn:
            minn = j

print('Minimum: ',minn,'\nMaximum: ',maxx)

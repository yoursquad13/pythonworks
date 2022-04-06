num = int(input('Enter the number of students: '))

std = {}

for i in range(0,num):
    name = input('Enter the name of student: ')
    marks = int(input('Enter the marks obtained '))
    std[name]=marks

minn = 100
maxx = 0
avg = 0
count = 0
for name in std:
    count = count + 1
    avg = avg + std[name]
    if std[name] > maxx:
        maxx = std[name]
    if std[name] < minn:
        minn = std[name]
avg = avg/count
print('Minimum marks obtained: ',minn,'\nMaximum marks obtained: ',maxx,'\nAverage marks obtained: ',avg)

std={'john':{'math':88,'english':86,'physics':76,'computer':66,'nepali':76},
    'sam':{'math':77,'english':67,'physics':87,'computer':67,'nepali':56},
     'anna':{'math':67,'english':65,'physics':67,'computer':76,'nepali':65},
     'ben':{'math':87,'english':78,'physics':67,'computer':77,'nepali':57},
     'jeff':{'math':90,'english':80,'physics':79,'computer':88,'nepali':70}
     }
#print(std)
avg = {}
for i in std:
    savg = 0
    for j in std[i]:
      savg = savg + std[i][j]
    avg[i]=savg/5

print('Average marks obtained by each student is listed below: ')
for i in avg:
    print(i,': ',avg[i])

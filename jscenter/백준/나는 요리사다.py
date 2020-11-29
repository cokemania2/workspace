maxx = 0
maxi = 0
for i in range(5) :
    tmp = sum(map(int,input().split(' ')))
    if tmp > maxx :
        maxx = tmp
        maxi = i + 1
print(maxi,maxx)

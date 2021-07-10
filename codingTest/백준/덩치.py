N = int(input())
a = []
for i in range(N) :
    a += [list(map(int,input().split(' ')))]
for i in range(N) :
    rank = 1
    for j in range(N) :
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            rank += 1
    print(rank,end =' ')
            

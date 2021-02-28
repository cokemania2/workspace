##https://www.acmicpc.net/problem/11557
##Yangjojang of The Year

T = int(input())
for i in range(T) :
    N = int(input())
    maxName = ''
    maxx = 0
    for j in range(N) :
        n, d = input().split(' ')
        if int(d) >= maxx :
            maxxName = n
            maxx = int(d)
    print(maxxName)

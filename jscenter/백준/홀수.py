##https://www.acmicpc.net/problem/2576
##홀수
minn = 1000
summ = 0
for i in range(7) :
    a = int(input())
    if a % 2 == 1 :
        summ += a
        if a < minn :
            minn = a
if summ == 0 :
    print(-1)
else : 
    print(summ)
    print(minn)

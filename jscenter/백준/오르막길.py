##https://www.acmicpc.net/problem/2846
##오르막길

before = 0
summ = 0
maxx = 0
N = int(input())
P = list(map(int,input().split(' ')))
for i in range(1,N) :
    if P[i] > P[i - 1]  :# 이전 숫자보다 크면
        summ += P[i] - P[i - 1]
    else :
        if summ > maxx :
            maxx = summ
        summ = 0
if summ > maxx :
    maxx = summ
print(maxx)

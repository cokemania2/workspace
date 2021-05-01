##https://www.acmicpc.net/problem/16466
##콘서트

arr = [True] * 1000000
N = int(input())
n = list(map(int,input().split(' ')))
for i in range(N) :
    arr[n[i] - 1] = False
for i in range(1000000) :
    if arr[i] == True :
        print(i + 1)
        break
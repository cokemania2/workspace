# https://www.acmicpc.net/problem/4948
# 베르트랑 공준.py

arr = [0, 0] + [1]*(123456*2)
for i in range(2,len(arr)):
    for j in range(2,len(arr)):
        if i*j >= len(arr):
            break
        if arr[i*j]:
            arr[i*j] = 0
while True:
    n = int(input())
    if n == 0 :
        break
    print(sum(arr[n+1:2*n+1]))

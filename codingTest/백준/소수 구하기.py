# https://www.acmicpc.net/problem/1929
# 소수 구하기.py

M, N = map(int, input().split())
arr = [False, False] + [True]*N
for i in range(2,N):
    for j in range(2,N):
        if i*j > N:
            break
        if arr[i*j]:
            arr[i*j] = False
for i in range(M,N+1):
    if arr[i]:
        print(i)
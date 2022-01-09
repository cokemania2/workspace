# https://www.acmicpc.net/problem/11728
# 배열 합치기.py

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(sorted(A+B))
for i in C:
    print(i,end=' ')
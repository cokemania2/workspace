# 공.py
# https://www.acmicpc.net/problem/1547

answer = 1
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    if x == answer:
        answer = y
    elif y == answer:
        answer = x
print(answer)
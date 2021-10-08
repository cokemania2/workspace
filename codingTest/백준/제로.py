# https://www.acmicpc.net/problem/10773
# 제로.py

import sys

answer = []
recent = 0
K = int(input())
for i in range(K):
    n = int(sys.stdin.readline())
    if n != 0:
        answer.append(n)
    else:
        answer.pop()
print(sum(answer))
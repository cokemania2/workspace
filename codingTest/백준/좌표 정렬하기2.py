# https://www.acmicpc.net/problem/11651
# 좌표 정렬하기 2.py

import sys
N = int(input())

answer = [] 
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    answer.append([a, b])
for i in list(sorted(answer, key=lambda x : (x[1], x[0]))):
    print(i[0],i[1])
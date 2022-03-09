# https://www.acmicpc.net/problem/2012
# 등수 매기기.py
import sys

answer = 0
score = []
n = int(input())
for i in range(n):
    score.append(int(sys.stdin.readline()))
score = sorted(score)
for i, v in enumerate(score):
    answer += abs(v-(i+1))
print(answer)
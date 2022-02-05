# https://www.acmicpc.net/problem/11508
# 2+1 세일.py

answer = 0
milk = []
n = int(input())
for i in range(n):
    milk.append(int(input()))
milk.sort(reverse=True)
for i,v in enumerate(milk):
    if i % 3 == 2:
        continue
    answer += v
print(answer)
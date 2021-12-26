# https://www.acmicpc.net/problem/14659
# 한조서열정리하고옴ㅋㅋ.py

count = 0
maxCount = 0
n = int(input())
N = list(map(int,(input().split())))
tmp = N[0]

for i in range(1, n):
    if N[i] < tmp:
        count += 1
        if count > maxCount:
            maxCount = count
    else:
        tmp = N[i]
        count = 0
print(max(maxCount, count))
# https://www.acmicpc.net/problem/11650
# 좌표 정렬하기.py

coordinate = []
n = int(input())
for i in range(n):
    coordinate.append(list(map(int,input().split())))
coordinate.sort(key=lambda x : (x[0], x[1]))
for x in coordinate:
    print(x[0],x[1]) 
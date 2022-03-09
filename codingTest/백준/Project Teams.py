# https://www.acmicpc.net/problem/20044
# Project Teams.py

n = int(input())
w = sorted(list(map(int,input().split())))
print(min([w[i] + w[len(w)-1-i] for i in range(len(w) // 2)]))
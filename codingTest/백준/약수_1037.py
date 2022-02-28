# https://www.acmicpc.net/problem/1037
# 약수.py
a = int(input())
b = list(map(int,(input().split())))
b.sort()
print(b[0]*b[len(b)-1])
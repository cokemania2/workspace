# https://www.acmicpc.net/problem/1269
# 대칭 차집합.py

d = input()
a = set(input().split())
b = set(input().split())
c = set(a ^ b)
print(len(c))
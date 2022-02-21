# https://www.acmicpc.net/problem/11536
# 줄 세우기.py

names = []
n = int(input())
for i in range(n):
    names.append(input())
if names == sorted(names):
    print('INCREASING')
elif names == sorted(names,reverse=True):
    print('DECREASING')
else:
    print('NEITHER')

# https://www.acmicpc.net/submit/11098/36075021
# 첼시를 도와줘!.py

n = int(input())
for i in range(n):
    p = int(input())
    print(list(sorted([input().split() for i in range(p)], key= lambda x : int(x[0])))[-1][1])
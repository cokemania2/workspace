# https://www.acmicpc.net/problem/1764
# 듣보잡.py

import sys

N_list =[]
N_dic ={}
answer = []

N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    ㅕnput = sys.stdin.readline().split('\n', 1)[0]
    N_list.append(nput)
    N_dic[nput] = True
for i in range(M):
    mput = sys.stdin.readline().split('\n', 1)[0]
    if mput in N_dic:
        answer.append(mput)
answer = list(sorted(answer))
print(len(answer))
for i in answer:
    print(i)

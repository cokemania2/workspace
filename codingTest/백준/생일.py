# https://www.acmicpc.net/problem/5635
# 생일.py

from datetime import datetime

n = int(input())
answer_list = [[]  for i in range(n)]
for i in range(n):
    info = input().split()
    answer_list[i].append(info[0])
    answer_list[i].append(datetime.strptime("/".join(info[1:]), '%d/%m/%Y'))
answer = list(sorted(answer_list, key=lambda x : x[1]))
print(answer[-1][0])
print(answer[0][0])
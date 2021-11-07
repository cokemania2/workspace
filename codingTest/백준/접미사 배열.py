# https://www.acmicpc.net/problem/11656
# 접미사 배열.py

S = input()
answer = [S]
for i in range(1,len(S)):
    answer.append(S[-i:])
answer = list(sorted(answer))
for i in answer:
    print(i)
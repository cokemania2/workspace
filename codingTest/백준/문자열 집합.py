# https://www.acmicpc.net/submit/14425/35827871
# 문자열 집합.py

answer = 0
N, M = map(int, input().split())
s = [input()  for i in range(N)]
check = [input()  for i in range(M)]
for i in check:
    if i in s:
        answer += 1
print(answer)
# https://www.acmicpc.net/problem/1436
# 영화감독 숌.py

answer = 0
i = 666
n = 0
N = int(input())
while True:
    if '666' in str(i):
        answer += 1
        n += 1
    if n == N:
        print(i)
        break
    i += 1
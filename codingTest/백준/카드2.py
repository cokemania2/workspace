# https://www.acmicpc.net/problem/2164
# 카드2.py

from collections import deque

N = int(input())

deque2 = deque([i for i in range(1, N+1)])
while True:
    e = deque2.popleft()
    if len(deque2) == 0:
        print(e)
        break
    deque2.append(deque2.popleft())
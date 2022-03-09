# https://www.acmicpc.net/problem/1966
# 프린터 큐.py
from collections import deque

t = int(input())
for i in range(t):
    index = [0 for _ in range(9)]
    star = {}
    n, m = map(int,input().split()) 
    doc = deque(list(map(int, input().split())))
    for j in doc:
        index[j-1] += 1
    star[0] = doc[m]
    doc[m] = 0
    answer = 1
    while True:
        if doc[0] == 0:
            if star[0] == 9:
                print(answer)
                break
            elif sum(index[star[0]:]) == 0:
                print(answer)
                break
        if sum(index[doc[0]:]) == 0:
            index[doc[0]-1] -= 1
            doc.popleft()
            answer += 1
            continue
        doc.append(doc.popleft())
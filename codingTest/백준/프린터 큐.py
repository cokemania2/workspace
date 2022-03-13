# https://www.acmicpc.net/problem/1966
# 프린터 큐.py
from collections import deque

t = int(input())
for i in range(t):
    answer = 1
    index = [0 for _ in range(9)]
    n, m = map(int,input().split()) 
    doc = deque(list(map(int, input().split())))
    # 우선순위를 index에 등록
    for j in doc:
        index[j-1] += 1
    # 정답을 0으로 변환해준다. 
    star = {}
    star[0] = doc[m]
    doc[m] = 0
    
    while True:
        # 정답이면
        if doc[0] == 0:
            # 우선순위가 9 == (최우선순위)
            if star[0] == 9:
                print(answer)
                break
            # index에 지금 정답보다 더 큰 우선순위가 있는지 확인 
            elif sum(index[star[0]:]) == 0:
                print(answer)
                break
        # 정답은 아니지만 우선순위가 걸렸을경우
        if sum(index[doc[0]:]) == 0:
            index[doc[0]-1] -= 1
            doc.popleft()
            answer += 1
            continue
        doc.append(doc.popleft())
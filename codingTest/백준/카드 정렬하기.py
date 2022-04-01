# https://www.acmicpc.net/problem/1715
# 카드 정렬하기.py
import sys, heapq

answer = 0
result = 0
N = int(input())
cards = []
for i in range(N):
    cards.append(int(sys.stdin.readline()))
heapq.heapify(cards)
while len(cards) != 1:    
    result = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, result)
    answer += result
print(answer)
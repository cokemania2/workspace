# https://www.acmicpc.net/problem/2798
# 블랙잭.py

from itertools import combinations

N, M = map(int, input().split())
card = list(map(int, input().split()))
m = 0
for c in list(combinations(card, 3)):
    if M - sum(c) >= 0 and M - sum(c)  < M - m:
        m = sum(c)
print(m)
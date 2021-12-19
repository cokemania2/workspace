# https://www.acmicpc.net/problem/18406
# 럭키 스트레이트.py

N = list(map(int, input()))
half = len(N)//2
print('LUCKY' if sum(N[:half]) == sum(N[half:]) else 'READY')

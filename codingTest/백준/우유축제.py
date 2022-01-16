# https://www.acmicpc.net/problem/14720
# 우유축제.py

def solution(N, milk):
    count = 0
    pattern = [0, 1, 2]
    for v in milk:
        if v == pattern[count % 3]:
            count += 1
    return count

N = int(input())
milk = list(map(int, input().split(' ')))
print(solution(N, milk))
# https://www.acmicpc.net/problem/1783
# 병든 나이트.py

def solution(N, M):
    if N == 1 or M == 1:
        return 1
    if N == 2:
        tmp = 1 + (M-1) // 2 
        return min(tmp, 4)
    if M <= 4:
        return M
    if M <= 8:
        return 4 + (M - 4) // 2
    return M - 2


N, M = map(int ,input().split())
print(solution(N, M))
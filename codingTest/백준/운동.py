# https://www.acmicpc.net/problem/1173
# 운동.py

def soulution():
    N, m, M, T, R = map(int,input().split())
    time = 0
    pluse = m
    if m + T > M:
        return -1
    while N > 0:
        if pluse + T > M:
            pluse = (pluse - R) if (pluse - R) > m else m
        else:
            pluse += T
            N -= 1
        time += 1
    return time

print(soulution())
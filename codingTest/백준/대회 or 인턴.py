# https://www.acmicpc.net/problem/2875
# 대회 or 인턴.py

W, M, K = map(int, input().split())
count = 0 
while True:
    W -= 2
    M -= 1
    if W < 2 or M < 1 or W + M < K + 3:
        print(count)
        break
    count += 1
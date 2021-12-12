# https://www.acmicpc.net/problem/1932
# 정수 삼각형.py

n = int(input())
dp = [[] for i in range(n)]
t = [list(map(int, input().split())) for i in range(n)]
t.reverse()
print(dp, t)
dp[0] = t[0]
for i in range(1,n):
    for j in range(n-i):
        dp[i].append(max(dp[i-1][j], dp[i-1][j+1]) + t[i][j])
print(dp[-1][0])
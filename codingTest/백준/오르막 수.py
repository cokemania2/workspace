# https://www.acmicpc.net/problem/11057
# 오르막 수.py

n = int(input())
dp = [[] for _ in range(n)]
dp[0] = [1 for i in range(10)]
for i in range(1, n):
    dp[i].append(1)
    for j in range(1,10):
        dp[i].append(dp[i-1][j] + dp[i][j-1])
print(sum(dp[n-1]) % 10007)